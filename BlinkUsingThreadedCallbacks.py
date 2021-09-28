import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


pwm1 = GPIO.PWM(4, 1)
pwm2 = GPIO.PWM(20, 1)
pwm3 = GPIO.PWM(21, 1)

def myCallback(pin):
  try:
    if pin == 20:
      pwm1.start(0)
      for d1 in range(101):
        pwm1.ChangeDutyCycle(d1)
        sleep(0.005)
      for d2 in range(101):
        pwm1.ChangeDutyCycle(101 - d2)
        sleep(0.005)
    if pin == 21:
      pwm2.start(0)
      for d3 in range(101):
        pwm2.ChangeDutyCycle(d3)
        sleep(0.005)
      for d4 in range(101):
        pwm2.ChangeDutyCycle(101 - d4)
        sleep(0.005)
  except KeyboardInterrupt:
    print('\nExiting')


GPIO.add_event_detect(5, GPIO.RISING, callback=myCallback,bouncetime=200)
GPIO.add_event_detect(6, GPIO.RISING, callback=myCallback,bouncetime=200)

try:
  while 1:
    pwm3.start(50)
except KeyboardInterrupt:
  print('\nExiting')


pwm1.stop()
pwm2.stop()
pwm3.stop()

GPIO.cleanup()