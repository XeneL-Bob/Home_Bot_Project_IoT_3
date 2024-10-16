import RPi.GPIO as GPIO
import time

class UltrasonicSensor:
    def __init__(self, trig_pin, echo_pin):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def get_distance(self):
        # Send trigger signal
        GPIO.output(self.trig_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trig_pin, False)

        # Wait for echo signal
        start_time = time.time()
        stop_time = time.time()

        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()
        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()

        # Calculate distance
        time_elapsed = stop_time - start_time
        distance = (time_elapsed * 34300) / 2  # Speed of sound = 34300 cm/s
        return distance