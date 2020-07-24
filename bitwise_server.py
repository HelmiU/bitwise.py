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
num1 = random.randint(0,100)
num2 = random.randint(0,100)
bits = '1111111'
#binum1= bin(num1)[2:]
#binum2= bin(num2)[2:]
binernum1 = '{0:0{1}b}'.format(int(num1),len(bits))
binernum2 = '{0:0{1}b}'.format(int(num2),len(bits))
print(num1)
print(num2)
op = random.choice(list(ops.keys()))
op1 = random.choice(list(ops1.keys()))
op2= random.choice(list(ops2.keys()))
answer = ops.get(op)(int(num1),int(num2))
answer1 = ops1.get(op1)(int(num1),int(num2))
answer2 = ops2.get(op2)(int(num1),int(num2))
jawabanA = '{0:0{1}b}'.format(answer,len(bits))
jawabanB = '{0:0{1}b}'.format(answer1,len(bits))
jawabanC = '{0:0{1}b}'.format(answer2,len(bits))
a= datetime.now().strftime('%M')
print(a)
if a<='20':
	print ("masuk pada sesi 1")
	soal = ('selesaikan {} {} {}?\n'.format(binernum1, op, binernum2))
	soc.send(soal)
	jawaban = soc.recv(1024)
	if  str(jawabanA)== str(jawaban):
		respon = ("jawaban anda benar")
		soc.send(respon)
		print("mulai tersambung dengan client")
	else :
		respon= ("jawaban anda salah")
		soc.send(respon)
		print("gagal terhubung dengan client")
elif a<='40':
	print("masuk pada sesi 2")
	soal1 = ('selesaikan  {} {} {}?\n'.format(binernum1, op1, binernum2))
	soc.send(soal1)
	jawaban = soc.recv(1024)
	if str(jawaban) == str(jawabanB):
		respon = ("jawaban anda benar")
		soc.send(respon)
		print("mulai tersambung dengan client")
	else :
		respon= ("jawaban anda salah")
		soc.send(respon)
		print("gagal terhubung dengan client")
elif a<='59':
	print("masuk pada sesi 3")
	soal2 = ('selesaikan  {} {} {}?\n'.format(binernum1, op2, binernum2))
	soc.send(soal2)
	jawaban = soc.recv(1024)
	if str(jawaban) == str(jawabanC):
		respon = ("jawaban anda benar")
		soc.send(respon)
		print("mulai tersambung dengan client")
	else :
		respon= ("jawaban anda salah")
		soc.send(respon)
		print("gagal terhubung dengan client")

soc.close()
