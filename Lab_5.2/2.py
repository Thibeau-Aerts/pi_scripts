import wiringpi
import time

pin1 = 1
pin2 = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin1,1)
wiringpi.pinMode(pin2,0)


i = 0
while (i == 0):
    if wiringpi.digitalRead(pin2) == 0:
        wiringpi.digitalWrite(pin1, 1)
        time.sleep(0.1)
        wiringpi.digitalWrite(pin1, 0)
        time.sleep(0.1)
        print("led blinks")
    else:
        print("LED not flashing")
        time.sleep(0.2)