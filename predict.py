from ultralytics import YOLO

# Load your best model
model = YOLO('runs/detect/train/weights/best.pt') # Change 'train' to 'train2' if needed

# Run prediction on your NEW images
results = model.predict(source='test_images', save=True, conf=0.10)

print("Check 'runs/detect/predict2' to see if it found the debris!")