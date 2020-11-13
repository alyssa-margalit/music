import time
import sys
import grovepi
from grovepi import *
import math
import pygame

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
		delay = 2
	time.sleep(delay)
	