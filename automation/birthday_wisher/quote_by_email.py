import random
import smtplib
from email.mime.text import MIMEText
from data.env_vars import FROM_ADDRESS, TO_ADDRESS, PASSWORD
import datetime as dt


def get_quote():
    with open("./quotes.txt", "r") as file:
        data = file.readlines()
    return random.choice(data)


def send_mail(text):
    from_address = FROM_ADDRESS
    to_address = TO_ADDRESS
    password = PASSWORD

    msg = MIMEText(f"The Quote of the Day is\n\n{text}", "plain")

    msg["From"] = from_address
    msg["To"] = to_address
    msg["Subject"] = "Quote of the Week"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as conn:
        try:
            conn.login(from_address, password)
            conn.sendmail(from_address, from_address, msg.as_string())
            print("Mail sent successfully!")
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")


if dt.datetime.now().weekday() == 1:
    quote_of_the_day = get_quote()
    send_mail(quote_of_the_day)
