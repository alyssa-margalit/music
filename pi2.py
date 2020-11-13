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
pygame.mixer.music.set_volume(15)
#pygame.mixer.music.play()
#while pygame.mixer.music.get_busy() == True:
	#pass
while True:
	
	distance1 = ultrasonicRead(ranger)
	time.sleep(.1)
	distance2 = ultrasonicRead(ranger)
	distance = (distance1+distance2)/2
	#print(distance)
	slide = analogRead(pot)
	#print(slide)
	if 0<distance<3:
		pygame.mixer.music.queue("S1.mp3")
		pygame.mixer.music.play()
		#pygame.mixer.music.unload("S1.mp3")
		print("1")
		#time.sleep(delay)

	elif 3<distance<6:
		pygame.mixer.music.queue("S2.mp3")
		pygame.mixer.music.play()
		print("2")
		#time.sleep(delay)
	elif 6<distance<9:
		pygame.mixer.music.queue("S3.mp3")
		pygame.mixer.music.play()
		print("3")
		#time.sleep(delay)
	elif 9<distance<12:
		pygame.mixer.music.queue("S4.mp3")
		pygame.mixer.music.play()
		print("4")
		#time.sleep(delay)
	elif 12<distance<15:
		pygame.mixer.music.queue("S5.mp3")
		pygame.mixer.music.play()
		print("5")
		#time.sleep(delay)
	elif 12<distance<15:
		pygame.mixer.music.queue("S6.mp3")
		pygame.mixer.music.play()
		print("6")
		#time.sleep(delay)
	elif 15<distance<18:
		pygame.mixer.music.queue("S7.mp3")
		pygame.mixer.music.play()
		print("7")
		#time.sleep(delay)
	elif 18<distance<21:
		pygame.mixer.music.queue("S8.mp3")
		pygame.mixer.music.play()
		print("8")
		#time.sleep(delay)
	#else:
	pygame.mixer.music.load(queue[0])
	pygame.mixer.music.play()
		#pygame.mixer.music.play()
	#while pygame.mixer.music.get_busy() == True:
		#pass
	#pygame.mixer.music.stop()
	time.sleep(.1)

	