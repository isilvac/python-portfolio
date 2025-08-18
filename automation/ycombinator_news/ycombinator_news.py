import random
from email.mime.text import MIMEText
from data.env_vars import FROM_ADDRESS, TO_ADDRESS, PASSWORD

from bs4 import BeautifulSoup
import requests
import smtplib


def format_mail_content(content: list) -> str:
    signature = ['Have a nice day!', 'Have a good one', 'See you tomorrow!', 'Chao!']
    formatted_news = ''
    for news in content:
        if news["url"].startswith('item?'):
            news["url"] = "https://news.ycombinator.com/" + news["url"]
        formatted_news += f"({news["score"]} votes) {news["title"]}\n{news["url"]}\n\n"
    formatted_news += random.choice(signature)
    return formatted_news


def send_mail(text: list):
    ''' Sends an email with the top 5 news from YCombinator to myself '''
    email_address = TO_ADDRESS
    password = PASSWORD

    msg = MIMEText(f"{format_mail_content(text)}", "plain")

    msg["From"] = email_address
    msg["To"] = email_address
    msg["Subject"] = "YCombinator Top 5 News of the Day"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as conn:
        try:
            conn.login(email_address, password)
            conn.sendmail(email_address, email_address, msg.as_string())
            print("Mail sent successfully!")
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")


article_titles = []
article_links = []
response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.findAll(class_="titleline")
for item in articles:
    article_titles.append(item.find(name="a").text)
    article_links.append(item.find(name="a").get("href"))
article_upvotes = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]

ordered_articles_by_score = []
for _ in article_upvotes:
    largest_index = max(article_upvotes)
    item_pos = article_upvotes.index(largest_index)
    item = {
        "title": article_titles[item_pos],
        "url": article_links[item_pos],
        "score": largest_index
    }
    ordered_articles_by_score.append(item)
    article_upvotes[item_pos] = 0

send_mail(ordered_articles_by_score[:5:])
