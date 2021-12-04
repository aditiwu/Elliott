import bluetooth
from time import *
port = 1
sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect(('98:D3:31:FC:3B:3E', port))
with open("value.txt") as asdfg:
    qwerty = asdfg.readlines()
readline = (qwerty[0])
print ("Left: "+readline)
sleep(1.5)
sock.send("LightsOff")

