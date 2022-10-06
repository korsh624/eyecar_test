import cv2 as cv
cv2 = cv
import numpy as np
import time
import os
import pigpio
os.system("sudo pigpiod")  # Launching GPIO library
time.sleep(1)

ESC = 17 # драйвер двигателя, смотри на номера после GPIO
STEER = 18 # сервопривод
pi = pigpio.pi()
time.sleep(1)
pi = pigpio.pi()
time.sleep(1)
pi.set_servo_pulsewidth(ESC, 0)
pi.set_servo_pulsewidth(STEER, 0)
time.sleep(2)
print("podau signal")
h=0
while (h<10):
    pi.set_servo_pulsewidth(ESC, 1555)
    h=h+1
    time.sleep(1)
