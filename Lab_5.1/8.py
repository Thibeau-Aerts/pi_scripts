import wiringpi
import time

pin1 = 2
pin2 = 3
pin3 = 4
pin4 = 5

wiringpi.wiringPiSetup()
wiringpi.pinMode(pin1,2)
wiringpi.pinMode(pin2,2)
wiringpi.pinMode(pin3,2)
wiringpi.pinMode(pin4,2)

def blink(percentage):
    a = 1024/100*100
    print(a)
    wiringpi.pwmWrite(pin1, 1)
    wiringpi.pwmWrite(pin2, 1)
    wiringpi.pwmWrite(pin3, 1)
    wiringpi.pwmWrite(pin4, 1)

i = 0
while (i == 0):
    blink(0)
    time.sleep(2)
    blink(25)
    time.sleep(2)
    blink(25)
    time.sleep(2)
    blink(25)
    time.sleep(2)