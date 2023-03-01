import wiringpi
import time

wiringpi.wiringPiSetup()
wiringpi.pinMode(2,1)

for i in range(500):
    wiringpi.digitalWrite(2, 1)
    time.sleep(0.1)
    wiringpi.digitalWrite(2, 0)
    time.sleep(0.1)