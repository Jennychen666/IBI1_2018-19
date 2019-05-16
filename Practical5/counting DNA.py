# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:53:10 2019

@author: admin
"""

sequence=input("Please enter a DNA sequence:", )
#the code was amended to  have a prompt for users and word without spaces
myDirt={}
for word in sequence:
    if word in myDirt:
        myDirt[word]+=1
    else:
        myDirt[word]=1
print(myDirt)

import matplotlib.pyplot as plt
labels='A','T','G','C'
sizes=tuple(myDirt.values())
explode=(0.1,0,0,0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',
        shadow=True,startangle=90)
ax1.axis('equal')
plt.show()

        



