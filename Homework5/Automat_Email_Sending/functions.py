from user_constants import *
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import smtplib,ssl,os
import csv
from time import sleep
from random import uniform
import logging

def create_mesage(date: str,sender_name: str, receiver_name: str, html_path: Path, attachment_path: Path) -> MIMEMultipart:
    """Create MIMEMultipart message with subject, Text part, HTML part and Attachment

    Args:
        date (str): today's date (DD.MM.YYY)
        sender_name (str): name of user
        receiver_name (str): name of receiver
        html_path (Path): path to html file
        attachment_path (Path): path to attachmant file

    Returns:
        MIMEMultipart: email encoded message
    """

    # Message container
    msg = MIMEMultipart()
    msg['Subject'] = f"Daily report {date}"
    msg['From'] = sender_name
    msg['To'] = receiver_name
    
    # Message text version
    text_part = MIMEText(f"Dear {receiver_name}, please pay attention to this attacment", 'plain')
    
    # Message  HTML version
    with open(html_path, "r") as f: html_content = f.read()
    html_part = MIMEText(html_content, 'html')
    
    # attachments
    with open(attachment_path, 'rb') as f: att1 = f.read()
    attachment_part = MIMEBase('application', 'octet-stream')
    attachment_part.set_payload(att1)
    encoders.encode_base64(attachment_part)
    
    # add header
    attachment_part.add_header(
        'Content-disposition',
        f'attachment; filename={attachment_path.name}'
        )
    msg.attach(text_part)
    msg.attach(html_part)
    msg.attach(attachment_part)
    return msg

def save_to_log(logfile_path: Path, operation_result: dict, receiver_name: str, receiver_email: str) -> None:
    """Save results of sending to log file 

    Args:
        logfile_path (Path): path to log file with name format DD.MM.YYYY(today's date)
        operation_result (dict): return of sendmail function
        receiver_name (str): name of receiver
        receiver_email (str): receiver email
    """
    if not os.path.exists(logfile_path):
        log_date = datetime.now().strftime("%d.%b.%Y")
        with open(logfile_path, "w") as log:
            log.write(log_date+"\n")
    
    logging.basicConfig(level = logging.INFO, filename = logfile_path)
    if not operation_result:
        logging.info(f"{receiver_name} ({receiver_email}): Message sended")
    else:
        logging.error(f"{receiver_name} ({receiver_email}): {operation_result}")
    return

def send_message(date: str, pathes: dict) -> None:
    """Sending daily reports to clients via email taking information about clients from receivers file

    Args:
        date (str): today's date (DD.MM.YYYY)
        pathes (dict): dictionary with pathes to attachmant,receivers,html and log files
        where key are [attachmant,receivers,html,log] in string format and values are the pathes to files
    """
    
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=ssl.create_default_context()) as smtp_server:
        smtp_server.login(SENDER_EMAIL, APP_PASSWORD)
        with open(pathes["receivers"],"r") as file:
            reader = csv.reader(file)
            next(reader)
            for name, last_name, email in reader:
                receiver_name = f"{name} {last_name}"
                message = create_mesage(date,SENDER_NAME,receiver_name, pathes["html"],pathes["attachment"])
                try:
                    res = smtp_server.sendmail(SENDER_EMAIL, [email], message.as_string())
                except smtplib.SMTPRecipientsRefused as eror:
                    res = eror
                save_to_log(pathes["logfile"],res,receiver_name,email)
                delay = uniform(0.5,1)
                sleep(delay)
        



