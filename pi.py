import time
import sys
import grovepi
from grovepi import *
import math

ranger = 4
pot = 2
delay = 1
distance = ultrasonicRead(ranger)
print(distance)
slide = analogRead(pot)
print(slide)
while True:
	distance = ultrasonicRead(ranger)
	print(distance)
	slide = analogRead(pot)
	print(slide)
	if distance == 10:
		delay = 2
	time.sleep(delay)
	