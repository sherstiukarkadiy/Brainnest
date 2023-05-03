from pathlib import Path
import json
from playsound import playsound
import sys

error_sound = Path(__file__).parent.joinpath("Sounds/windows-error.mp3")

# USER INFORMATION
SENDER_JSON = Path(__file__).parent.joinpath("sender_info.json")
with open(SENDER_JSON, "r") as user:
    user_info = user.read()
    user_info = json.loads(user_info)
    
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = user_info["sender-email"] 
SENDER_NAME = user_info["sender-name"]
APP_PASSWORD = user_info["password"]
SMTP_PORT = 465

if len(SENDER_EMAIL) == 0 or len(SENDER_NAME) == 0 or len(APP_PASSWORD) == 0:
    playsound(error_sound)
    print("Not enough information, add it in sender_info.json file")
    sys.exit()

