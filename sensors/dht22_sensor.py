import Adafruit_DHT

class DHT22Sensor:
    def __init__(self, pin):
        self.sensor = Adafruit_DHT.DHT22
        self.pin = pin

    def read(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity is not None and temperature is not None:
            return temperature, humidity
        else:
            print("Failed to get reading. Trying again...")
            return None, None
