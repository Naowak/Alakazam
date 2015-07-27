import socket
from classServer import *

IP = ""
PORT = 10000

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((IP,PORT))

WaitingList = ListThread()
WaitingList.start()


while True:
	tcpsock.listen(10)
	print( "En écoute...")
	(clientsocket, (ip, port)) = tcpsock.accept()
	newthread = ClientThread(ip, port, clientsocket, WaitingList)
	newthread.start()

