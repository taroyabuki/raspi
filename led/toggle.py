import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

ledState = False

try:
  while True:
    if GPIO.input(24) == GPIO.HIGH:
      ledState = not ledState
      if ledState == True:
        GPIO.output(25, GPIO.HIGH)
      else:
        GPIO.output(25, GPIO.LOW)
      sleep(0.2)
    sleep(0.01)
except KeyboardInterrupt:
  pass

GPIO.cleanup()
