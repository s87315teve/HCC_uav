#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading 
import socket
import sys
import time


host = ''
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
tello_address1 = ('192.168.2.5', 8889)
tello_address2 = ('192.168.2.6', 8889)
#sock.bind(locaddr)
message1=["command", "takeoff",  "forward 200", "land"]
message2=["command", "takeoff",  "forward 200", "land"]
delay=[3,8,8,2]

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print("{} : {}".format(server,data.decode(encoding="utf-8")))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


for i in range(0,len(message1)):
    msg1=message1[i]
    msg2=message2[i]
    sock.sendto(msg1.encode("utf-8"), tello_address1)
    sock.sendto(msg2.encode("utf-8"), tello_address2)
    time.sleep(delay[i])
"""
while True: 

    try:
        msg = input("");

        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Send data
        # you have to send "command" first
        msg = msg.encode(encoding="utf-8") 
        sock.sendto(msg, tello_address1)
        sock.sendto(msg, tello_address2)

    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break

"""

