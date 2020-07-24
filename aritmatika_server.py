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
running = True
ops = {'+':operator.add}
ops1 = {'-':operator.sub}
ops2 = {'*':operator.mul}
ops3 = {'%':operator.mod}
num1 = random.randint(0,100)
num2 = random.randint(0,100)  
op = random.choice(list(ops.keys()))
op1 = random.choice(list(ops1.keys()))
op2= random.choice(list(ops2.keys()))
op3= random.choice(list(ops3.keys()))
answer = ops.get(op)(num1,num2)
answer1 = ops1.get(op1)(num1,num2)
answer2 = ops2.get(op2)(num1,num2)
answer3 = ops3.get(op3)(num1,num2)
a= datetime.now().strftime('%M')
print(a)
if a<='15':
	print ("masuk pada sesi 1")
	soal = ('berapa hasil operasi perhitungan  {} {} {}?\n'.format(num1, op, num2))
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
elif a<='30':
	print("masuk pada sesi 2")
	soal1 = ('berapa hasil operasi perhitungan  {} {} {}?\n'.format(num1, op1, num2))
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
elif a<='45':
	print("masuk pada sesi 3")
	soal2 = ('berapa hasil operasi perhitungan  {} {} {}?\n'.format(num1, op2, num2))
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
elif a<='59':
	print("masuk pada sesi 4")
	soal3 = ('berapa hasil operasi perhitungan  {} {} {}?\n'.format(num1, op3, num2))
	soc.send(soal3)
	jawaban = soc.recv(1024)
	if jawaban == str(answer3):
		respon = ("jawaban anda benar")
		soc.send(respon)
		print("mulai tersambung dengan client")
	else :
		respon= ("jawaban anda salah")
		soc.send(respon)
		print("gagal terhubung dengan client")
