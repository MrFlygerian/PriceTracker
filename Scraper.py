# import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import smtplib

URL = "https://www.amazon.co.uk/dp/B07JQRYR5M/ref=" \
      "gw_uk_desk_h1_qh_tabl_mst_myp20?pf_rd_r=FESV7T9XC2X66Y6ERHEM&pf_rd_p=" \
      "05d25881-ea1e-4da2-a171-95249dbf5809"

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')

driver = webdriver.Chrome(options=options,
                          executable_path=r"C:\Users\bless\chromedriver_win32\chromedriver")



page = driver.get(URL)
myPrice = 10

def trackPrice():
    price = getPrice()[0]
    if price > myPrice:
        diff = abs(price-myPrice)
        print (f'{diff} too expensive')
    else:
        print('You can afford this')

#send_male()


def getPrice():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_dealprice").get_text()
    price = float(price[1:])
    print(title)
    print(price)
    return price, title

def send_male():

    subject = 'Price Change'
    text = "Subject:" + subject + '\n\n' + URL
    server = smtplib.SMTP(host='smtp.gmail.com',port =587 )

    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('blessed.chianumba@gmail.com', 'mjmfsybkmzldlucb')
    server.sendmail('blessed.chianumba@gmail.com','blessed.chianumba@gmail.com', text)
    print ('mail sent')


def store_price():
    price, title = getPrice()
    temp_dict = {'price': price, 'title': title}
    pass


if __name__=="__main__":
    trackPrice()
    driver.quit()
