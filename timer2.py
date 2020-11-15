from threading import Timer
from time import sleep
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
pygame.mixer.music.load("S1.mp3")
pygame.mixer.music.set_volume(15)


def hello():
    print ("hello, world")
    pygame.mixer.music.play()
    t = Timer(2,hello)
    t.start()

t = Timer(2, hello)
t.start() # after 3 seconds, "hello, world" will be printed

# timer will wake up ever 3 seconds, while we do something else
while True:
	print ("do something else")
	distance = ultrasonicRead(ranger)
	print(distance)
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
	pygame.mixer.music.load(queue)
    sleep(1)