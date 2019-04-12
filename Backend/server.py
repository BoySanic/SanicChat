#! /usr/bin/python3
import socket
import json

print("SanicChat Server starting...");
TCP_IP = '127.0.0.1'
TCP_PORT = 3001
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))	
s.listen(1)
while 1:
	conn, addr = s.accept()
	print("Connection Address: %s", addr)
	data = conn.recv(BUFFER_SIZE)
	if not data: continue
	print("Received data: ", data.decode())
	j = json.loads(data.decode())
	print(j["username"])
	conn.close()