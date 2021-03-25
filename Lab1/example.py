# coding=utf-8
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#

import threading 
import socket
import sys
import time

#Tello EDU 的IP和port，所有控制命令將發送到此位置
tello_address = ('192.168.10.1', 8889)

#本機監聽port地址，將會從這邊收到來自無人機的response
host = ''
port = 9000
locaddr = (host,port) 

#建立udp socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(locaddr)


def recv():
    while True: 
        try:
            #監聽此socket，當收到資料的時候就會執行 data, server = sock.recvfrom(1518)
            #data為本機收到的資料，資料須先用utf-8解碼後才會變成字串
            #server為無人機的IP
            data, server = sock.recvfrom(1518)
            print("{} : {}".format(server, data.decode(encoding="utf-8")))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#建立thread在背景執行，讓電腦可以收到無人機的response
recvThread = threading.Thread(target=recv)
recvThread.start()

#進入無限迴圈，讓你可以用鍵盤輸入控制命令
while True: 

    try:
        msg = input("");

        if not msg:
            continue  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Send data
        # you have to send "command" first
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
        time.sleep(0.1)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break




