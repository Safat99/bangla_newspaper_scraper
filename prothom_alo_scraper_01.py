from bs4 import BeautifulSoup
import requests
import os
import webbrowser

page = 'http://www.prothom-alo.com/'
result = requests.get(page)

if result.status_code != 200:
    print("not connected")
    exit()

soup = BeautifulSoup(result.content, 'html.parser')


##################### for seeing all the links ########################
urls = soup.findAll('a')
links_text = [i.text for i in urls]
links = [i.get('href') for i in urls]
# for i in range(len(links)):
#     print(links_text[i], links[i])

last_link = links[-2]
print(last_link)
response = requests.get(last_link)
if response.status_code == 200:
    print('connected')

# path = os.path.abspath('temp.html')
# with open(path,'w') as file:
#     tmp_soup = BeautifulSoup(response.content,'html.parser')
#     file.write(str(tmp_soup))
#     print(str(tmp_soup))
# webbrowser.open(file)

# div = soup.findAll('div', {'class': 'container'})
# print(div.at)

