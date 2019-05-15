# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:06:35 2019

@author: admin
"""
import re
from fractions import Fraction
#The input numbers must be interger between 1 and 23
test = re.compile(r'(^[1-9]$)|(^1[0-9]$)|(^2[0-3]$)')
num = input('Please input numbers to computer 24:(use \' \' to divide them)\n', )
numList = num.split(' ')
for i in numList:
    if test.match(i): 
      continue
    else: 
      print('The input number must be intergers from 1 to 23')
      break
#turn tuple() into lists[] to change the values
num = list(map(int,numList))  
count = 0 
def dfs(n):
    global count
    count = count +1
#n is len(num) 
    if n == 1:
        if(int(num[0])==24):
            return 1
        else:
            return 0
    #select two different numbers
    for i in range(0,n):
        for j in range(i+1,n):
            a = num[i]
            b = num[n-1]  #b=num[j]
            
            num[i] = a+b
            if(dfs(n-1)):
                return 1
            
            num[i] = a-b
            if(dfs(n-1)):
                return 1  
            
            num[i] = b-a
            if(dfs(n-1)): 
                return 1 
            
            num[i] = a*b
            if(dfs(n-1)): 
                return 1  
            
            if a:
                num[i] = Fraction(b,a)
                if(dfs(n-1)): 
                    return 1    
            if b:
                num[i] = Fraction(a,b)
                if(dfs(n-1)): 
                    return 1 
              #Backtracking  
            num[i] = a
            num[j] = b
    return 0 

if (dfs(len(num))): 
    print('Yes')
else: 
    print('No')
print('Recursion times is ',count)

