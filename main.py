import cv2
import csv
from datetime import datetime

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")

faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

names = {
    1: "Vembarasu",
    2: "Kumaraguru",
    3: "Yokesh",
}

cam = cv2.VideoCapture(0)

while True:

    ret, img = cam.read()

    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        if w < 120 or h < 120:
            continue

        id, confidence = recognizer.predict(
            gray[y:y+h, x:x+w]
        )

        print( "Confidence:", confidence)

        if confidence < 35 :
            name = names.get(id, "Unknown")
            print(f"{name} Attendance Marked")
            now = datetime.now()

            with open(
                        "attendance.csv",
                        "a",
                        newline=""
                    ) as f:

                        writer = csv.writer(f)

                        writer.writerow([
                            name,
                            now.strftime("%Y-%m-%d"),
                            now.strftime("%H:%M:%S")
                        ])
                        print("CSV Saved Successfully")

            cam.release()
            cv2.destroyAllWindows()
            exit()
        else:
            print("unknown face detected")
            cv2.putText(
                        img,
                        "Unknown",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),
                        2
                    )

        cv2.rectangle( 
             img,
               (x, y), 
               (x + w, y + h),
                 (255, 0, 0),
                   2
                     )

        cv2.imshow(
            "Face Attendance System",
            img
        )

        cv2.waitKey(2000)  

        cam.release()
        cv2.destroyAllWindows()
        break