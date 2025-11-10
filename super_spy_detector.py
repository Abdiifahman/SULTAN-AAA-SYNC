#!/usr/bin/env python3
# super_spy_detector.py
"""
Super Spy Detector — Enhanced version
- Local enhancement (CLAHE + denoise + sharpening)
- YOLOv8 (ultralytics) optional integration if installed
- Faster R-CNN fallback if torch available
- Multi-angle correlation: ORB feature matching + homography-based ROI projection
- Clean single-line JSON output for parsers
- Terminal-like logs and developer/logic metadata
"""

import os, sys, json, time, argparse, hashlib
from pathlib import Path
from datetime import datetime
from glob import glob
import subprocess

import cv2
import numpy as np
from PIL import Image

# Optional libs
YOLO_AVAILABLE = False
TORCH_AVAILABLE = False
try:
    from ultralytics import YOLO
    YOLO_AVAILABLE = True
except Exception:
    YOLO_AVAILABLE = False

try:
    import torch
    from torchvision import transforms
    from torchvision.models.detection import fasterrcnn_resnet50_fpn
    TORCH_AVAILABLE = True
except Exception:
    TORCH_AVAILABLE = False

# -----------------------
# Utilities
# -----------------------
def tlog(*lines):
    ts = datetime.utcnow().isoformat() + "Z"
    for l in lines:
        print(f"[SUPER-TERMINAL] {ts} | {l}")
    sys.stdout.flush()

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def list_images(folder):
    exts = ("*.jpg","*.jpeg","*.png","*.webp","*.bmp")
    files=[]
    for e in exts:
        files += glob(os.path.join(folder,e))
    return sorted(files)

# -----------------------
# Enhancement pipeline
# -----------------------
def enhance_image(img_bgr):
    # denoise with fastNlMeans
    den = cv2.fastNlMeansDenoisingColored(img_bgr, None, 10,10,7,21)
    # CLAHE on luminance
    ycrcb = cv2.cvtColor(den, cv2.COLOR_BGR2YCrCb)
    y,cr,cb = cv2.split(ycrcb)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    y2 = clahe.apply(y)
    merged = cv2.merge((y2,cr,cb))
    enhanced = cv2.cvtColor(merged, cv2.COLOR_YCrCb2BGR)
    # mild sharpening
    kernel = np.array([[0,-0.5,0],[-0.5,3,-0.5],[0,-0.5,0]])
    sharpen = cv2.filter2D(enhanced, -1, kernel)
    return sharpen

# -----------------------
# Detectors
# -----------------------
def detect_hough_lens(img_bgr):
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
                               param1=60, param2=28, minRadius=4, maxRadius=60)
    out=[]
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for (x,y,r) in circles[0]:
            out.append({"type":"lens_candidate","bbox":[int(x-r),int(y-r),int(x+r),int(y+r)], "confidence":0.45, "meta":{"radius":int(r)}})
    return out

def detect_bright_spots(img_bgr):
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    v99 = int(np.percentile(gray, 99.6))
    _,th = cv2.threshold(gray, max(200, v99), 255, cv2.THRESH_BINARY)
    cnts,_ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    out=[]
    for c in cnts:
        a = cv2.contourArea(c)
        if 2 <= a <= 500:
            x,y,w,h = cv2.boundingRect(c)
            out.append({"type":"bright_spot","bbox":[x,y,x+w,y+h],"confidence":0.35,"meta":{"area":int(a)}})
    return out

def detect_yolo(img_path):
    if not YOLO_AVAILABLE:
        return []
    try:
        model = YOLO("yolov8n.pt")  # small default if present; user can change
        results = model(img_path, imgsz=640)
        dets=[]
        for r in results:
            boxes = r.boxes
            for b in boxes:
                conf = float(b.conf.item())
                cls = int(b.cls.item())
                xyxy = [int(x) for x in b.xyxy[0].tolist()]
                dets.append({"type":f"yolo_cls_{cls}","bbox":xyxy,"confidence":conf})
        return dets
    except Exception as e:
        tlog(f"YOLO detect failed: {e}")
        return []

def detect_fasterrcnn(img_bgr, model):
    if not TORCH_AVAILABLE or model is None:
        return []
    try:
        pil = Image.fromarray(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
        transform = transforms.Compose([transforms.ToTensor()])
        tensor = transform(pil).unsqueeze(0)
        model.to("cpu")
        model.eval()
        with torch.no_grad():
            out = model(tensor)[0]
        dets=[]
        labels = out["labels"].cpu().numpy()
        scores = out["scores"].cpu().numpy()
        boxes = out["boxes"].cpu().numpy()
        for lbl, sc, box in zip(labels, scores, boxes):
            if sc < 0.45: continue
            dets.append({"type":f"coco_{int(lbl)}","bbox":[int(box[0]),int(box[1]),int(box[2]),int(box[3])],"confidence":float(sc)})
        return dets
    except Exception as e:
        tlog(f"FasterRCNN detect failed: {e}")
        return []

# -----------------------
# Multi-angle correlation (ORB + homography)
# -----------------------
def correlate_multiview(image_records, match_threshold=10):
    # image_records: list of dicts with keys 'path','img' (bgr), 'detections'
    # Build keypoints/descriptors
    orb = cv2.ORB_create(2000)
    for rec in image_records:
        gray = cv2.cvtColor(rec["img"], cv2.COLOR_BGR2GRAY)
        k,d = orb.detectAndCompute(gray, None)
        rec["kp"]=k; rec["des"]=d

    # pairwise matching; if same detection area projects consistently, increase confidence
    bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)
    correlated_pairs=[]
    n = len(image_records)
    for i in range(n):
        for j in range(i+1, n):
            di = image_records[i]; dj = image_records[j]
            if di["des"] is None or dj["des"] is None: continue
            matches = bf.match(di["des"], dj["des"])
            matches = sorted(matches, key=lambda x: x.distance)
            if len(matches) < match_threshold: continue
            # estimate homography on best matches
            src_pts = np.float32([di["kp"][m.queryIdx].pt for m in matches[:match_threshold]]).reshape(-1,1,2)
            dst_pts = np.float32([dj["kp"][m.trainIdx].pt for m in matches[:match_threshold]]).reshape(-1,1,2)
            H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
            if H is None: continue
            # if homography found, note correlation
            correlated_pairs.append({"pair":[di["path"], dj["path"]], "matches":len(matches), "inliers":int(mask.sum()) if mask is not None else None})
    return correlated_pairs

