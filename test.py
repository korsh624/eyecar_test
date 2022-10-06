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
pi.set_servo_pulsewidth(ESC, 1500)
time.sleep(2)
h=90
while (h!=0):
    pi.set_servo_pulsewidth(ESC, 1555)
    pi.set_servo_pulsewidth(STEER, int(16.66666 * h))
    print(h)
    time.sleep(1)
pi.set_servo_pulsewidth(ESC, 0)
os.system("sudo killall pigpiod")  # Launching GPIO library