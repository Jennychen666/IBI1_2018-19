# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:35:05 2019

@author: admin
"""


import xml.dom.minidom
import re
import pandas as pd

filePath=r'C:/Users/admin/Desktop/IBI/IBI1_2018-19/week8/practical 8';  #Your file path
fileName='go_obo.xml';
resName='autophagosome2.xlsx'
file=filePath+'/'+fileName
res=filePath+'/'+resName

re_immu = re.compile(r'autophagosome')
#Function to find childnodes 
def Child(id, resultSet):
    for t in go:
        parents = t.getElementsByTagName('is_a')
        geneid = t.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data == id:
                resultSet.add(geneid)
#                don't use resultSet = resultSet | set([geneid])
#                otherwise you will create a new set instead of modifying the existing one
#                print (resultSet)
                Child(geneid, resultSet)
                
#create a pandas.Dataframe to store the output
df = pd.DataFrame(columns=['id','name','definition','childnodes'])

#create the DOM tree    
DOMTree = xml.dom.minidom.parse('go_obo.xml') 
obo = DOMTree.documentElement
go = obo.getElementsByTagName('term')
for term in go:
    defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    #find terms that contain the word 'autophagosome'
    if re_immu.search(defstr):
        id = term.getElementsByTagName('id')[0].childNodes[0].data
        name = term.getElementsByTagName('name')[0].childNodes[0].data
        resultSet = set()
        Child(id, resultSet)
        df = df.append(pd.DataFrame({'id':[id],'name':[name],'definition':[defstr],'childnodes':[len(resultSet)]})) 
        print(id, len(resultSet))
#save to excel
df.to_excel(res,index=False)