# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:51:05 2019

@author: admin
"""

# starts with some number x  no larger than 8192
x=int(input('Please input a number no larger than 8192:', ))
#set the cumulative result
r=str(x)+ " is "
#set the loop
while x>=1:
    i=0 #stands for the exponent
    while 2**i<=x:
        i+=1
    i=i-1
    r=r+"2**"+str(i)+"+"
    x=x-2**i
#remove the "+" at the end of the result
    r1=r[:-1]
#output a sentence that gives the binary composition of x. 
print(r1)