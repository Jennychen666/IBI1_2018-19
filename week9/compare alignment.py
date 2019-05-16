# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 00:50:06 2019

@author: admin
"""

import pandas as pd
import numpy as np
import re
seq_human="MLSRAVCGTSRQLAPVLGYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQ\
EALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASV\
GVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINW\
ENVTERYMACKK"
#genbank protein一栏搜索蛋白质编码 FASTA
seq_mouse="MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYH\
EALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSV\
GVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINW\
ENVTERYTACKK"
seq_random="WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEV\
GCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACF"
data=pd.read_csv(r'C:/Users/admin/Desktop/IBI/IBI1_2018-19/week9/Blosum62.txt',sep=r' +')
blosum=data.to_dict()
count=0
i=0
else_distance=0
for i in range[len(seq_human)]:
    if  seq_human[i]== seq_mouse[i]:
       value=blosum.copy(str(i))
    elif seq_human[i]!=seq_mouse[i]:
        else_distance+=1
    print(else_distance)
    value_new=value+else_distance
    value2=blosum.get(str,default=None)
    res=re.match(str,value2)

    
blosum=np.array( (25, 25) )

count+=1
print(blosum['A'][0])

#print(seq_human)



