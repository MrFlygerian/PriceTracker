from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')

driver = webdriver.Chrome(options=options,
                          executable_path=r"C:\Users\bless\chromedriver_win32\chromedriver")

catagories = ['https://www.amazon.co.uk/s?rh=n%3A468292%2Cp_72%3A4-&pf_rd_i=468292&pf_rd_p=d40c144e-45ba-5915-b01d-d92bd82e9a59&pf_rd_r=FJ0A45QRDQZA88E0QYEE&pf_rd_s=merchandised-search-11&pf_rd_t=BROWSE&ref=Oct_s9_apbd_otopr_hd_bw_b1xp6_S',
              'https://www.amazon.co.uk/luxury-skin-care/b/ref=lux_leftnav_skincare?ie=UTF8&node=3419776031&pf_rd_m=A3P5ROKL5A1OLE&pf_rd_s=merchandised-search-leftnav&pf_rd_r=VYF39KRJ0JW6YR3KVNDB&pf_rd_r=VYF39KRJ0JW6YR3KVNDB&pf_rd_t=101&pf_rd_p=deb905d7-a282-4712-921a-1ecda19b9d3c&pf_rd_p=deb905d7-a282-4712-921a-1ecda19b9d3c&pf_rd_i=3411821031',
              'https://www.amazon.co.uk/b/?node=300703&ref=gwrd_holiday_en&pf_rd_r=T83VCSE85WKRFK256F3W&pf_rd_p=0b4a9d3b-048e-4cd4-918b-36a69cc2ad5d']

driver.get(catagories[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')

links = [link.get('href') for link in soup.find_all('a') if link.get('href') != None and link.get('href').startswith('/')]
page_links = [f'https://www.amazon.com{link}' for link in links]
#print(page_links)
     


def scrape_prod_page(URL, title_lookup = 'productTitle', price_lookup = 'priceblock_ourprice'):
    time.sleep(1.1)
    driver.get(URL)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    title = soup.find(id=title_lookup).get_text().strip()
    price = soup.find(id=price_lookup).get_text()
    driver.quit()
    return title, price


for link in page_links:
    title, price = None, None
    try:
        title, price = scrape_prod_page(link)
    except:
        pass
    if title != None and price != None:
        print (title, price, link)

