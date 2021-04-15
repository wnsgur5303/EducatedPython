import serial
import string

port = 'COM3'
brate = 115200 #boudrate
cmd = 'temp'

seri = serial.Serial(port, baudrate = brate, timeout = None)
print(seri.name)

seri.write(cmd.encode())


while True:
    if seri.in_waiting != 0 :
        content1 = seri.readline()
        content2 = content1[:-2].decode().split('/')
        print(content1[:-2].decode())
        print(content2[1])

        
