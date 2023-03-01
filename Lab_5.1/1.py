import wiringpi
import time

pin = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin,1)


i = 0
while (i == 0):
    wiringpi.digitalWrite(pin, 1)
    time.sleep(0.1)
    wiringpi.digitalWrite(pin, 0)
    time.sleep(0.1)