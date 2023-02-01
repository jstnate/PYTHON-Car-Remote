import network
import urequests
import utime
import ujson

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'Ouioui'
password = 'pwdman02'
wlan.connect(ssid, password)
url = "http://192.168.154.133:3000/"

while True:
    try:
        r = urequests.get(url)
    except Exception as e:
        print(e) 