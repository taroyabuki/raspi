import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
  while True:
    if GPIO.input(24) == GPIO.HIGH:
      print("ON")
    else:
      print("OFF")
    sleep(0.1)
except KeyboardInterrupt:
  pass

GPIO.cleanup()
