import socket
import os

__author__ = 'G.V.N SAI'

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
os.system("clear")
s.bind(("127.0.0.1",12345))

print("Waiting For client....")
s.listen()
client,addrs=s.accept()
os.system("clear")
print("Connected With",addrs)
print('')
client.send(bytes("G.V.N is Active",encoding="utf-8"))
print(client.recv(1024).decode("utf-8"))
print("")

while True:
	print(client.recv(1024).decode("utf-8"))
	print("")
	data="G.V.N #-> "+input("Me #->")
	client.send(bytes(data,encoding="utf-8"))
	print("")
