import cv2
from models.yolo_model import detect_vehicles
from config import CAMERA_SOURCE

def process_traffic():
    """Processes real-time traffic video and detects congestion"""
    cap = cv2.VideoCapture(CAMERA_SOURCE)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        vehicle_count = detect_vehicles(frame)

        cv2.putText(frame, f"Vehicles: {vehicle_count}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Traffic Analysis", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
