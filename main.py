import time
import sensors.dht22_sensor as dht22
import sensors.ultrasonic_sensor as ultrasonic
import leds.led_control as led
import sensors.push_button as button
import cloud.cloud_logger as logger
import cloud.email_notifier as notifier

# Threshold for sending temperature alerts (in Celsius)
TEMP_ALERT_THRESHOLD = 30

def main():
    try:
        # Initialize components
        dht22_sensor = dht22.DHT22Sensor(pin=4)
        ultrasonic_sensor = ultrasonic.UltrasonicSensor(trig_pin=23, echo_pin=24)
        push_button = button.PushButton(pin=22)
        led_control = led.LEDControl(green_pin=17, yellow_pin=27)
        
        # Main loop
        while True:
            # Read temperature, humidity and distance
            temperature, humidity = dht22_sensor.read()
            distance = ultrasonic_sensor.get_distance()

            # Logging to cloud (Google Sheets)
            logger.log_to_google_sheets(temperature, humidity, distance)

            # Control LEDs based on distance (presence detection)
            if distance < 100:  # Detect presence
                led_control.turn_on_green()
                led_control.turn_off_yellow()
            else:
                led_control.turn_on_yellow()
                led_control.turn_off_green()

            # Send an alert if temperature exceeds threshold
            if temperature > TEMP_ALERT_THRESHOLD:
                notifier.send_email_alert(temperature)

            # Push button LED control (manual override)
            if push_button.is_pressed():
                led_control.toggle_green()
                led_control.toggle_yellow()

            # Wait before the next reading
            time.sleep(5)

    except KeyboardInterrupt:
        print("System interrupted. Cleaning up...")
        led_control.cleanup()

if __name__ == '__main__':
    main()
