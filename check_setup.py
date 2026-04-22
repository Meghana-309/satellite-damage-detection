from ultralytics import YOLO
import os

# 1. Load a tiny pre-trained model
# This will download 'yolov8n.pt' automatically to your folder
model = YOLO('yolov8n.pt') 

# 2. Print success message
print("-" * 30)
print("SETUP SUCCESSFUL!")
print(f"YOLOv8 is ready in your virtual environment.")
print("-" * 30)