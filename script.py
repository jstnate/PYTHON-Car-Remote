import network
import urequests
import ujson
import RPi.GPIO as GPIO 
from time import sleep

GPIO.setmode(GPIO.BCM)
#Pins 18 22 24 GPIO 24 25 8
Motor1E = 24 #  Enable pin 1 of the controller IC
Motor1A = 25 #  Input 1 of the controller IC
Motor1B = 8 #  Input 2 of the controller IC


GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

forward=GPIO.PWM(Motor1A,100) # configuring Enable pin for PWM
reverse=GPIO.PWM(Motor1B,100) # configuring Enable pin for PWM



wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'Ouioui'
password = 'pwdman02'
wlan.connect(ssid, password)
url = "http://192.168.154.133:3000/"

while True:
    try:
        r = urequests.get(url)
        data = r.json()["direction"]
        if data == 'backward':
                forward.start(0) 
                reverse.start(0)
                print('en arrière ! ')
                # this will run your motor in reverse direction for 2 seconds with 80% speed by supplying 80% of the battery voltage
                GPIO.output(Motor1E,GPIO.HIGH)
                forward.ChangeDutyCycle(0)
                reverse.ChangeDutyCycle(80)
                sleep(2)
        elif data == 'forward':
            # this will run your motor in forward direction for 5 seconds with 50% speed.
            print ('En avant !')
            GPIO.output(Motor1E,GPIO.HIGH)
            forward.ChangeDutyCycle(50)
            reverse.ChangeDutyCycle(0)
            sleep(5)
        elif data == 'stop':
            #stop motor
            print('STOP MAN')
            GPIO.output(Motor1E,GPIO.LOW)
            forward.stop() # stop PWM from GPIO output it is necessary
            reverse.stop() 
            GPIO.cleanup()
    except Exception as e:
        print(e) 

