import serial
import time


def py_ino():
    p=serial.Serial("COM5",9600)
    def conv(s):
        l1=[]
        print(s)
        for i in s:
            l1.append(ord(i))
            print(l1)
        return l1

    i=5
    while (i<=6):
        data=conv('O')
        print(data)
        p.write(bytes(data))
        print('UNLOCKED..!!!')
        time.sleep(2)
        i+=1
        
#py_ino()
