import RPi.GPIO as GPIO
GPIO.setmode(GPIO,BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:

	SwitchStatus = GPIO.input(24)
	if( SwitchStatus == 0):
		print('Button pressed')
	else:
		print('Button released')
