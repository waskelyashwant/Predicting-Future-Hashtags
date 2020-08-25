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

csv_file=open('D:/Work/BTP/Extracted Data/Data/10-08-20/ESPN.csv','a+')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Date','Time','Headline','Keywords'])

dicts={}


#adding headlines to dictionary
# csv_file=open("D:/Work/BTP/Extracted Data/Data/08-08-20/ESPN.csv",'r')
# file=csv.reader(csv_file)

# lines=len(list(file))
# print(lines)

# df=pd.read_csv("D:/Work/BTP/Extracted Data/Data/08-08-20/ESPN.csv")

# for i in range(1,lines,2):
# 	Headline=df["Headline"][i] 
# 	dicts[Headline]=1

# csv_writer.writerow(['','','',''])

sports=["cricket","football","tennis","badminton","athletics","hockey","nba","wwe"]

for i in range(0,8):
	print(sports[i])
	source = requests.get("https://www.espn.in/"+sports[i]).text
	soup = BeautifulSoup(source, 'lxml')

	for soup1 in soup.find_all('section',class_='contentItem__content--story'):
		soup2=soup1.find('div',class_='contentItem__titleWrapper')
		link1=soup1.find('a')
		link2=str(link1.attrs['href'])
		heading=soup2.find('h1',class_='contentItem__title--story')
		headline=heading.text
		print(link2)
		print(headline)
		if headline not in dicts.keys():
			try:
				source1 = requests.get("https://www.espn.in"+link2).text
				soup1 = BeautifulSoup(source1, 'lxml')
				try:
					keyword = soup1.find('meta',attrs={'name':'news_keywords'})
					data_keywords = str(keyword.attrs['content'])
					data_keywords=data_keywords.replace(',','')
					print(data_keywords)
					csv_writer.writerow([today,current_time,headline,data_keywords])
				except:
					pass	
			except:
				pass
		else:
			continue		
		
		print()

csv_file.close()		