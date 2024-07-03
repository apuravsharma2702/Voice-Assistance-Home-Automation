import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.IN)
GPIO.setup(25,GPIO.OUT)
flag=1
while True:
	state=GPIO.input(22)
	if state==True and flag==1:
		print("Gas has been detected.")
		flag=0
	GPIO.output(25,GPIO.HIGH)
  # time.sleep(2)
   

	if state==False and  flag==0:
		print("Gas has not been detected")
		flag=1
	GPIO.output(25,GPIO.LOW)

