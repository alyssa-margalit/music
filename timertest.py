from threading import Timer
from time import sleep

def hello():
    print ("hello, world")
    t = Timer(4,hello)
    t.start()

t = Timer(4, hello)
t.start() # after 3 seconds, "hello, world" will be printed

# timer will wake up ever 3 seconds, while we do something else
while True:
    print ("do something else")
    distance1 = ultrasonicRead(ranger)
    print(distance1)

    sleep(2)