# 🕒 Mickey's Clock

## 📌 Description
This project is a Pygame-based clock application that displays real system time using Mickey Mouse-style clock hands.

## 🎯 Features
- Displays current system time (minutes and seconds)
- Right hand represents minutes
- Left hand represents seconds
- Real-time updates every second
- Rotating clock hands using images

## 🧠 How it works
- The system time is fetched using Python's `datetime`
- Angles are calculated based on minutes and seconds
- `pygame.transform.rotate()` is used to rotate the hands
- The screen updates every second

## 🛠 Technologies
- Python
- Pygame

## ▶️ How to run
```bash
pip install pygame
python main.py