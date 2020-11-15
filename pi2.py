from threading import Thread
import time
import sys
import grovepi
from grovepi import *
import math
import pygame
from pygame.locals import *
import os

ranger = 4
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("S1.mp3")
pygame.mixer.music.set_volume(15)
global cycle
cycle = 0.0

class Hello5Program:  
    def __init__(self):
        self._running = True

    def terminate(self):  
        self._running = False  

    def run(self):
        global cycle
        while self._running:
            distance = ultrasonicRead(ranger)
            print(distance)
            time.sleep(.5) #.5 second delay
            cycle = cycle + 1.0
            print ("5 Second Thread cycle+1.0 - "+ str(cycle))

class Hello2Program:  
    def __init__(self):
        self._running = True

    def terminate(self):  
        self._running = False  

    def run(self):
        global cycle
        while self._running:
            pygame.mixer.music.stop()
            print("play sound")
            pygame.mixer.music.play()
            time.sleep(1) #1 second delay
            cycle = cycle + 0.5
            #print ("2 Second Thread cycle+1.0 - "+ str(cycle))
#Create Class
FiveSecond = Hello5Program()
#Create Thread
FiveSecondThread = Thread(target=FiveSecond.run) 
#Start Thread 
FiveSecondThread.start()

#Create Class
TwoSecond = Hello2Program()
#Create Thread
TwoSecondThread = Thread(target=TwoSecond.run) 
#Start Thread 
TwoSecondThread.start()


Exit = False #Exit flag
while Exit==False:
    cycle = cycle + 0.1 
    print ("Main Program increases cycle+0.1 - "+ str(cycle))
    time.sleep(1) #One second delay
    #if (cycle > 5): Exit = True #Exit Program

TwoSecond.terminate()
FiveSecond.terminate()
print ("Goodbye :)")