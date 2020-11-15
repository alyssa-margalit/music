from threading import Thread
import time
import sys
import grovepi
from grovepi import *
import math
import pygame
from pygame.locals import *
import os

#GPIO.setmode(GPIO.BCM)
#PIR_PIN = 18
#GPIO.setup(PIR_PIN, GPIO.IN)
#LED_PIN = 17
#GPIO.setup(LED_PIN, GPIO.OUT)
def musicOff():
    #GPIO.output(LED_PIN, GPIO.input(PIR_PIN))
    print("music playing")
    time.sleep(2)
    print("music off")
    #GPIO.output(LED_PIN, False)
try:
	while True:
		distance = ultrasonicRead(ranger)
		print(distance)
		if 0<distance<20:
			print("Motion Detected!")
			t = Thread(target=musicOff) # Create thread
			t.start() # Start thread
		time.sleep(4)
except KeyboardInterrupt:
	print("interupt")