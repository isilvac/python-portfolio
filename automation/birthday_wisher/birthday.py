from email.mime.text import MIMEText
from random import randint
from data.env_vars import FROM_ADDRESS, TO_ADDRESS, PASSWORD
import smtplib
import pandas
import datetime as dt


TODAY = dt.datetime.now()


def get_today_birthdays():
    month = TODAY.month
    day = TODAY.day
    with open("data/birthdays.csv", "r") as file:
        data = pandas.read_csv(file)
        all_birthdays = data.to_dict(orient="records")
    return [item for item in all_birthdays if (item["month"] == month and item["day"] == day)]


def get_template(person):
    text = ""
    with open(f"./data/letter_templates/letter_{randint(1, 3)}.txt", "r") as file:
        for line in file.readlines():
            text += line.replace("[NAME]", person)
    return text


def send_mail(text):
    from_address = FROM_ADDRESS
    to_address = TO_ADDRESS
    password = PASSWORD

    msg = MIMEText(f"{text}", "plain")

    msg["From"] = from_address
    msg["To"] = to_address
    msg["Subject"] = "HAPPY BIRTHDAY!!"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as conn:
        try:
            conn.login(from_address, password)
            conn.sendmail(from_address, from_address, msg.as_string())
            print("Mail sent successfully!")
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")


people_birthdays = get_today_birthdays()
names = [people["name"] for people in people_birthdays]
if len(names) == 1:  # One birthday
    print(f"It's {names[0]} birthday!")
elif len(names) == 0:  # NO cake today :(
    print("No birthdays today")
else:  # Cakes for everybody!
    print(f"It's {names[0]} and others birthday!")
for name in names:
    send_mail(get_template(name))
