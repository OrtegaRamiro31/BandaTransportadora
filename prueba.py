import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

MotorIN1 = 3
MotorIN2 = 2
MotorE1 = 21

GPIO.setup(MotorIN1,GPIO.OUT)
GPIO.setup(MotorIN2,GPIO.OUT)
GPIO.setup(MotorE1,GPIO.OUT)

def avanzar():
    GPIO.output(MotorIN1,GPIO.HIGH) 
    GPIO.output(MotorIN2,GPIO.LOW)  
    GPIO.output(MotorE1,GPIO.HIGH)  

def retroceder():
    GPIO.output(MotorIN1,GPIO.LOW) 
    GPIO.output(MotorIN2,GPIO.HIGH)  
    GPIO.output(MotorE1,GPIO.HIGH)  

if __name__ == 'main':
    while True:
        avanzar()
        sleep(5)
        retroceder()
        sleep(5)