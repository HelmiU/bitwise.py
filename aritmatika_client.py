from datetime import datetime

import socket    
import operator

ip2 ='192.168.43.207'
#ip2 = map_network.ip()
#print (ip2)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip2,8080))
soal = s.recv(1024)
print (soal)	
print ('jawabannya  ' ) 
jawaban= raw_input()
s.send(str(jawaban))
respon = s.recv(1024)
print(respon)
pem = ("jawaban anda benar")
if respon == pem :
	print("mulai terhubung dengan server")
	s.close()
else :
	print("gagal terhubung dengan client")
	s.close()
s.close()

