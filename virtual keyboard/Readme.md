# ✋ Virtual Keyboard using OpenCV, MediaPipe, and Hand Gestures

This project implements a **gesture-controlled virtual keyboard** using Python, OpenCV, and MediaPipe.
The user can type by moving their hand in front of a webcam and selecting keys through finger distance and position.

## 📌 Features

* Real-time hand tracking using **MediaPipe**.
* On-screen keyboard displayed using **OpenCV**.
* Key selection by pinching with index and middle fingers.
* Supports:
  * Uppercase and lowercase layouts (switch via `APR` key).
  * Space (`SP`), Clear Last Character (`CL`), and Layout Toggle (`APR`).
* Simulates keystrokes on your system using **pynput**.

## 🛠️ Requirements
* Python 3.x
* OpenCV (`cv2`)
* MediaPipe
* NumPy
* pynput

### Install Dependencies

Use the following command to install required libraries:

```bash
pip install opencv-python mediapipe numpy pynput
```

---

## ▶️ How to Run

1. Make sure your webcam is connected.
2. Run the script:

```bash
python virtualKeyboard.py
```

3. A virtual keyboard window will appear.
4. Use your hand to move the cursor (index finger tip).
5. Tap a key by pinching (bringing index and middle fingers together).
6. Press `q` to quit.

---

## 🧠 How It Works

* **MediaPipe Hands** detects 21 landmarks of the hand.
* Uses landmark 8 (index fingertip) to determine cursor position.
* Detects a "pinch" by measuring distance between landmark 8 (index) and 12 (middle).
* Calculates the distance between landmarks 5 and 17 to determine if the hand is open (to prevent accidental clicks).
* Keyboard is drawn using rectangles with `cv2`.
* Simulated key presses are sent using the `pynput` library.

---

## 🎮 Special Keys

| Key | Function                           |
| --- | ---------------------------------- |
| CL  | Clear last character (Backspace)   |
| SP  | Add a space                        |
| APR | Toggle between uppercase/lowercase |

## 📃 License

This project is open-source and free to use for educational purposes.
**
