import RPI.GPIO as GPIO
import os
import time

#GPIO mode (BOARD/BCM)
GPIO.setup(GPIO.BOARD)
#Set the GPIO pins for the ultrasonic sensor
TRIG = 16
ECHO = 18

#Set the GPIO pins for the vibration motor
vibrator_input = 12 #Pulse Width Modulation pin

#Set the flow of the pins (IN and OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#making the GPIO port for the vibration motor as an output port
GPIO.setup(vibrator_input, GPIO.OUT)

GPIO.output(vibrator_input, False)

while 1:
	GPIO.output(TRIG, False)
	time.sleep(0.5)
	distance_list = []
	for i in range(10):
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)

		while GPIO.input(ECHO) == 0:
			start_time = time.time()

			while GPIO.input(ECHO) == 1:
				end_time == time.time()

				total_time = (end_time - start_time)

		#distance = speed * time
		#speed of sound in air is 34300 cm/s
		distance = (34300 * total_time) / 2
		distance = round(distance, 4)
		distance_list.append(distance)

		smallest_in_list = min(int(s) for s in distance_list)
	####### Code for the ultrasonic sensor ends here #######

	####### The following code is for the vibration motor ######
	if smallest_in_list  < 150:
		try:
			if smallest_in_list <= 100:
				GPIO.output(vibrator_input, True)
				time.sleep(1)
				GPIO.output(vibrator_input, False)
			else:
				GPIO.output(vibrator_input, True)
				time.sleep(0.2)
				GPIO.output(vibrator_input, False)

		except KeyboardInterrupt:
			GPIO.output(vibrator_input, False)