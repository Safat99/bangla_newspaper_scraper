from bs4 import BeautifulSoup
import requests
from datetime import datetime
import csv
import os

page = 'https://www.kalerkantho.com/print-edition/rangberang/2022/02/04/1117128'
# page = 'https://www.kalerkantho.com/print-edition/education/2022/02/04/1117186'
# page = 'https://www.kalerkantho.com/print-edition/news/2022/01/25/1114116'


def extracting_paragraph(page):
	page = page
	response = requests.get(page)
	soup = BeautifulSoup(response.content, 'html.parser')
	title_text = soup.find('div',{'class':'col-sm-12 col-md-8 details'})
	if title_text is not None:
		title_text = title_text.h2.text
		main_text= soup.find('div',{'class':'some-class-name2'}).findAll('p')
		paragraph = ''

		for i in main_text:
    		# print(i.text)
			paragraph += i.text
	else:
		title_text = 'Nothing'
		main_text = 'Nothing'
		paragraph = 'Nothing'	


	fields = ['Date', 'Category', 'Headline', 'Paragraph']
	date = str(datetime.now().date())
	main_dict = {'Date': date, 'Headline': title_text, 'Category': page.split('/')[4], 'Paragraph': paragraph}

	file_name = 'news.csv'
	file_exists = os.path.isfile(file_name)

	with open(file_name, 'a' , newline = '') as csvfile:
		csvwriter = csv.DictWriter(csvfile, fields)
		if not file_exists:
			csvwriter.writeheader()
		csvwriter.writerow(main_dict)


if __name__=='__main__':
	extracting_paragraph(page)