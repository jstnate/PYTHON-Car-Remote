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
        data = r.json()["direction"]

        if data == 'forward':
            print('en avant') 
            speed.duty_u16(60000)
            speed2.duty_u16(60000)
            IN1.low()
            IN2.high()
            IN4.low()
            IN3.high()
        elif data == 'backward':
            print('en arrière')    
            speed.duty_u16(20000)
            speed2.duty_u16(20000)
            IN1.high()
            IN2.low()
            IN4.high()
            IN3.low()

            sleep(5)
        elif data == 'right':
            print('à droite')
            speed.duty_u16(20000)
            speed2.duty_u16(20000)
            IN1.high()
            IN2.low()
            IN4.low()
            IN3.low()
        elif data == 'left':
            print('à gauche')
            speed.duty_u16(20000)
            speed2.duty_u16(20000)
            IN1.low()
            IN2.low()
            IN4.high()
            IN3.low()    
        elif data == 'stop':
            print('stop')
            IN1.low()
            IN2.low()
            IN4.low()
            IN3.low()

        print(data)
        r.close()
        utime.sleep(1)

    except Exception as e:
        print(e) 


