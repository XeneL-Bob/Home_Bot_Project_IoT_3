##############################################################################
Hello, this project designed to monitor environmental conditions and detect user presence in a room using a Raspberry Pi. 
The system includes temperature and humidity monitoring, presence detection, LED indicators for visual feedback, 
and push-button control for manual overrides. The system logs data to Google Sheets and sends email alerts when 
temperature thresholds are exceeded. A Flask web interface allows user to monitor the system and control LEDs remotely.

##############################################################################
Hardware Components

Raspberry Pi (Model 3B+ or higher)
HC-SR04 Ultrasonic Sensor (for presence detection)
DHT22 Temperature and Humidity Sensor
Green and Yellow LEDs
Push Button
Breadboard and resistors
Power Supply

##############################################################################
Software Components

Python 3
Flask Web Framework
Google Sheets API (for data logging)
SMTP (for email notifications)

##############################################################################
Project Features

Presence detection using the ultrasonic sensor.
Temperature and humidity monitoring using the DHT22 sensor.
Visual feedback with LEDs: Green for detected presence, Yellow for no movement.
Manual control of LEDs via push button.
Data logging to Google Sheets in real-time.
Email alerts when temperature exceeds predefined thresholds.
Remote monitoring and control through a Flask web interface.

##############################################################################

intelligent-home-environment/
│
├── main.py                       # Main script to run the system
├── sensors/
│   ├── dht22_sensor.py           # DHT22 sensor handling
│   ├── ultrasonic_sensor.py      # Ultrasonic sensor handling
│   ├── push_button.py            # Push button control
├── leds/
│   ├── led_control.py            # LED control for green/yellow LEDs
├── cloud/
│   ├── cloud_logger.py           # Logging to Google Sheets
│   ├── email_notifier.py         # Email alert system
├── web/
│   ├── app.py                    # Flask web app for monitoring and control
├── requirements.txt              # List of required Python libraries
└── README.md                     # Project documentation

#############################################################################

Setup Instructions
Hardware Setup:

Connect the ultrasonic sensor, DHT22 sensor, LEDs, and push button to the Raspberry Pi’s GPIO pins as outlined in the project's documentation.
Install Required Python Libraries: Ensure all required Python libraries are installed by running the following command:

bash
pip install -r requirements.txt

########################################
Google Sheets API Setup:

Create a Google Sheets document and configure the Google Sheets API.
Download your credentials.json file and place it in the cloud/ directory.

########################################
Email Setup:

Configure SMTP settings in email_notifier.py with your Gmail credentials (use an app-specific password for better security).

########################################
Run the Project:

Run the main Python script to start the system:
bash
python3 main.py

########################################

Access the Web Interface:
Start the Flask web server:

bash
cd web
python3 app.py

Access the interface by opening your web browser and going to http://<raspberry_pi_local_ip>:5000

#############################################################################
Usage

Monitor the room's environment (temperature, humidity, and presence) via the web interface or by checking the LEDs.
Manually toggle the LEDs with the push button or through the Flask web interface.
View the logged data in Google Sheets.
Receive email alerts when the temperature exceeds the defined threshold.

#############################################################################

##################
#############
#######

License:

This project is open-source and can be modified or distributed freely.

#######
#############
##################

