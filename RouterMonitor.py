import os, time
#import RPi.GPIO as GPIO

gpioPin = 17

hostname = "1.1.1.1"
pingRetryTime=1
offTime=30
upstartTime=60


check = 1
secondTry = 2
stop = 3
start = 4

state = check

v = [state,0]

#GPIO.setup(gpioPin,GPIO.OUT)


def ping():
    print "ping" , hostname 
    response = os.system("ping -c 1  -w2 "  + hostname +" > /dev/null 2>&1")  
    return response == 0

def shutdown():
    print "shutdown"
 #   GPIO.output(gpioPin, True) 
    

def startup():
    print "startup"
  #  GPIO.output(gpioPin, False) 
    


def monitor(state):
    if state == check:
        if ping():
            return [check,pingRetryTime]
        else:
            return [secondTry,pingRetryTime]
    elif state == secondTry:
        if ping():
            return [check,pingRetryTime]
        else:
            return [stop,0]
    elif state == stop:
        shutdown()
        return [start,offTime]
    elif state == start:
        startup()
        return [check,upstartTime]
while True:
    v=monitor(v[0])
    time.sleep( v[1] )