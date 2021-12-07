from bs4 import BeautifulSoup
import requests
import os
import webbrowser

# page = 'http://www.prothom-alo.com/'
page = 'https://www.prothomalo.com/sports'
result = requests.get(page)

if result.status_code != 200:
    print("not connected")
    exit()
else:
    print('successfully connected!!!\n')

soup = BeautifulSoup(result.text, 'html5lib')

h2 = soup.find('div', id='container')
for i in h2:
    print(i.text)


##################### for seeing all the links ########################
# urls = soup.findAll('a')
# links_text = [i.text for i in urls]
# links = [i.get('href') for i in urls]
# for i in range(len(links)):
#     print(links_text[i], links[i])
################################################################################
