# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:53:10 2019

@author: admin
"""
#the user should give a DNA string of length
sequence=input("Please enter a DNA sequence:", )
#count the respective number of times that the symbols 'A', 'C', 'G', and 'T' 
#Create a frequency dictionary mapping str:int 
myDirt={}
#set the loop to search the sequence
for word in sequence:
    if word in myDirt:
        myDirt[word]+=1
    else:
        myDirt[word]=1
#show the numebers of four nucleotides
print(myDirt)
#construct a pie from the data
import matplotlib.pyplot as plt
labels='A','T','G','C'
sizes=tuple(myDirt.values()) 
explode=(0.1,0,0,0)   #the part of 'A' will be seperated from the pie chart a bit
fig1, ax1 = plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',
        shadow=True,startangle=90)
ax1.axis('equal')
plt.show()

        



