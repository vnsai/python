import socket
import time
import os

__author__ = 'G.V.N SAI'

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def chat():
	print(s.recv(1024).decode("utf-8"))
	print('')
	data = "SAI $-> "+input("Me $->")
	s.send(bytes(data,encoding="utf-8"))
	print("")

while True:
	try:
		s.connect(("127.0.0.1",12345))
		print("Connected Successfully!!!")
		print("")
		s.send(bytes("SAI is Active",encoding="utf-8"))
		while True:
			chat()
		break
	except ConnectionRefusedError:
		print("Server is Down.Trying to connect.")
		time.sleep(0.5)
		os.system("clear")
		print("Server is Down.Trying to connect..")
		time.sleep(0.5)
		os.system("clear")
		print("Server is Down.Trying to connect...")
		time.sleep(0.5)
		os.system("clear")
