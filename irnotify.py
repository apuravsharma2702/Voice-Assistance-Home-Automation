import urllib2
import json
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.IN)
GPIO.setup(12,GPIO.OUT) 

def sendNotification(token, channel, message):
	data = 
	{
		"body" : message,
		"message_type" : "text/plain"
	}

	req = urllib2.Request('http://api.pushetta.com/api/pushes/{0}/'.format(channel))
	req.add_header('Content-Type', 'application/json')
	req.add_header('Authorization', 'Token {0}'.format(token))

	response = urllib2.urlopen(req, json.dumps(data))
flag=1
state=GPIO.input(27)
while True:
	if GPIO.input(27)==True and flag==1:
		token1="61a2a5e3869469eac2f1e5cfaa6d99eb87a2070c"
		mychannel="grp7led" 
		message="Someone is on the door." 
		GPIO.output(12,GPIO.HIGH)
		flag=0
  
		sendNotification(token1,mychannel,message)
 
		if state==False and flag==0:
			flag=1
			GPIO.output(12,GPIO.LOW)
