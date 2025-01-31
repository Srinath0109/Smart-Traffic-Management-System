import cv2
import numpy as np

# Load YOLO Model
MODEL_WEIGHTS = "../models/yolov4.weights"
MODEL_CONFIG = "../models/yolov4.cfg"
LABELS_PATH = "../models/coco.names"

LABELS = open(LABELS_PATH).read().strip().split("\n")
net = cv2.dnn.readNetFromDarknet(MODEL_CONFIG, MODEL_WEIGHTS)
layer_names = net.getLayerNames()
layer_names = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

def detect_vehicles(frame):
    """Detect vehicles using YOLO"""
    height, width = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    detections = net.forward(layer_names)

    vehicle_count = 0
    for output in detections:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5 and LABELS[class_id] in ["car", "truck", "bus", "motorbike"]:
                vehicle_count += 1

    return vehicle_count
