import RPi.GPIO as GPIO

LedPin = 12    # pin12 --- led

GPIO.setmode(GPIO.BOARD)       # Pinagem física
GPIO.setup(LedPin, GPIO.OUT)   # Pino de led como saída