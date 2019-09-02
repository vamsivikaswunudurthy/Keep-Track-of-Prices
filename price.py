import requests
from bs4 import BeautifulSoup
import regex
import smtplib



url="https://www.amazon.in/Apple-MacBook-Pro-9th-Generation-Intel-Core-i9/dp/B07SDPJ531/ref=sr_1_4?keywords=macbook+pro+15+inch&qid=1566634572&s=gateway&sr=8-4"

headers ={"useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}

def check_price():
    page = requests.get(url,headers = headers)
    soup = BeautifulSoup(page.content,"html.parser")

    title = soup.find(id="productTitle").getText()
    ctitle = title.strip()
    price =soup.find(id="priceblock_ourprice").getText()
    # finding price
    # removing comma and rupee sign we will be using regex
    price = float(regex.sub('\,', '', price[2:]))
    #remove decimal
    convertprice = str(price).split('.')[0]
    cprice =int(convertprice)

    print(ctitle)
    print(cprice)

    if(cprice > 200000):
        send_mail()
    else:
        print("price has not changed")




def send_mail():
    server =smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('vamsivikas1993@gmail.com','VamsIvikas091193')

    subject = "price fell down"

    body = "check the amazon link https://www.amazon.in/Apple-MacBook-Pro-9th-Generation-Intel-Core-i9/dp/B07SDPJ531/ref=sr_1_4?keywords=macbook+pro+15+inch&qid=1566634572&s=gateway&sr=8-4"

    #msg ="Subject:,{}\n,{}\n" .format(subject,body)
    msg = f"Subject:{subject}\n\nlink-{body}"



    server.sendmail(
        "vamsivikas1993@gmail.com",
        "vamsivikaswunudurthy@gmail.com",
        msg
    )

    print("email has been sent")

    server.quit()


check_price()