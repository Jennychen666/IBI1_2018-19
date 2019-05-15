# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:51:05 2019

@author: admin
"""

#start with a number no larger than 8192
x=int(input('Please input a number no larger than 8192:', ))
#set the cumulative result
r=str(x)+ " is "
#set the loop
while x>=1:
    i=0
    while 2**i<=x:
        i+=1
    i=i-1
    r=r+"2**"+str(i)+"+"
    x=x-2**i
#remove the "+" at the end of the result
    r1=r[:-1]
#print the final result
print(r1)