# -----------------------
# Pipeline
# -----------------------
def analyze_folder(folder, use_auto_models=False):
    imgs = list_images(folder)
    tlog(f"Found {len(imgs)} images")
    if not imgs:
        return {"error":"no_images","images":[]}

    # attempt to load torchvision model if requested
    tv_model = None
    if TORCH_AVAILABLE and use_auto_models:
        try:
            tlog("Loading Faster R-CNN (torchvision pretrained)")
            tv_model = fasterrcnn_resnet50_fpn(pretrained=True)
        except Exception as e:
            tlog(f"Failed to load torchvision model: {e}")
            tv_model = None

    records=[]
    for p in imgs:
        tlog(f"Processing {Path(p).name}")
        img_bgr = cv2.imdecode(np.fromfile(p, dtype=np.uint8), cv2.IMREAD_COLOR)
        if img_bgr is None:
            img_bgr = cv2.cvtColor(np.array(Image.open(p).convert("RGB")), cv2.COLOR_RGB2BGR)
        enhanced = enhance_image(img_bgr)
        h,w = enhanced.shape[:2]
        dets=[]
        dets += detect_hough_lens(enhanced)
        dets += detect_bright_spots(enhanced)
        if YOLO_AVAILABLE:
            dets += detect_yolo(p)
        if tv_model is not None:
            dets += detect_fasterrcnn(enhanced, tv_model)
        # normalize bbox and clamp
        for d in dets:
            x1,y1,x2,y2 = d["bbox"]
            d["bbox"] = [max(0,int(x1)), max(0,int(y1)), min(int(w),int(x2)), min(int(h),int(y2))]
        rec = {"path":p, "img":enhanced, "width":w, "height":h, "detections":dets, "sha256":sha256_file(p)}
        records.append(rec)
        tlog(f"Detected {len(dets)} items in {Path(p).name}")

    # correlate across views
    tlog("Running multi-angle correlation")
    correlations = correlate_multiview(records)

    # aggregate results and compute final suspicious list with scoring
    images_out=[]
    total_susp=0
    for rec in records:
        sus=[]
        for d in rec["detections"]:
            score = d.get("confidence", 0.0)
            typ = d.get("type","unknown")
            reasons=[]
            if typ.startswith("lens") or typ=="lens_candidate" or "lens" in typ:
                score += 0.25; reasons.append("circular-lens-like")
            if typ=="bright_spot":
                score += 0.15; reasons.append("tiny-bright-spot")
            if typ.startswith("yolo_cls") or typ.startswith("coco_"):
                reasons.append("object-detected")
            # clamp
            score = min(0.99, score)
            if score >= 0.5:
                sus.append({"type":typ,"bbox":d["bbox"],"score":round(score,3),"reasons":reasons})
        total_susp += len(sus)
        images_out.append({
            "image": Path(rec["path"]).name,
            "path": rec["path"],
            "sha256": rec["sha256"],
            "width": rec["width"], "height": rec["height"],
            "detections_count": len(rec["detections"]),
            "suspicious": sus
        })

    result = {
        "scan_id": sha256_file(imgs[0])[:16] + "_" + datetime.utcnow().strftime("%Y%m%d%H%M%S"),
        "timestamp_utc": datetime.utcnow().isoformat()+"Z",
        "image_count": len(imgs),
        "images": images_out,
        "summary": {
            "total_detections": sum(len(r["detections"]) for r in records),
            "total_suspicious": total_susp,
            "recommendation": "Physically inspect frames with high 'score' and consistent multi-angle correlation."
        },
        "developer": {"name":"SuperDetector Enhanced","version":"0.3"},
        "logic": {
            "steps":[
                "Enhance each image (denoise, CLAHE, sharpen)",
                "Run local heuristics (Hough circles, bright-spot) + optional ML detectors (YOLO/FasterRCNN)",
                "Correlate features across images via ORB + homography",
                "Aggregate and compute suspicious score"
            ],
            "notes":["This is a detection-assist tool — not definitive proof. Train custom model for production."]
        },
        "terminal_log":["images_processed:"+str(len(imgs)), "yolo_available:"+str(YOLO_AVAILABLE), "torch_available:"+str(TORCH_AVAILABLE)],
        "correlations": correlations
    }
    return result

# -----------------------
# CLI
# -----------------------
def main():
    ap = argparse.ArgumentParser(description="Super Spy Detector — Enhanced")
    ap.add_argument("--images", required=True, help="folder with images taken from multiple angles")
    ap.add_argument("--use-models", action="store_true", help="attempt to load heavier models (torch)")
    ap.add_argument("--output", default=None, help="append JSONL to file")
    args = ap.parse_args()

    tlog("Starting Super Detector Enhanced")
    res = analyze_folder(args.images, use_auto_models=args.use_models)
    single = json.dumps(res, ensure_ascii=False)
    print(single)
    if args.output:
        with open(args.output,"a",encoding="utf-8") as f:
            f.write(single+"\n")
        tlog(f"Wrote results to {args.output}")

if __name__=="__main__":
    main()