# -*- coding: utf-8 -*-
"""
Created on Fri May 17 02:49:14 2019

@author: admin
"""
import os
os.chdir('C:/Users/admin/Desktop/IBI/IBI1_2018-19/Practical13')

def xml_to_cps():

    import os
    import xml.dom.minidom

    # first, convert xml to cps 
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
    # now comes the painful part. Just copy and paste this ok
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
                
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    cpsFile = open("predator-prey.cps","w",encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()
y=xml_to_cps() 

import re
import numpy
#open the result file
file=open('modelResults.csv','r')
file1=file.readlines()
#change the lines into arrays
data=[]
names=[]
count=0
for line in file1:
    if count==0:
        names=re.split(r',+',line)
        count=1
    else:
        r=re.split(r',+',line)
        del(r[0])# remove 'A','B' in the first line 
        data.append(r)
        
results=numpy.array(data)
results=results.astype(numpy.float)
#print(results)


import matplotlib.pyplot as plt
plt.figure(figsize=(6,4),dpi=150)
#plot a time course of the population
plt.plot(results[:,0],label='Predator (b=0.02,d=0.4)')
plt.plot(results[:,1],label='Prey (b=0.1,d=0.02)')
plt.xlabel('time')
plt.ylabel('population size')
plt.title('Time Course')
plt.legend(loc='upper right')#make the location of label on the upper right 

#plots predator population against prey population
plt.figure(figsize=(6,4),dpi=150)
plt.xlabel("predator(b=0.02.d=0.4)")
plt.ylabel("prey(b=0.1,d=0.02)")
plt.title('Limit cycle')
plt.plot(results[:,0],results[:,1])

#define the four rate parameters
#pick one number between 0 to 1 for each
#import xml.dom.minidom.Change parameters.Save again

#import numpy.Randomly pick numbers.
#set while loops
#import matplotlib for plots.
    
    
    
    
    
