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

csv_file=open('D:/Work/BTP/Extracted Data/Data/10-08-20/India_today.csv','a+')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Date','Time','Headline','Keywords'])

dicts={}


#adding headlines to dictionary
# csv_file=open("D:/Work/BTP/Extracted Data/Data/10-08-20/India_today.csv",'r')
# file=csv.reader(csv_file)

# lines=len(list(file))
# print(lines)

# df=pd.read_csv("D:/Work/BTP/Extracted Data/Data/08-08-20/India_today.csv")

# for i in range(1,lines,2):
# 	Headline=df["Headline"][i] 
# 	dicts[Headline]=1

# csv_writer.writerow(['','','',''])

# Extraction
sports=["cricket","football","tennis","badminton","athletics","hockey","other-sports"]
for i in range(0,7):
	print(sports[i])
	source=requests.get("https://www.indiatoday.in/sports/"+sports[i]).text
	soup=BeautifulSoup(source,'lxml')

	for a1 in soup.find_all('div',class_='detail'):
		a=a1.find('a')
		link=str(a.attrs['href'])
		print(link)
		headline=a.text
		print(headline)
		if headline not in dicts.keys():
			dicts[headline]=1
			source1=requests.get("https://www.indiatoday.in"+link).text
			soup1=BeautifulSoup(source1,'lxml')
			try:
				keyword=soup1.find('meta',attrs={'name':'news_keywords'})
				data_keywords=str(keyword.attrs['content'])
				data_keywords=data_keywords.replace(',','')
			except:
				data_keywords=""	

			print(data_keywords)
			print()
			
			csv_writer.writerow([today,current_time,headline,data_keywords])
		else:
			continue;	

csv_file.close()		


