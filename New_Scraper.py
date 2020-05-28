import requests
from bs4 import BeautifulSoup
import html5lib
from selenium import webdriver
URL = 'https://www.amazon.co.uk/LG-Electronics-32LM630BPLA-AEK-32-Inch-Freeview/dp/B07RT5FJL8/ref=psdc_560864_t1_B07ZQK89GJ'

title_lookup = 'productTitle'
price_lookup = 'priceblock_ourprice'


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')

driver = webdriver.Chrome(options=options,
                          executable_path=r"C:\Users\bless\chromedriver_win32\chromedriver")
driver.get(URL)
soup = BeautifulSoup(driver.page_source, 'html.parser')
title =soup.find(id = title_lookup).get_text().strip()
price = soup.find(id = price_lookup).get_text()
driver.quit()
print(title, price)
