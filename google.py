import sys
import RPi.GPIO as a
from Adafruit_IO import MQTTClient
a.setmode(a.BCM)
a.setwarnings(False)
a.setup(4,a.OUT)
a.setup(18,a.OUT)

ADAFRUIT_IO_KEY = 'f0397362a8ad4fa3969bbf0d9b09f66d'
ADAFRUIT_IO_USERNAME = 'Sasuke2702'
FEED_ID = 'project1'
def connected(client):
	print('Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID))
	client.subscribe(FEED_ID)

def disconnected(client):
	print('Disconnected from Adafruit IO!')
	sys.exit(1)

def message(client, feed_id, payload):
	print('Feed {0} received new value: {1}'.format(feed_id, payload))
	if  payload=='FAN ON':
		a.output(4,a.LOW)
		print("Making FAN ON")
	if payload=='FAN OFF':
		a.output(4,a.HIGH)
		print("Making FAN OFF")
	if payload=='LIGHT ON':
		a.output(18,a.HIGH)
		print("Making LIGHT ON")
	if payload=='LIGHT OFF':
		a.output(18,a.LOW)
		print("Making LIGHT OFF")


client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

client.connect()

client.loop_blocking()

