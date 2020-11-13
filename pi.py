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
#pygame.mixer.music.load("bass.mp3")
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
		pygame.mixer.music.load("S1.mp3")
		pygame.mixer.music.play()
		#pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			pass

		pygame.mixer.music.stop()
		#pygame.mixer.music.unload("S1.mp3")
		print("1")
		#time.sleep(delay)

	elif 3<distance<6:
		pygame.mixer.music.load("S2.mp3")
		pygame.mixer.music.play()
		#pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			pass
		pygame.mixer.music.stop()
		#pygame.mixer.music.unload("S2.mp3")
		print("2")
		#time.sleep(delay)
	elif 6<distance<9:
		pygame.mixer.music.load("S3.mp3")
		pygame.mixer.music.play()
		#pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			pass
		pygame.mixer.music.stop()
		#pygame.mixer.music.unload("S3.mp3")
		print("3")
		#time.sleep(delay)
	elif 9<distance<12:
		pygame.mixer.music.load("S4.mp3")
		pygame.mixer.music.play()
		#pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			pass
		pygame.mixer.music.stop()
		#pygame.mixer.music.unload("S4.mp3")
		print("4")
		#time.sleep(delay)
	elif 12<distance<15:
		pygame.mixer.music.load("S5.mp3")
		pygame.mixer.music.play()
		#pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			pass
		pygame.mixer.music.stop()
		#pygame.mixer.music.unload("S5.mp3")
		print("5")
		#time.sleep(delay)
	elif 12<distance<15:
		pygame.mixer.music.load("S6.mp3")
		pygame.mixer.music.play()
		#pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			pass
		pygame.mixer.music.stop()
		#pygame.mixer.music.unload("S7.mp3")
		print("6")
		#time.sleep(delay)
	elif 15<distance<18:
		pygame.mixer.music.load("S7.mp3")
		pygame.mixer.music.play()
		#pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			pass
		pygame.mixer.music.stop()
		#pygame.mixer.music.unload("S7.mp3")
		print("7")
		#time.sleep(delay)
	elif 18<distance<21:
		pygame.mixer.music.load("S8.mp3")
		pygame.mixer.music.play()
		#pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			pass
		pygame.mixer.music.stop()
		#pygame.mixer.music.unload("S8.mp3")
		print("8")
		#time.sleep(delay)
	#else:
	time.sleep(.5)

	if 0<slide<20:
		delay = 1
	elif 20<slide<500:
		delay = .7
	else:
		delay = .5
	
	