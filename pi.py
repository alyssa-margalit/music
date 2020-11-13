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
print(distance)
slide = analogRead(pot)
print(slide)
pygame.mixer.init()
pygame.mixer.music.load("bass.mp3")
pygame.mixer.music.set_volume(15)
#pygame.mixer.music.play()
#while pygame.mixer.music.get_busy() == True:
	#pass
while True:
	
	distance = ultrasonicRead(ranger)
	print(distance)
	slide = analogRead(pot)
	print(slide)
	if 0<distance<3:
		pygame.mixer.music.load("bass.mp3")
		pygame.mixer.music.play()
		time.sleep(delay)
	elif 3<distance<6:
		pygame.mixer.music.load("Drum3.mp3")
		pygame.mixer.music.play()
		time.sleep(delay)
	elif 6<distance<9:
		pygame.mixer.music.load("drum_stick.mp3")
		pygame.mixer.music.play()
		time.sleep(delay)
	elif 9<distance<12:
		pygame.mixer.music.load("meow.mp3")
		pygame.mixer.music.play()
		time.sleep(delay)
	elif 12<distance<15:
		pygame.mixer.music.load("Sfx1.mp3")
		pygame.mixer.music.play()
		time.sleep(delay)
	elif 12<distance<15:
		pygame.mixer.music.load("Sfx2.mp3")
		pygame.mixer.music.play()
		time.sleep(delay)
	elif 15<distance<18:
		pygame.mixer.music.load("Sfx3.mp3")
		pygame.mixer.music.play()
		time.sleep(delay)
	elif 18<distance<21:
		pygame.mixer.music.load("Sfx5.mp3")
		pygame.mixer.music.play()
		time.sleep(delay)
	elif 21<distance<24:
		pygame.mixer.music.load("Sfx6.mp3")
		pygame.mixer.music.play()
		time.sleep(delay)
	elif 24<distance<27:
		pygame.mixer.music.load("Sfx7.mp3")
		pygame.mixer.music.play()
		time.sleep(delay)
	elif 27<distance<30:
		pygame.mixer.music.load("Sfx8.mp3")
		pygame.mixer.music.play()
		time.sleep(delay)
	elif 27<distance<30:
		pygame.mixer.music.load("snare.mp3")
		pygame.mixer.music.play()
		time.sleep(delay)
	else:
		time.sleep(delay)

	if 0<slide<20:
		delay = 1
	elif 20<slide<500:
		delay = .7
	else:
		delay = .5
	
	