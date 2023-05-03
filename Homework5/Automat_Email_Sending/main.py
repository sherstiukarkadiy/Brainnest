from functions import *
from pathlib import Path
import schedule,time

date,log_date = datetime.now().strftime("%d.%m.%Y"), datetime.now().strftime("%d.%b.%Y")
pathes = {
    "attachment" : Path(__file__).parent.joinpath(f"Reports/DAYLY REPORT {date}.docx"),
    "receivers" : Path(__file__).parent.joinpath("receivers.csv"),
    "html" : Path(__file__).parent.joinpath("HTML/message.html"),
    "logfile" : Path(__file__).parent.joinpath(f"Log Files/{date}.log")
    }
with open(pathes["logfile"], "w") as log:
    log.write(log_date+"\n")

schedule.every().day.at("19:00").do(send_message, date, pathes)

while True:
    schedule.run_pending()
    time.sleep(1)