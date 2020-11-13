import time
import sys
import grovepi
from grovepi import *
import math
import pygame

pygame.mixer.init()
pygame.mixer.music.load("bass-drum.mp3")

ranger = 4
pot = 2
delay = 1
distance = ultrasonicRead(ranger)
print(distance)
slide = analogRead(pot)
print(slide)
while True:
	pygame.mixer.music.play()
	distance = ultrasonicRead(ranger)
	print(distance)
	slide = analogRead(pot)
	print(slide)
	if distance == 10:
		delay = 2
	time.sleep(delay)
	