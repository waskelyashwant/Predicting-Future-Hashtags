import pandas as pd
import numpy as np
import csv

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import cluster


stemmer=PorterStemmer()

sw=stopwords.words('english')
# print(sw)

def tokenizer(keyword):
	return [stemmer.stem(w) for w in keyword.split(' ')]

# keywords={'campaign building',
#           'ppc campaign generator',
#           'how to build ppc campaigns',
#           'how do you group keywords',
#           'how to group keywords',
#           'keyword grouper',
#           'keyword grouping software',
#           'ppc campaign builder',
#           'best software to group keywords','tokyo','Amritsar Punjab','punjab','Japan tokyo'}

keywords=[]

##############   TOI  ################

file1=open("D:/Work/BTP/Extracted Data/Data/09-08-20/toidata.csv")
reader1=csv.reader(file1)
lines1=len(list(reader1))
print(lines1)

with open("D:/Work/BTP/Extracted Data/Data/09-08-20/toidata.csv", encoding='utf-8', errors='ignore') as file1:
	df1=pd.read_csv(file1)
	for i in range(1,lines1,2):
		keywords.append(df1["Keywords"][i])


#############   YAHOO NEWS  ################

file2=open("D:/Work/BTP/Extracted Data/Data/09-08-20/yahoonews_data.csv",encoding="utf-8", errors='ignore')
reader2=csv.reader(file2)
lines2=len(list(reader2))
print(lines2)

df2=pd.read_csv("D:/Work/BTP/Extracted Data/Data/09-08-20/yahoonews_data.csv")
for i in range(1,lines2,2):
     keywords.append(df2["Keywords"][i])


#############   ESPN  ################

file3=open("D:/Work/BTP/Extracted Data/Data/09-08-20/ESPN.csv")
reader3=csv.reader(file3)
lines3=len(list(reader3))     
print(lines3)

with open("D:/Work/BTP/Extracted Data/Data/09-08-20/ESPN.csv", encoding='utf-8', errors='ignore') as file3:
	df3=pd.read_csv(file3)
	for i in range(1,lines3,2):
		keywords.append(df3["Keywords"][i])


##############   INDIA TODAY  ################

file4=open("D:/Work/BTP/Extracted Data/Data/09-08-20/India_today.csv")
reader4=csv.reader(file4)
lines4=len(list(reader4))     
print(lines4)

with open("D:/Work/BTP/Extracted Data/Data/09-08-20/India_today.csv", encoding='utf-8', errors='ignore') as file4:
	df4=pd.read_csv(file4)
	for i in range(1,lines4,2):
		keywords.append(df4["Keywords"][i])


# print(keywords)     

key_len=len(keywords)

for i in range(0,key_len):
     keywords[i]=keywords[i].title()

tfidf=TfidfVectorizer(tokenizer=tokenizer, stop_words=sw)
X=pd.DataFrame(tfidf.fit_transform(keywords).toarray(), columns=tfidf.get_feature_names())
# # print(a)

c=cluster.KMeans(45)
a=c.fit_predict(X)
print(a)
b=len(a)
print(b)

X['pred']=c.fit_predict(X)
# print(X['pred'])

X['keywords']=keywords
# print(X.loc[0]['keywords'])
print(X)
d=0
for i in range(0,b):
     d=max(d,X['pred'][i])


for i in range(0,b):
     for j in range(0,d+1):
          if X['pred'][i]==j:
               with open("D:/Work/BTP/Extracted Data/Data/09-08-20/"+str(j) +".txt","a+", encoding='utf-8') as f:
               	  f.write(X['keywords'][i]+'\n')
               	  f.close()
# X.to_csv('f5.csv')