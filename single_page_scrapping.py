from bs4 import BeautifulSoup
import requests
from datetime import datetime



# page = 'https://www.kalerkantho.com/print-edition/sports/2022/01/25/1114003'
page = 'https://www.kalerkantho.com/print-edition/news/2022/01/25/1114116'

response = requests.get(page)
soup = BeautifulSoup(response.content, 'html.parser')
title_text = soup.find('div',{'class':'col-sm-12 col-md-8 details'}).h2
print("TITLE ",title_text.text)
main_text= soup.find('div',{'class':'some-class-name2'}).findAll('p')
for i in main_text:
    print(i.text)

# print(main_text) # >>> not efficient

date = datetime.now().date()
