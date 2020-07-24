from datetime import datetime
import operator
import random
import socket

#main
s = socket.socket()
port=8080
ip =''
s.bind(('',port))
s.listen(5)
soc, client_address = s.accept()
ops = {'&':operator.and_}
ops1 = {'|':operator.or_}
ops2 = {'^':operator.xor}
num1 = random.randint(0,15)
num2 = random.randint(0,15)
bits = '1111'
binum1= bin(num1)[2:]
binum2= bin(num2)[2:]
binernum1 = '{0:0{1}b}'.format(int(num1),len(bits))
binernum2 = '{0:0{1}b}'.format(int(num2),len(bits))
print(num1)
print(num2)
op = random.choice(list(ops.keys()))
op1 = random.choice(list(ops1.keys()))
op2= random.choice(list(ops2.keys()))
answer = int(binernum1) & int(binernum2)
answer1 = (int(binum1) | int(binum2))
answer2 = (int(binum1) ^ int(binum2))
#a= datetime.now().strftime('%M')
a='15'
print (answer)
print(a)

if a<='20':
	print ("masuk pada sesi 1")
	soal = ('selesaikan {} & {}?\n'.format(binernum1, binernum2))
	soc.send(soal)
	jawaban = soc.recv(1024)
	if jawaban == str(answer):
		respon = ("jawaban anda benar")
		soc.send(respon)
		print("mulai tersambung dengan client")
	else :
		respon= ("jawaban anda salah")
		soc.send(respon)
		print("gagal terhubung dengan client")
elif a<='40':
	print("masuk pada sesi 2")
	soal1 = ('selesaikan  {} | {}?\n'.format(binernum1, binernum2))
	soc.send(soal1)
	jawaban = soc.recv(1024)
	if jawaban == str(answer1):
		respon = ("jawaban anda benar")
		soc.send(respon)
		print("mulai tersambung dengan client")
	else :
		respon= ("jawaban anda salah")
		soc.send(respon)
		print("gagal terhubung dengan client")
elif a<='59':
	print("masuk pada sesi 3")
	soal2 = ('selesaikan  {} ^ {}?\n'.format(binernum1, binernum2))
	soc.send(soal2)
	jawaban = soc.recv(1024)
	if jawaban == str(answer2):
		respon = ("jawaban anda benar")
		soc.send(respon)
		print("mulai tersambung dengan client")
	else :
		respon= ("jawaban anda salah")
		soc.send(respon)
		print("gagal terhubung dengan client")

soc.close()
