from grovepi import *
import time

ranger = 4

while True:
	distance = ultrasonicRead(ranger)
	print(distance)
	time.sleep(1)
