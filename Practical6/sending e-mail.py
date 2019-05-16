# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:28:59 2019

@author: admin
"""

import re
from email.header import Header
from email.mime.text import MIMEText
import smtplib

fpath = 'C:/Users/admin/Desktop/IBI/IBI1_2018-19/Practical6'#input your file path

#my email address list
lname='address_information.csv'
lfile=fpath+'/'+lname
#the body file
bname = 'body.txt'
bfile = fpath+'/'+bname
#regex precompile
re_email = re.compile(r'^[0-9A-Za-z_]+@[0-9A-Za-z_]+(\.[0-9A-Za-z_]+)+$')
re_loginname = re.compile(r'(\S+)@')

############TEST THE ADDRESS############
with open(lfile, 'r') as info:
    info = info.read()
all = re.split(r'[,\n]',info) 
mList = []
for i in range(0,len(all),3):
    mList.append((all[i],all[i+1],all[i+2]))
#filter the wrong address    
filter_list = mList[1:]    
for i in range(1,len(mList)):
    if re_email.match(mList[i][1]):
        print(mList[i][1],':Correct Address！')
    else: 
        print(mList[i][1],':Wrong Address！')
        filter_list.remove(mList[i])
        
############SEND THE EMAIL############
with open(bfile, 'r') as rbody:     
    rbody = rbody.read()
   
from_addr = input('From: ')
password = input('Password: ')
    
for char in filter_list:
    to_addr = char[1]
    subject = char[2]
    #for different users, change salutation
    body = re.sub('User',char[0],rbody)
    loginname = re_loginname.search(from_addr).group(1)
    Your_name = 'Jenny'
    from_name = Header(Your_name,'utf-8')
    from_name.append(from_addr,'ascii')
    to_name = Header(char[0],'utf-8')
    to_name.append(to_addr,'ascii')
    
    msg = MIMEText(body,'plain','utf-8')
    msg['From'] = from_name
    msg['To'] = to_name
    msg['Subject'] = Header(subject,'utf-8')
    
    try:
        server = smtplib.SMTP('smtp.zju.edu.cn',25)
        server.login(loginname, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print('Mail sent successfully!')
    except smtplib.SMTPException:
        print('Mail delivery failed')