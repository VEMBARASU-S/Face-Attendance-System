import cv2
import os

cam = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)
face_id = 3
count=0

if not os.path.exists("dataset"):
    os.makedirs("dataset")

while True:

    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        1.3,
        5
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(
            img,
            (x, y),
            (x+w, y+h),
            (255, 0, 0),
            2
        )

        count += 1

        cv2.imwrite(
            f"dataset/User.{face_id}.{count}.jpg",
            gray[y:y+h, x:x+w]
        )

        cv2.imshow("Capture Face", img)

    if cv2.waitKey(100) & 0xff == 27:
        break

    elif count >= 50:
        break

cam.release()
cv2.destroyAllWindows()

print("50 Images Captured Successfully")