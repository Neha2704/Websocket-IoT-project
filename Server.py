import os
import socket
import sys
from _thread import *
import RPi.GPIO as GPIO
import time
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

red_pin = 14
orange_pin = 15
blue_pin = 18

red_flag = False
orange_flag = False
blue_flag = False

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup (red_pin, GPIO.OUT)
GPIO.setup (orange_pin, GPIO.OUT)
GPIO.setup (blue_pin, GPIO.OUT)

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 8000
try:
        s.bind((host,port))
except socket.error as e:
        print(str(e))
        
s.listen(5)

def threaded_client(conn):
        
        while True:
              
                global serial_input
                temp = serial_input[2] + serial_input[3]
                humidity = serial_input[4] + serial_input[5]

                data = conn.recv(1024)
                reply = data.decode('utf-8')

                global red_flag
                global orange_flag
                global blue_flag

                if not data:
                        break
                
                print ('\n\nYou: ' + reply)

                ################### RED ###################
                
                if 'red' in reply or 'Red' in reply or 'read' in reply:

                        if 'on' in reply:

                                GPIO.output(red_pin, GPIO.HIGH)
                                conn.send(str.encode('RED light is ON!'))

                                red_flag = True
                                print ('Pi: RED light is ON!')
                                break;
                                #os.system("espeak \"Switching on the red light\"")

                        elif 'off' in reply or 'of' in reply:
                                
                                GPIO.output(red_pin, GPIO.LOW)
                                conn.send(str.encode('RED light is OFF!'))

                                red_flag = False
                                print ('Pi: RED light is OFF!')
                                break;
                                #os.system("espeak \"Switching off the red light\"")
                        
                        else:

                                if red_flag is True:
                                      conn.send(str.encode('RED light status: ON'))
                                      print ('Pi: RED light is ON!')
                                      break;
                                else:
                                      conn.send(str.encode('RED light status: OFF'))
                                      print ('Pi: RED light is OFF!')
                                      break;
                              
                ############### ORANGE #########################
                
                elif 'Orange' in reply or 'orange' in reply:
                        
                        if 'on' in reply:

                                GPIO.output(orange_pin, GPIO.HIGH)
                                conn.send(str.encode('ORANGE light is ON!'))

                                orange_flag = True
                                print ('Pi: ORANGE light is ON!')
                                break;
                                #os.system("espeak \"Switching on the orange light\"")
                        
                        elif 'off' in reply or 'of' in reply:
                                
                                GPIO.output(orange_pin, GPIO.LOW)
                                conn.send(str.encode('ORANGE light is OFF!'))
                        
                                orange_flag = False
                                print ('Pi: ORANGE light is OFF!')
                                break;
                                #os.system("espeak \"Switching off the orange light\"")
                        
                        else:

                                if orange_flag is True:
                                      conn.send(str.encode('ORANGE light status: ON'))
                                      print ('Pi: ORANGE light is ON!')
                                      break;
                                else:
                                      conn.send(str.encode('ORANGE light status: OFF'))
                                      print ('Pi: ORANGE light is OFF!')
                                      break;

                ###################### BLUE ##############################
                
                elif 'blue' in reply or 'Blue' in reply:

                        if 'on' in reply:
                        
                                GPIO.output(blue_pin,GPIO.HIGH)
                                conn.send(str.encode('BLUE light is ON!'))
                        
                                blue_flag = True
                                print ('Pi: BLUE light is ON!')
                                break;
                                #os.system("espeak \"Switching on the blue light\"")
                        
                        elif 'off' in reply or 'of' in reply:

                                GPIO.output(blue_pin, GPIO.LOW)
                                conn.send(str.encode('BLUE light is OFF!'))

                                blue_flag = False
                                print ('Pi: BLUE light is OFF!')
                                break;
                                #os.system("espeak \"Switching off the blue light\"")
                        
                        else:

                                if blue_flag is True:
                                      conn.send(str.encode('BLUE light status: ON'))
                                      print ('Pi: BLUE light is ON!')
                                      break;
                                else:
                                      conn.send(str.encode('BLUE light status: OFF'))
                                      print ('Pi: BLUE light is OFF!')
                                      break;
                                      
                ##################################################################

                elif 'all' in reply or 'All' in reply or 'al' in reply:

                        if 'on' in reply:

                                GPIO.output(red_pin, GPIO.HIGH)
                                GPIO.output(blue_pin, GPIO.HIGH)
                                GPIO.output(orange_pin, GPIO.HIGH)
                                conn.send(str.encode('ALL lights are ON!'))

                                red_flag = True
                                blue_flag = True
                                orange_flag = True
                                print ('Pi: ALL lights are ON!')
                                break;
                                #os.system("espeak \"Switching on the red light\"")

                        elif 'off' in reply or 'of' in reply:
                                
                                GPIO.output(red_pin, GPIO.LOW)
                                GPIO.output(blue_pin, GPIO.LOW)
                                GPIO.output(orange_pin, GPIO.LOW)
                                conn.send(str.encode('ALL lights are OFF!'))

                                red_flag = False
                                blue_flag = False
                                orange_flag = False
                                print ('Pi: ALL lights are OFF!')
                                break;
                                #os.system("espeak \"Switching off the red light\"")

                                      
                ###############################################################
                                        
                elif 'temperature' in reply:

                        print ('Pi: Temperature is ' + temp + ' degrees')
                        conn.send(str.encode('Temperature: ' + temp + ' degrees'))
                        
                elif 'humidity' in reply:

                        print('Pi: Humidity is ' + humidity + '%')
                        conn.send(str.encode('Humidity: ' + humidity + '%'))

                elif 'thank you' in reply:

                        print('Pi: You\'re welcome')
                        conn.send(str.encode('You\'re welcome'))

                else:
                        print('Pi: What was that?')
                        conn.send(str.encode('What was that?'))

        conn.close()

def socketinput(a):

        global conn
        global addr
        conn, addr = s.accept()
        #print ('Got connection from ' + addr[0] + ':' + str(addr[1]))
        start_new_thread(threaded_client,(conn,))


while True:
        
        serial_input = str(ser.readline())
        room =  serial_input[6] + serial_input[7] + serial_input[8]

        if room[0] == '9' or room[0] == '8':

                GPIO.output(blue_pin,GPIO.HIGH)
                GPIO.output(orange_pin,GPIO.HIGH)
                GPIO.output(red_pin,GPIO.HIGH)

                red_flag = True
                orange_flag = True
                blue_flag = True
     
        start_new_thread(socketinput,('abc',))
