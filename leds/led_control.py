import RPi.GPIO as GPIO

class LEDControl:
    def __init__(self, green_pin, yellow_pin):
        self.green_pin = green_pin
        self.yellow_pin = yellow_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.yellow_pin, GPIO.OUT)

    def turn_on_green(self):
        GPIO.output(self.green_pin, True)

    def turn_off_green(self):
        GPIO.output(self.green_pin, False)

    def turn_on_yellow(self):
        GPIO.output(self.yellow_pin, True)

    def turn_off_yellow(self):
        GPIO.output(self.yellow_pin, False)

    def toggle_green(self):
        GPIO.output(self.green_pin, not GPIO.input(self.green_pin))

    def toggle_yellow(self):
        GPIO.output(self.yellow_pin, not GPIO.input(self.yellow_pin))

    def cleanup(self):
        GPIO.cleanup()
