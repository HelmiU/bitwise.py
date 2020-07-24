import socket
import time
import os
s = socket.socket()
print("masukkan pilihan ")
print("1. beritahu user adanya penyesuaian ip")
print("2. beritahu fog b user siap tersambung")
print("3. keluar")
while True:
	jawaban= raw_input()
	if jawaban == '1':
		ip = '10.72.99.159' #ip 4g selalu berubah
		s.connect((ip,8081))
		data = "adanya penyesuaian IP layanan pada Fog B" 
		s.send(data.encode())
		s.close()
	elif jawaban == '2':
		os.system("python notif.py")
	elif jawaban=='3':
		break
