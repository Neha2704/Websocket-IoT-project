#!/usr/bin/env python

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

def on_connect(client, userdata, rc, a):
    print ("Connected with rc: " + str(rc))
    client.subscribe("topic")

def on_message(client, userdata, msg):
    #print ("Topic: "+ msg.topic+"\nMessage: "+str(msg.payload))
    if msg.payload.decode() == 'Orange light on':
        print ('Orange led is ON!\n')
        GPIO.output(18,GPIO.HIGH)
    elif msg.payload.decode() == 'Orange light off':
        print ('Orange led is OFF!\n')
        GPIO.output(18,GPIO.LOW)
    elif msg.payload.decode() == 'red light on':
        print ('Red led is ON!\n')
        GPIO.output(14,GPIO.HIGH)
    elif msg.payload.decode() == 'red light off':
        print ('Red led is OFF!\n')
        GPIO.output(14,GPIO.LOW)                                          
        

client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
client.loop_forever()
