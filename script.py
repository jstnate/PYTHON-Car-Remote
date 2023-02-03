import network
import urequests
import ujson
import utime
from time import sleep
from machine import Pin, PWM


IN1 = Pin(3, Pin.OUT)
IN2 = Pin(2, Pin.OUT)

IN3 = Pin(19, Pin.OUT)
IN4 = Pin(18, Pin.OUT)

speed = PWM(Pin(4))
speed2 = PWM(Pin(20))
speed2.freq(1000)
speed.freq(1000)

BlueLed = 1
WhiteLed = 2
RedLed = 3




wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'Ouioui'
password = 'pwdman02'
wlan.connect(ssid, password)
url = "http://192.168.154.133:3000/"
while not wlan.isconnected():
    print("no co")
    sleep(1)


while True:
    try:
        r = urequests.get(url)
        direction = r.json()["direction"]
        girophares = r.json()["giro"]

        if girophares == 'on':
            print('LA POLICE')


        if direction == 'forward':
            print('en avant') 
            speed.duty_u16(40000)
            speed2.duty_u16(40000)
            IN1.low()
            IN2.high()
            IN4.low()
            IN3.high()
        elif direction == 'backward':
            print('en arrière')    
            speed.duty_u16(20000)
            speed2.duty_u16(20000)
            IN1.high()
            IN2.low()
            IN4.high()
            IN3.low()

            sleep(5)
        elif direction == 'right':
            print('à droite')
            IN1.low()
            IN2.high()
            IN4.low()
            IN3.high()
            speed.duty_u16(30000)
            speed2.duty_u16(30000)
            IN1.low()
            IN2.high()
            IN4.low()
            IN3.low()
        elif direction == 'left':
            print('à gauche')
            IN1.low()
            IN2.high()
            IN4.low()
            IN3.high()
            speed.duty_u16(30000)
            speed2.duty_u16(30000)
            IN1.low()
            IN2.low()
            IN4.low()
            IN3.high()    
        elif direction == 'stop':
            print('stop')
            IN1.low()
            IN2.low()
            IN4.low()
            IN3.low()

        print(direction)
        r.close()
        utime.sleep(1)

    except Exception as e:
        print('eroor')

