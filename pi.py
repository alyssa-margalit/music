import time
import sys
import grovepi
from grovepi import *
import math
import pygame
from pygame.locals import *

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
pygame.mixer.music.set_volume(3)
#pygame.mixer.music.play()
#while pygame.mixer.music.get_busy() == True:
	#pass
while True:
	
	distance = ultrasonicRead(ranger)
	print(distance)
	slide = analogRead(pot)
	print(slide)
	if 10<distance<15:
		pygame.mixer.music.play()
	if 0<slide<20:
		delay = 2
	elif 20<slide<500:
		delay = .5
	else:
		delay = 1
	time.sleep(delay)
	