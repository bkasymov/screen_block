# Face Detection and Computer Sleep System

This project provides a Python script to detect the owner's face using a webcam and put the computer to sleep if a different face is detected or if no face is detected for more than 5 seconds. The script uses OpenCV for face detection and the AppleScript command for sleeping the computer on macOS.

## Prerequisites

- Python 3.x
- OpenCV
- NumPy

## Installation

1. Install the required Python packages:

    ```sh
    pip install opencv-python-headless numpy
    ```

2. Ensure you have a webcam connected to your computer.

## Usage

### 1. Capture Owner's Face

Before starting the face detection, you need to capture the owner's face. This can be done by running the script and following the prompt:

    ```sh
    python script.py
    ```

When prompted:

    ```sh
    No owner face image found.
    Do you want to capture owner's face now? (y/n):
    ```

Type `y` and press Enter. Ensure your face is clearly visible to the webcam.

### 2. Start Face Detection

After capturing the owner's face, the script will automatically start the face detection process. If the owner's face is detected, the system remains active. If a different face or no face is detected for more than 5 seconds, the computer will go to sleep.

### 3. Running the Script

To run the script:

    ```sh
    python script.py
    ```

## Code Explanation

### `face_cascade`

This variable loads the pre-trained face detection model provided by OpenCV.

### `sleep_computer()`

This function uses `osascript` to run an AppleScript command to put the computer to sleep.

### `capture_owner_face()`

This function captures the owner's face using the webcam, saves it as `owner_face.jpg`, and indicates when the face is successfully captured.

### `detect_face()`

This function continuously captures frames from the webcam, detects faces, and compares them to the saved owner's face. If a different face is detected or no face is detected for more than 5 seconds, the computer is put to sleep.

### `main()`

The main function initializes the process by checking if the owner's face image exists. If not, it prompts the user to capture the face. Then it starts the face detection process.

## Notes

- This script is designed for macOS because it uses AppleScript to put the computer to sleep. For other operating systems, you need to modify the `sleep_computer()` function accordingly.
- Ensure that the lighting conditions are consistent when capturing the owner's face and during face detection for optimal performance.

## License

This project is licensed under the MIT License.

---

For any issues or contributions, feel free to open an issue or submit a pull request on the GitHub repository.
