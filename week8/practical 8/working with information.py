# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:15:15 2019

@author: admin
"""
import re
import pandas as pd
from xml.dom.minidom import parse
import xml.dom.minidom
# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
genes= collection.getElementsByTagName("term")

re_immu = re.compile(r'autophagosome')

df = pd.DataFrame(columns=['id','name','definition','childnodes'])
#Function to find childnodes 
def Child(id, resultSet):
    for t in genes:
        parents = t.getElementsByTagName('is_a')
        geneid = t.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data == id:
                resultSet.add(geneid)
                Child(geneid, resultSet)
for term in genes:
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
df.to_excel('C:/Users/admin/Desktop/IBI/IBI1_2018-19/week8/')
   



