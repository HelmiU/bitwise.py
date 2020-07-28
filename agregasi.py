import socket
import time
import os
import datetime

class Timer(object):
    """A simple timer class"""
    
    def __init__(self):
        pass
    def start(self):
        """Starts the timer"""
        self.start = datetime.datetime.now()
    def stop(self):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = datetime.datetime.now()
        print str(self.stop - self.start)
    def elapsed(self):
        """Time elapsed since start was called"""
        print str(datetime.datetime.now() - self.start)[:-3]
    def now(self):
	print str(datetime.datetime.now())[:-3]


watch=Timer()
s = socket.socket()
print("masukkan pilihan ")
print("1. beritahu user adanya penyesuaian ip")
print("2. menunggu user untuk tersambung")
print("3. keluar")
while True:
	jawaban= raw_input()
	watch.start()
	if jawaban == '1':
		ip = '10.16.144.116'
		s.connect((ip,8085))
		data = "adanya penyesuaian IP layanan pada Fog B" 
		s.send(data.encode())
		watch.elapsed()#capture waktu
		s.close()
	elif jawaban == '2':
		#run = s.recv(1024).decode()
		os.system("python notif.py")
		watch.elapsed()#capture waktu
		break
	elif jawaban=='3':
		break
