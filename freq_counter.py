from collections import Counter
import csv
import re

def word_count(filename):
	with open(filename) as f:
		return Counter(f.read().split(" "))
  

dictionary1={}
dictionary2={}
dictionary3={}
dictionary4={}

dictionary4321={}
dictionary432={}
dictionary43={}
dictionary44={}

for i in range(0,45):
	text = open("D:/Work/BTP/Extracted Data/Data/06-08-20/"+str(i)+".txt",'r')
	count=0
	d={}
	string=''
	for line in text: 
		line = line.strip()
		line = line.lower() 

		words = line.split(" ") 
		for word in words: 
			if word in d: 
				d[word] = d[word] + 1
			else:
				d[word]=1

	for j in d:
		if d[j]>=count:
			count=d[j]
			string=j

	if string not in dictionary1:
		dictionary1[string]=count
	else:
		dictionary1[string]=dictionary1[string]+count		


# for i in range(0,45):
# 	counter=word_count("D:/Work/BTP/Extracted Data/Data/05-08-20/"+str(i)+".txt")
# 	count=0
# 	string=""
# 	for j in counter:
# 		if counter[j]>=count:
# 			count=counter[j]
# 			string=j;

# 	if string not in dictionary2:
# 		dictionary2[string]=count
# 	else:
# 	    dictionary2[string]=dictionary2[string]+count		

for i in range(0,45):
	text = open("D:/Work/BTP/Extracted Data/Data/07-08-20/"+str(i)+".txt",'r')
	count=0
	d={}
	string=''
	for line in text: 
		line = line.strip()
		line = line.lower() 

		words = line.split(" ") 
		for word in words: 
			if word in d: 
				d[word] = d[word] + 1
			else:
				d[word]=1

	for j in d:
		if d[j]>=count:
			count=d[j]
			string=j

	if string not in dictionary2:
		dictionary2[string]=count
	else:
		dictionary2[string]=dictionary2[string]+count		


# for i in range(0,45):
# 	counter=word_count("D:/Work/BTP/Extracted Data/Data/06-08-20/"+str(i)+".txt")
# 	count=0
# 	string=""
# 	for j in counter:
# 		if counter[j]>=count:
# 			count=counter[j]
# 			string=j;

# 	if string not in dictionary3:
# 		dictionary3[string]=count
# 	else:
# 	    dictionary3[string]=dictionary3[string]+count	

for i in range(0,45):
	text = open("D:/Work/BTP/Extracted Data/Data/08-08-20/"+str(i)+".txt",'r')
	count=0
	d={}
	string=''
	for line in text: 
		line = line.strip()
		line = line.lower() 

		words = line.split(" ") 
		for word in words: 
			if word in d: 
				d[word] = d[word] + 1
			else:
				d[word]=1

	for j in d:
		if d[j]>=count:
			count=d[j]
			string=j

	if string not in dictionary3:
		dictionary3[string]=count
	else:
		dictionary3[string]=dictionary3[string]+count

# for i in range(0,45):
# 	counter=word_count("D:/Work/BTP/Extracted Data/Data/07-08-20/"+str(i)+".txt")
# 	count=0
# 	string=""
# 	for j in counter:
# 		if counter[j]>=count:
# 			count=counter[j]
# 			string=j;

# 	if string not in dictionary4:
# 		dictionary4[string]=count
# 	else:
# 	    dictionary4[string]=dictionary4[string]+count

for i in range(0,45):
	text = open("D:/Work/BTP/Extracted Data/Data/09-08-20/"+str(i)+".txt",'r')
	count=0
	d={}
	string=''
	for line in text: 
		line = line.strip()
		line = line.lower() 

		words = line.split(" ") 
		for word in words: 
			if word in d: 
				d[word] = d[word] + 1
			else:
				d[word]=1

	for j in d:
		if d[j]>=count:
			count=d[j]
			string=j

	if string not in dictionary4:
		dictionary4[string]=count
	else:
		dictionary4[string]=dictionary4[string]+count


print("dictionary1: ")
print(dictionary1)
print()
print("dictionary2")
print(dictionary2)
print()
print("dictionary3")
print(dictionary3)
print()
print("dictionary4")
print(dictionary4)
print()

for i in dictionary4:
	if i in dictionary3.keys():
		if i in dictionary2.keys():
			if i in dictionary1.keys():
				if i not in dictionary4321:
					dictionary4321[i]=dictionary1[i]+dictionary2[i]+dictionary3[i]+dictionary4[i]
				else:
					dictionary4321[i]+=dictionary1[i]+dictionary2[i]+dictionary3[i]+dictionary4[i]
			else:
				if i not in dictionary432:
					dictionary432[i]=dictionary4[i]+dictionary2[i]+dictionary3[i]
				else:
					dictionary432[i]+=dictionary4[i]+dictionary2[i]+dictionary3[i]	  
		else:
			if i not in dictionary43:
				dictionary43[i]=dictionary3[i]+dictionary4[i]
			else:
				dictionary43[i]+=dictionary3[i]+dictionary4[i]
	else:
	    dictionary44[i]=dictionary4[i]			



# for i in dictionary2:
# 	if i not in dictionary1.keys():
# 		if i in dictionary3.keys():
# 			if i not in dictionary23:
# 				dictionary23[i]=dictionary2[i]+dictionary3[i]
# 			else:
# 				dictionary23[i]+=dictionary2[i]+dictionary3[i]	


sports = {'tennis':1,'cricket':5,'football':2,'nba':6, 'basketball':45, 'wwe':5, 'badminton':44, 'news':55, 'hockey':45, 'athletics':22, '':5}
for i in sports:
	if i in dictionary4321.keys():
		dictionary4321.pop(i)
	if i in dictionary432.keys():
		dictionary432.pop(i)
	if i in dictionary43.keys():
		dictionary43.pop(i)
	if i in dictionary4321.keys():
		dictionary44.pop(i)			

print("dictionary4321:")
print(dictionary4321)		
print()
print("dictionary432:")
print(dictionary432)		
print()	
print("dictionary43:")
print(dictionary43)		
print()
print("dictionary4:")
print(dictionary44)