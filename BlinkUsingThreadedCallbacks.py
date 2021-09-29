import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


pwm4 = GPIO.PWM(4, 1)
pwm23 = GPIO.PWM(23, 1)
pwm24 = GPIO.PWM(24, 1)

def myCallback(pin):
  if pin == 5:
    pwm4.start(0)
    for d1 in range(100):
      pwm4.ChangeDutyCycle(d1)
      sleep(0.05)
    for d2 in range(100):
      pwm4.ChangeDutyCycle(100 - d2)
      sleep(0.05)
  if pin == 6:
    pwm23.start(0)
    for d3 in range(100):
      pwm23.ChangeDutyCycle(d3)
      sleep(0.05)
    for d4 in range(100):
      pwm23.ChangeDutyCycle(100 - d4)
      sleep(0.05)
  


GPIO.add_event_detect(5, GPIO.RISING, callback=myCallback,bouncetime=200)
GPIO.add_event_detect(6, GPIO.RISING, callback=myCallback,bouncetime=200)

try:
  while 1:
    pwm24.start(50)
except KeyboardInterrupt:
  print('\nExiting')
  pwm4.stop()
  pwm23.stop()
  pwm24.stop()
  GPIO.cleanup()




