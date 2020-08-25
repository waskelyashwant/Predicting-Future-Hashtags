from bs4 import BeautifulSoup
import requests
import csv
import time 
import pandas as pd

from datetime import datetime
from datetime import date

now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M:%S")

print("Current Time =", current_time)
print("Today's date:", today)

source=requests.get('https://timesofindia.indiatimes.com/sports').text

soup=BeautifulSoup(source,'lxml')


csv_file=open('D:/Work/BTP/Extracted Data/Data/10-08-20/toidata.csv','a+')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['date','Time','Headline','Keywords'])


dicts={}

#adding headlines to dictionary
# csv_file=open("D:/Work/BTP/Extracted Data/Data/10-08-20/toidata.csv",'r')
# file=csv.reader(csv_file)

# lines=len(list(file))
# print(lines)

# df=pd.read_csv("D:/Work/BTP/Extracted Data/Data/10-08-20/toidata.csv",encoding='windows-1252')

# for i in range(1,lines,2):
# 	Headline=df["Headline"][i] 
# 	dicts[Headline]=1

# csv_writer.writerow(['','','',''])



anchor1=soup.find_all('div',class_='news-section clearfix')
b=len(anchor1)

for i in range(1,b):
	for anchor3 in anchor1[i].find_all('span',class_='w_tle'):
		links=anchor3.find('a')
		headline=links.text
		print(headline)
		if headline not in dicts.keys():
			link=str(links.attrs['href'])
			if link[0]!='h':
				source1=requests.get('https://timesofindia.indiatimes.com'+link).text
			else:
				source1=requests.get(link).text	
			soup1=BeautifulSoup(source1,'lxml')
			try:
				keyword=soup1.find('meta',attrs={'name':'keywords'})
				data_keywords=str(keyword.attrs['content'])
				data_keywords=data_keywords.replace(',',' ')
				print(data_keywords)
				csv_writer.writerow([today,current_time,headline,data_keywords])
			except:
				pass
		else:
		    continue		

		print()    



for a1 in soup.find_all('div',class_='section_wdgt clearfix'):
	for a3 in a1.find_all('span',class_='w_tle'):
		links=a3.find('a')
		headline=links.text
		print(headline)
		if headline not in dicts.keys():
			link=str(links.attrs['href'])
			source1=requests.get('https://timesofindia.indiatimes.com'+link).text
			soup1=BeautifulSoup(source1,'lxml')
			try:
				keyword=soup1.find('meta',attrs={'name':'keywords'})
				data_keywords=str(keyword.attrs['content'])
				data_keywords=data_keywords.replace(',',' ')
				print(data_keywords)
				csv_writer.writerow([today,current_time,headline,data_keywords])
			except:
			    pass	
		else:
		    continue		

		print()


csv_file.close()