import requests
from lxml import html
def unitMessage(scrip):
    url = "https://www.nepsealpha.com/search?q=" + scrip
    r = requests.get(url)
    hellYea = html.fromstring(r.content)
    price = float(hellYea.xpath("/html/body/div/div[4]/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/table/thead/tr/th/h2/text()")[1].strip())
    thisMessage = "\n" + scrip.upper() + ' price has reached ' + str(price) + "."
    return thisMessage
