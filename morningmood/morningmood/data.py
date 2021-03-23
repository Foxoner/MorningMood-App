from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import psycopg2
import datetime
# instead of module fortune, place code here
import csv
import random

fileName = r'F:\Developing\PortfolioUsefulThings\FortuneCookieFortunes.txt'
with open(fileName, 'r') as f:
    reader = csv.reader(f)
    allRows = list(reader)
day_fortune = random.choice(allRows)[0]
# end of module fortune

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

url1 = 'https://coinmarketcap.com/currencies/bitcoin/markets/'
url2 = 'https://coinmarketcap.com/currencies/ethereum/'
url3 = 'https://bitstat.top/fear_greed.php'
url4 = 'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2'

source = [{'url': url1, 'class': '.priceValue___11gHJ'},
          {'url': url2, 'class': '.priceValue___11gHJ'},
          {'url': url3, 'class': '#fgi_textfield'},
          {'url': url4, 'class': '.today-temp'},
          {'url': url4, 'class': '.description'}]

list1 = []


def scrape(source):
    for i in source:
        driver.get(i['url'])
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        text = soup.select(i['class'])
        for idx, item in enumerate(text):
            title = item.get_text()
            list1.append(title)

    driver.close()

    


scrape(source)

text_btc = list1[0]
text_eth = list1[1]
text_index = list1[2]
text_temperature = list1[3]
text_weather = list1[4]
datetime = datetime.datetime.today()

print(text_btc, text_eth, text_index, text_temperature, text_weather, day_fortune, datetime)

con = psycopg2.connect(
    database='morning_mood',
    user='project_manager',
    password="123456",
    host="127.0.0.1",
    port="5432"
)

cur = con.cursor()
cur.execute(
    "INSERT INTO mainpage_information (cur_date,btc,eth,index,temperature,weather,fortune) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(
        datetime,
        text_btc,
        text_eth,
        text_index,
        text_temperature,
        text_weather,
        day_fortune)
)

con.commit()
print("Records inserted successfully")

con.close()
