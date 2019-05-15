# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:02:59 2019

@author: admin
"""
import re
from email.mime.text import MIMEText
from email.header import Header
import smtplib
# 第三方 SMTP 服务
xfile = open('address_information.csv ','r')
#search for the correct email address
reader=xfile.read()
address=re.findall(r'(\S+@\S+com)',reader)
print(address)
xfile.close()

xfile1=open('body.txt','r')   
body=xfile1.read()
print(body)
xfile1.close()

re_email = re.compile(r'^[0-9A-Za-z_]+@[0-9A-Za-z_]+(\.[0-9A-Za-z_]+)+$')
re_loginname = re.compile(r'(\S+)@')

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

mail_host="smtp.sina.com"  #设置服务器
mail_user="cjj200076@sina.com"    #用户名
mail_pass="chenjiajia7025"   #口令 
 
 
sender = 'cjj200076@sina.com'
receivers=['cjj200076@sina.com'] # 接收邮件，可设置为你的邮箱
 
message = MIMEText('body', 'plain', 'utf-8')
message['From'] = Header("cjj200076", 'utf-8')   #use utf-8 in ascii but not vice versa
message['To'] =  Header("test", 'utf-8')
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ('Mail sent successfully!')
except smtplib.SMTPException:
    print ('Error: failure')