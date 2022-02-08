from logging import exception
from bs4 import BeautifulSoup
import requests
import os
from single_page_scrapping import extracting_paragraph

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
            page_names[tmp[4]].append(urls[i])
        
    if tmp[3] == 'feature':
        page_names[tmp[3]].append(urls[i])

########## for showing all the pages and links ###########
# for i,j in enumerate(page_names.items()):
#     print(i,j)
#############################

count =0
for i in page_names.values():
    for j in i:
        try:
            extracting_paragraph(j)
            count +=1
            print(count,"links extracted")
        except Exception as e:
            print("error occured")
            print(e)
            continue


##############
output_folder = 'outputs/'
def file_sorting():
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    os.chdir(output_folder)
    for i in page_names.keys():
        if not os.path.exists(i):
            os.mkdir(i)
        else:
            os.chdir(i)
########################
