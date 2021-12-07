from bs4 import BeautifulSoup
import requests
import pandas as pd

page = "https://www.kalerkantho.com/"
response = requests.get(page)
print(response.status_code)
soup = BeautifulSoup(response.content,'html.parser')

# nav = soup.find('div', {'class': 'new-nav'})
nav = soup.find('nav', {'class':'row'})
# print(nav)

urls, urltexts = [],[]

for i in nav.find_all('a'):
    if i.get('href')[:5] == 'https':
        urls.append(i.get('href'))
        urltexts.append(i.text)



############## to see all the urls from the navbar #############
# print('urls are printing \n\n\n')
# for i,j in enumerate(urls):
#     print(i,j)
# print(len(urls))
########################################################

page_keys = ['first-page', 'last-page', 'sports', 'news', 'education', 'industry-business', 'deshe-deshe',
'priyo-desh', 'oboshore', 'islamic-life', 'editorial', 'sub-editorial', 'rangberang', 'feature']

page_names={}

for i in page_keys:
    page_names[i] = []


for i in range(len(urls)):
    tmp = urls[i].split('/')
    if tmp[3] == 'print-edition':
        if tmp[4] in page_names:
            page_names[tmp[4]].append(urltexts[i])

    if tmp[3] == 'feature':
            page_names[tmp[3]].append(urltexts[i])

for i,j in enumerate(page_names.items()):
    print(i,j) 


# for i in urls[:20]:
#     tmp = requests.get(i)
#     print(tmp.status_code)

# x = pd.DataFrame(page_names)
# print(x.head)