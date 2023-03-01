import wiringpi
import time

pin1 = 2
pin2 = 3
pin3 = 4
pin4 = 5

wiringpi.wiringPiSetup()
wiringpi.pinMode(pin1,1)
wiringpi.pinMode(pin2,1)
wiringpi.pinMode(pin3,1)
wiringpi.pinMode(pin4,1)


i = 0
while (i == 0):
    wiringpi.digitalWrite(pin1, 1)
    wiringpi.digitalWrite(pin2, 1)
    wiringpi.digitalWrite(pin3, 1)
    wiringpi.digitalWrite(pin4, 1)
    time.sleep(0.1)
    wiringpi.digitalWrite(pin1, 0)
    wiringpi.digitalWrite(pin2, 0)
    wiringpi.digitalWrite(pin3, 0)
    wiringpi.digitalWrite(pin4, 0)
    time.sleep(0.1)