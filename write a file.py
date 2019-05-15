# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:45:07 2019

@author: admin
"""

fout = open('myfile.txt','w') 
line1 = 'Lecture 6.2\n' 
line2 = 'File Operation\n' 
fout.write(line1) 
fout.write(line2) 
fout.close() 