# Self-Driving Car Project

Hello there, this project is now in v1.0.0. We have developed the initial idea and made significant progress.

## Project Overview

This project is about a self-driving car that uses a PC and an ESP32CAM mounted on a tiny car. The video from the ESP32CAM is processed on the PC using Python, NumPy, and OpenCV to measure the curve of a path. The curve data is then sent to a MQTT broker, which forwards it to the ESP32CAM. The ESP32CAM uses this curve data to control the car's movement using a PID system.

## Key Files

The main logic of the project is contained in two files:

1. `./src-arduino/src/sketch.cpp` lines 1225 to 1242: This part of the code handles the communication with the MQTT broker and the processing of the curve data.

2. `./src-arduino/src/Motor.cpp` lines 40 to 87: This part of the code controls the movement of the car based on the curve data. It uses a PID system to adjust the car's speed and direction based on the curve of the path. After moving the motors, there is a microsecond delay before returning the curve and turn values.

## Future Updates

We are continuously working on improving this project. Stay tuned for future updates!

## Illustrative Content

<img src="https://github.com/FedericoSebas/CERTERO-Smart-Car/assets/108437899/edb2dc8d-395e-404d-92d9-898de5a04f51" width="250"/>


https://github.com/FedericoSebas/CERTERO-Smart-Car/assets/108437899/04f8dd56-40b6-4fee-bdeb-6901cfbc2fd8

