#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
deviceId = "DTD1XVUc"
deviceKey = "wJIIZlJuqNwZUT7q"
import time
import sys
import httplib, urllib
import json
def post_to_mcs(payload): 
	headers = {"Content-type": "application/json", "deviceKey": deviceKey} 
	not_connected = 1 
	while (not_connected):
		try:
			conn = httplib.HTTPConnection("api.mediatek.com:80")
			conn.connect() 
			not_connected = 0 
		except (httplib.HTTPException, socket.error) as ex: 
			print "Error: %s" % ex
			time.sleep(10)
			 # sleep 10 seconds 
	conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers) 
	response = conn.getresponse() 
	print( response.status, response.reason, json.dumps(payload), time.strftime("%c")) 
	data = response.read() 
	conn.close() 
while True:
	SwitchStatus = GPIO.input(24)
	if( SwitchStatus == 0):
		print('button pressed')
	else:
		print('button released')
	payload = {"datapoints":[{"dataChnId":"Humidity","values":{"value":0}},
		{"dataChnId":"Temperature","values":{"value":0}},{"dataChnId":"SwitchStatus"
                ,"values":{"value":SwitchStatus}}]}
	post_to_mcs(payload)
	time.sleep(1)
