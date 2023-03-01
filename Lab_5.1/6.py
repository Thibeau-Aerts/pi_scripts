import wiringpi
import time

pin = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin,1)

def blink(tijd):
    for m in range(3):
        wiringpi.digitalWrite(pin, 1)
        time.sleep(tijd)
        wiringpi.digitalWrite(pin, 0)
        time.sleep(tijd)

i = 0
while (i == 0):
    blink(0.5)
    blink(1.5)
    blink(0.5)