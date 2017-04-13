import RPI.GPIO as GPIO
import time

#GPIO mode (BOARD/BCM)
GPIO.setup(GPIO.BCM)

#Set the GPIO pins for the Ultrasonic sensor
TRIG = 
ECHO = 

#Set the GPIO pins for the vibration motor
vibrator_input = 

#Set the flow of the pins (IN and OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#making the GPIO port for the vibration motor as an output port
GPIO.setup(vibrator_input, GPIO.OUT)

GPIO.output(TRIG, False)
time.sleep()

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == 0:
	start_time = time.time()

while GPIO.input(ECHO) == 1:
	end_time == time.time()

total_time = end_time - start_time

#distance = speed * time
#speed of sound in air is 34300 cm/s
distance = (34300 * total_time) / 2
distance = round(distance, 4)
####### The code for the Ultrasonic sensor ends here #######

####### The following code is for the vibration motor ######
while distance  <= 100:
	GPIO.output(vibrator_input, True)