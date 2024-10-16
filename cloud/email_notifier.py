import smtplib
from email.mime.text import MIMEText

def send_email_alert(temperature):
    msg = MIMEText(f"Warning: Room temperature has exceeded {temperature}°C.")
    msg['Subject'] = 'Temperature Alert'
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = 'recipient_email@gmail.com'

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login("your_email@gmail.com", "your_password")
            server.sendmail("your_email@gmail.com", "recipient_email@gmail.com", msg.as_string())
        print("Alert email sent.")
    except Exception as e:
        print(f"Error sending email: {e}")
