import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name("path_to_your_credentials.json", scope)

# Authorize the clientsheet 
client = gspread.authorize(creds)

# Get the sheet
sheet = client.open("Home Environment Log").sheet1

def log_to_google_sheets(temperature, humidity, distance):
    try:
        row = [time.strftime("%Y-%m-%d %H:%M:%S"), temperature, humidity, distance]
        sheet.append_row(row)
        print("Data logged to Google Sheets.")
    except Exception as e:
        print(f"Error logging data: {e}")
