# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
message = 'hello'
b = bytes(message, encoding='utf-8')
sock.send(b)

data = sock.recv(1024)
sock.close()

print(data)