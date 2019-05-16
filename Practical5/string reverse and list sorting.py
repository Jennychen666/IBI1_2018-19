# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:03:34 2019

@author: admin
"""
#improvements:ask the user for an input string, instead of hard-coding the string in the script.
sequence=str(input('Please input a string:',))
#reverse the order
#use split() to get words from a string
sequence=sequence[ ::-1]
sequence=sequence.split(" ")

sequence.sort()
sequence.reverse()
print(sequence)
