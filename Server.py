import os
import socket
import sys
from _thread import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 8000
try:
        s.bind((host,port))
except socket.error as e:
        print(str(e))

s.listen(5)

def threaded_client(conn):
        #conn.send(str.encode('Type something...'))

        while True:
                data = conn.recv(1024)
                reply = data.decode('utf-8')

                if not data:
                        break
                
                print ('Server output: ' + reply)
                
                if reply == 'red light on':
                        print ('Red led is ON!\n')
                        GPIO.output(14,GPIO.HIGH)
                        conn.send(str.encode('RED led is ON!'))
                        os.system("espeak \"Red light is on\"")
                        
                elif reply == 'red light off':
                        print ('Red led is OFF!\n')
                        GPIO.output(14,GPIO.LOW)
                        conn.send(str.encode('RED led is OFF!'))
                        os.system("espeak \"Red light is off\"")
                
                elif reply == 'Orange light on':
                        print ('Orange led is ON!\n')
                        GPIO.output(18,GPIO.HIGH)
                        conn.send(str.encode('ORANGE led is ON!'))
                        os.system("espeak \"Orange light is on\"")

                elif reply == 'Orange light off':
                        print ('Orange led is OFF!\n')
                        GPIO.output(18,GPIO.LOW)
                        conn.send(str.encode('ORANGE led is OFF!'))
                        os.system("espeak \"Orange light is off\"")

                #conn.sendall(str.encode(reply))
        conn.close()

while True:
	conn, addr = s.accept()
	print ('Got connection from ' + addr[0] + ':' + str(addr[1]))

	start_new_thread(threaded_client,(conn,))
