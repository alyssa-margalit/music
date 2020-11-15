from threading import Thread
import time
import sys
import grovepi
from grovepi import *
import math
import pygame
from pygame.locals import *
import os

global queue
queue = "S1.mp3"
os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("S1.mp3")
queue = "S1.mp3"
pygame.mixer.music.set_volume(15)

ranger = 4

#GPIO.setmode(GPIO.BCM)
#PIR_PIN = 18
#GPIO.setup(PIR_PIN, GPIO.IN)
#LED_PIN = 17
#GPIO.setup(LED_PIN, GPIO.OUT)


#global busy
busy = 0

def musicOff():
    print("music playing")
    time.sleep(.5)
    print("music off")
    global busy
    busy = 0
    #print(busy)
    pygame.mixer.music.stop()
    
try:
	while True:
		distance = ultrasonicRead(ranger)
		#print(distance)
		#print(busy)
		if busy ==0:
			if 0<distance<10:
				pygame.mixer.music.load("S1.mp3")
				print("Motion Detected!")
				t = Thread(target=musicOff) # Create thread
				t.start() # Start thread
				pygame.mixer.music.play()
				busy = 1
			elif 10<distance<20:
				pygame.mixer.music.load("S2.mp3")
				print("Motion Detected!")
				t = Thread(target=musicOff) # Create thread
				t.start() # Start thread
				pygame.mixer.music.play()
				busy = 1

		time.sleep(.3)
except KeyboardInterrupt:
	print("interupt")