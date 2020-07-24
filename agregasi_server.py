import socket

listensocket = socket.socket()
port=8081
ip =''
listensocket.bind(('',port))
listensocket.listen(5)
clientsocket, client_address = listensocket.accept()
print("Notifications for user complete")
run = s.recv(1024).decode()
print(run)
clientsocket.close()
	
