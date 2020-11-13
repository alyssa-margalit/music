import time
import sys
import grovepi
from grovepi import *
import math
import pygame
from pygame.locals import *
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()

pygame.mixer.init()


ranger = 4
pot = 2
delay = 1
distance = ultrasonicRead(ranger)
#print(distance)
slide = analogRead(pot)
#print(slide)
pygame.mixer.init()
pygame.mixer.music.load("S1.mp3")
queue = "S1.mp3"
pygame.mixer.music.set_volume(15)
#pygame.mixer.music.play()
#while pygame.mixer.music.get_busy() == True:
	#pass
global queue 
queue = "S1.mp3"

def newBeat(distance):

	if 0<distance<3:
		queue = "S1.mp3"
		print("1")

	elif 3<distance<6:
		queue = "S2.mp3"
		print("2")

	elif 6<distance<9:
		queue = "S3.mp3"
		print("3")
	elif 9<distance<12:
		queue = "S4.mp3"
		print("4")
	elif 12<distance<15:
		queue = "S5.mp3"
		print("5")
	elif 12<distance<15:
		queue = "S6.mp3"
		print("6")
	elif 15<distance<18:
		queue = "S7.mp3"
		print("7")
	elif 18<distance<21:
		queue = "S8.mp3"
		print("8")
	else:
		print("101")


while True:
	
	distance1 = ultrasonicRead(ranger)
	time.sleep(.1)
	distance2 = ultrasonicRead(ranger)
	distance = (distance1+distance2)/2
	slide = analogRead(pot)

	pygame.mixer.music.play()
	while True:
		if pygame.mixer.music.get_busy():
			print("busy")
			pass
		else:
			newBeat(distance)
			pygame.mixer.music.load(queue)
			break
		#pygame.mixer.music.play()
	#while pygame.mixer.music.get_busy() == True:
		#pass
	#pygame.mixer.music.stop()
	time.sleep(.2)

	