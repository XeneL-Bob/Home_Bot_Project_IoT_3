from flask import Flask, render_template
import leds.led_control as led

app = Flask(__name__)
led_control = led.LEDControl(green_pin=17, yellow_pin=27)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led/green/on')
def green_led_on():
    led_control.turn_on_green()
    return "Green LED is ON"

@app.route('/led/green/off')
def green_led_off():
    led_control.turn_off_green()
    return "Green LED is OFF"

@app.route('/led/yellow/on')
def yellow_led_on():
    led_control.turn_on_yellow()
    return "Yellow LED is ON"

@app.route('/led/yellow/off')
def yellow_led_off():
    led_control.turn_off_yellow()
    return "Yellow LED is OFF"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
