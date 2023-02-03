
import network
import urequests
import ujson
import utime
from time import sleep
import _thread
from machine import Pin, PWM


IN1 = Pin(3, Pin.OUT)
IN2 = Pin(2, Pin.OUT)

IN3 = Pin(19, Pin.OUT)
IN4 = Pin(18, Pin.OUT)

speed = PWM(Pin(4))
speed2 = PWM(Pin(20))
speed2.freq(1000)
speed.freq(1000)

BlueLed = Pin(12, mode=Pin.OUT)
WhiteLed = Pin(11, mode=Pin.OUT)
RedLed = Pin(10, mode=Pin.OUT)

buzzer = PWM(Pin(9))
buzzer.freq(740)

Fsharp = 740
C = 523




wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'Ouioui'
password = 'pwdman02'
wlan.connect(ssid, password)
url = "http://192.168.154.133:3000/"
while not wlan.isconnected():
    print("no co")
    sleep(1)



def buzzer_function():
    
    for cycle in range(30000):
        buzzer.freq(Fsharp)
        buzzer.duty_u16(cycle)
        buzzer.duty_u16(0)
    for cycle in range(30000):
        buzzer.freq(C)
        buzzer.duty_u16(30000 - cycle)


while True:
    try:
        r = urequests.get(url)
        direction = r.json()["direction"]
        girophares = r.json()["giro"]
        

        if girophares == 'on':

            _thread.start_new_thread(buzzer_function, ())

            BlueLed.on()
            utime.sleep(0.2)
            BlueLed.off()

            WhiteLed.on()
            utime.sleep(0.2)
            WhiteLed.off()

            RedLed.on()
            utime.sleep(0.2)
            RedLed.off()


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
            buzzer.duty_u16(0)

        print(direction)
        r.close()

    except Exception as h:
        print(h)