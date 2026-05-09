# Satellite and Space Debris Detection

An automated system to identify structural damage in satellites and track orbital debris using YOLOv8 and Computer Vision.

## Project Roadmap
- [x] Phase 1: Environment Setup ✅
- [x] Phase 2: Data Collection & Labeling ✅
- [x] Phase 3: Model Training ✅
- [x] Phase 4: Tracking & Collision Logic
- [ ] Phase 5: Dashboard Deployment

## Setup Instructions
1. Clone the repo
2. Create venv: `python -m venv venv`
3. Activate: `.\venv\Scripts\activate`
4. Install: `pip install ultralytics opencv-python pandas matplotlib`

## Project Progress

### Day 1: Environment Setup
- **Status:** Complete ✅
- **Activity:** Configured Python virtual environment and installed core deep learning libraries (PyTorch, Ultralytics).
- **Tooling:** Verified GPU/CPU compatibility and initialized the Git repository.

### Day 2: Data Preparation
- **Status:** Complete ✅
- **Activity:** Sourced space debris dataset and organized folders into Train, Test, and Validation sets.
- **Configuration:** Authored `data.yaml` to define object classes for the YOLOv8 model.

### Day 3: Model Training & Prediction
- **Status:** Complete ✅
- **Results:** Achieved a **mAP50 of 0.971 (97%)** after 25 epochs.
- **Validation:** Successfully ran `predict.py` on test images, identifying debris with high confidence.
## 🛰️ Day 6 & 7: Orbital Tracking & Collision Prediction

### **Overview**
Transitioned from static image detection to real-time orbital mechanics. Integrated live satellite data to predict potential collisions in Low Earth Orbit (LEO).

### **Key Technical Implementations**
*   **TLE Integration:** Automated retrieval of Two-Line Element (TLE) sets from Space-Track.org for 10+ orbital objects, including the ISS and Starlink constellations.
*   **SGP4 Propagation:** Implemented the SGP4 algorithm to convert TLE data into Earth-Centered Inertial (ECI) coordinates (x, y, z).
*   **Vectorized Risk Assessment:** Developed a collision engine using NumPy and Itertools to calculate Euclidean distances between all tracked objects.
*   **Threshold Logic:** Established safety protocols (High Risk < 5km, Medium Risk < 25km) to simulate Space Situational Awareness (SSA) workflows.

### **Results**
- **Live Positions:** Successfully generated a Pandas DataFrame of real-time satellite coordinates.
- **Safety Status:** "All satellites at safe distances" confirmed via automated logs.
- **Model Synergy:** Combined YOLOv8 damage detection with orbital pathing to create a comprehensive satellite health monitoring system.
