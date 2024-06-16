import cv2
import numpy as np
import subprocess
import time

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def sleep_computer():
    script = 'tell application "System Events" to sleep'
    subprocess.run(["osascript", "-e", script])


def capture_owner_face():
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            owner_face = gray[y : y + h, x : x + w]
            cv2.imwrite("owner_face.jpg", owner_face)
            print("Owner's face captured!")
            break
        else:
            print("No face detected! Trying again...")

    video_capture.release()


def detect_face():
    video_capture = cv2.VideoCapture(0)
    last_seen = time.time()
    owner_face = cv2.imread("owner_face.jpg", cv2.IMREAD_GRAYSCALE)

    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            current_face = cv2.resize(
                gray[y : y + h, x : x + w], (owner_face.shape[1], owner_face.shape[0])
            )
            diff = cv2.absdiff(current_face, owner_face)
            if np.mean(diff) < 50:
                print("Owner's face detected!")
                last_seen = time.time()
            else:
                print("Different face detected!")
                if time.time() - last_seen > 5:
                    sleep_computer()
                    break
        else:
            print("No face detected!")
            if time.time() - last_seen > 5:
                sleep_computer()
                break

        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()


def main():
    try:
        owner_face = cv2.imread("owner_face.jpg", cv2.IMREAD_GRAYSCALE)
        if owner_face is None:
            print("No owner face image found.")
            answer = input("Do you want to capture owner's face now? (y/n): ")
            if answer.lower() == "y":
                capture_owner_face()
            else:
                return
        detect_face()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
