import requests
from bs4 import BeautifulSoup
import smtplib

# Get the product link
URL = 'https://www.amazon.ca/Apple-MWP22AM-A-AirPods-Pro/dp/B07ZPC9QD4/ref=sr_1_1_sspa?crid=1593I6ACVLV7W&dchild=1&keywords=airpods+pro&qid=1612195884&sprefix=airpo%2Caps%2C175&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQUxZWTRaN0lYNTFFJmVuY3J5cHRlZElkPUEwMDM1MzA2M05RQVNSR1lSWEIwVyZlbmNyeXB0ZWRBZElkPUEwNzA0MjEzMUZWSTVRRVFZNjhVTSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

# function to check the price of given product
def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[0:15]

    if(converted_price > 260.00):
        send_mail()

# function for send the mail if price is in given range
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('some@email.com', 'somePassword')
    subject = 'Price fell down!'
    body = 'Check amazon link: https://www.amazon.ca/Apple-MWP22AM-A-AirPods-Pro/dp/B07ZPC9QD4/ref=sr_1_1_sspa?crid=1593I6ACVLV7W&dchild=1&keywords=airpods+pro&qid=1612195884&sprefix=airpo%2Caps%2C175&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQUxZWTRaN0lYNTFFJmVuY3J5cHRlZElkPUEwMDM1MzA2M05RQVNSR1lSWEIwVyZlbmNyeXB0ZWRBZElkPUEwNzA0MjEzMUZWSTVRRVFZNjhVTSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

    msg = "Subject: {subject}\n\n{body}".format(subject=subject, body=body)

    server.sendmail(
        'some@email.com',
        'other@email.com',
        msg
    )

    print("Email Sent Successfully.")
    server.quit()


check_price()
