import webiopi

GPIO = webiopi.GPIO
LIGHT = 25

def setup():
  GPIO.setFunction(LIGHT, GPIO.OUT)

def loop():
  webiopi.sleep(1)

def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)
