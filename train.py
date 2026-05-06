from ultralytics import YOLO
import os

def main():
    # 1. Load the model
    model = YOLO('yolov8n.pt') # Loads a small, fast version

    # 2. Train the model
    # Note: We use 'data/data.yaml' because that's where we moved it
    model.train(
        data='data/data.yaml', 
        epochs=25,        # Start with 25 to test if it works
        imgsz=640,        # Standard image resolution
        device='cpu'      # Uses your laptop processor
    )

if __name__ == '__main__':
    main()