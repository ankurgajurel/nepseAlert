"Please don't edit this file"

import requests
from lxml import html

def mainFn():
    scrip = input("Enter the company symbol: ")
    target = float(input("Enter you target price: "))
    url = "https://www.nepsealpha.com/search?q=" + scrip
    r = requests.get(url)
    hellYea = html.fromstring(r.content)
    price = float(hellYea.xpath("/html/body/div/div[4]/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/table/thead/tr/th/h2/text()")[1].strip())

    while True:        
        if price > (target - 1):
            from plyer import notification 
            title = "The target of " + scrip + " has been reached"
            message = "The price of " + scrip + " has reached " + str(price)
            notification.notify(title = title, message = message)

            from twilio.rest import Client
            client = Client("AC0f742cb0a43176b34f73d596b5f03846", "f43f184c5ab7f08a3c3c082c3197b24f")
            client.messages.create(to = ["+9779818542902"], from_ = "+12019776138", body = message)
            break
        else:
            pass
               

mainFn()
    
