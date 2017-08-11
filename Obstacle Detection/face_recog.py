import RPI.GPIO as GPIO
import os
import time

#GPIO mode (BOARD/BCM)
GPIO.setup(GPIO.BOARD)

TO_BUTTON = 32
FROM_BUTTON = 33

GPIO.setup(TO_BUTTON, GPIO.OUT)
GPIO.setup(FROM_BUTTON, GPIO.IN)

GPIO.output(TO_BUTTON, False)
GPIO.output(FROM_BUTTON, False)

while 1:	
	GPIO.output(TO_BUTTON, True)

	#Calling the face recognition program
	if GPIO.output(FROM_BUTTON, True):
		os.system('python recognizer.py')
	############################
	