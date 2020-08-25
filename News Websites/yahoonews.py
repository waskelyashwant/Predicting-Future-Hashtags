from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import time 

from datetime import datetime
from datetime import date


now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M:%S")

print("Current Time =", current_time)
print("Today's date:", today)

csv_file=open('D:/Work/BTP/Extracted Data/Data/10-08-20/yahoonews_data.csv','a+',encoding="utf-8")
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Date','Time','Headline','Keywords'])

dicts={}

# adding headlines to dictionary
# csv_file=open("D:/Work/BTP/Extracted Data/Data/10-08-20/yahoonews_data.csv",'r')
# file=csv.reader(csv_file)

# lines=len(list(file))
# print(lines)

# df=pd.read_csv("D:/Work/BTP/Extracted Data/Data/10-08-20/yahoonews_data.csv")

# for i in range(1,lines,2):
# 	Headline=df["Headline"][i] 
# 	dicts[Headline]=1

# csv_writer.writerow(['','','',''])

source= requests.get('https://in.news.yahoo.com/sports').text
soup=BeautifulSoup(source,'lxml')

y0=soup.find('div',attrs={'id':'Main'})
for y1 in y0.find_all('ul',class_='My(0) Ov(h) P(0) Wow(bw)'):
		for y2 in y1.find_all('li'):
			y3=y2.find('h3')
			y4=y3.find('a')
			headline=y4.text
			print(headline)
			# encoded=headline.encode('cp1252')
			# headline=encoded.decode('utf-8')
			if headline not in dicts.keys():
				link=str(y4.attrs['href'])
				source1=requests.get('https://in.news.yahoo.com'+link).text
				soup1=BeautifulSoup(source1,'lxml')
				try:
					keyword=soup1.find('meta',attrs={'name':'news_keywords'})
					data_keywords=str(keyword.attrs['content'])
					data_keywords=data_keywords.replace(',','')
					print(data_keywords)
					csv_writer.writerow([today,current_time,headline,data_keywords])	
				except:
					data_keywords=""	

				print()
			else:
				continue

csv_file.close()