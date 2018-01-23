#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5002
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "data from client :", data
    num=int(data)
    factorial = 1
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,num + 1):
           factorial = factorial*i
       print('The factorial of',num,'is',factorial,' and send back to client')

    conn.send(str(factorial))  # echo
conn.close()
