# Face Attendance System

## Project Overview
Face Attendance System is a Python-based application that automatically marks attendance using face recognition technology. The system captures facial images, trains a recognition model, identifies registered users, and stores attendance records in a CSV file.

## Features
- Face Detection using Haar Cascade Classifier
- Face Recognition using LBPH Algorithm
- Automatic Attendance Marking
- Attendance Stored in CSV File
- Unknown Face Detection
- Real-Time Camera Recognition

## Technologies Used
- Python
- OpenCV
- NumPy
- CSV
- Haar Cascade
- LBPH Face Recognizer

## Project Structure

```
Face_Attendance/
│
├── dataset/
├── trainer/
│   └── trainer.yml
├── capture.py
├── trainer.py
├── main.py
├── attendance.csv
└── README.md
```

## How to Run

### 1. Capture Face Images
```bash
python capture.py
```

### 2. Train the Model
```bash
python trainer.py
```

### 3. Start Attendance System
```bash
python main.py
```

## Output
- Registered users are recognized automatically.
- Attendance is saved in `attendance.csv`.
- Unknown users are detected and rejected.

## Author
**Vembarasu S**  
Electronics and Communication Engineering (ECE)

## GitHub Repository
Face Attendance System Project
