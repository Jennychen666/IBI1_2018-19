# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:09:04 2019

@author: admin
"""
# starts with a positive integer n and computes and displays the Collatz sequence of n 
n=int(input("Please input a positive integer:", ))
#the sequence ends when reaching 1 for the ﬁrst time
while n!=1: 
#dividing by 2 (if n is even) 
 if n%2 == 0:
    n=int(n/2) #show integers insread of floats,add code int()
#multiplying by 3 and adding 1 (if n is odd)
 else: 
    n=int(n*3+1)
#output the result
 print(n)


    
       
    