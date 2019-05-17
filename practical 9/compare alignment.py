# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 00:50:06 2019

@author: admin
"""
#create a two dimension dictionary
seq_human='MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEK\
YQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWG\
WLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
seq_mouse='MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEK\
YHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWG\
WLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
seq_random="WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLME\
VGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTT\
VRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL"
def readdic(filename):
    handle=open(filename,"r")
    content=handle.readlines()
    handle.close()
    
    letters=[]
    dic={}
    
    first=True
    for line in content:
        splitted=line.split()
        if first:
            for a in splitted:
                dic[a]={}
                letters.append(a)
            first=False
        else:
            a=splitted[0]
            for i in range(1,len(splitted)):
                b=letters[i-1]
                dic[a][b]=splitted[i]
    return dic
#use the two dimension directory for the Blosum62.txt
dic=readdic('Blosum62.txt')

#calculate the score which starts with 0
score1=0
for i in range(0,len(seq_human)):# same length
    score1=score1+(int(dic[seq_human[i]][seq_mouse[i]]))# read the corresponding numbers
    #print(score)
print('The BLOSUM score for human-mouse comparison:'+str(score1))
score2=0
for i in range(0,len(seq_human)):# same length
    score2=score2+(int(dic[seq_human[i]][seq_random[i]]))# read the corresponding numbers
print('The BLOSUM score for human-random comparison:'+str(score2))
score3=0
for i in range(0,len(seq_human)):# same length
    score3=score3+(int(dic[seq_random[i]][seq_mouse[i]]))# read the corresponding numbers
print('The BLOSUM score for mouse-random comparison:'+str(score3))


#calculate identities for the three comparsions
count1=0
for i in range(0,len(seq_human)):
    if seq_human[i]==seq_mouse[i]:
        count1=count1+1
#print(count)
identity=count1/len(seq_human)
identity=str(identity*100)+'%'
print('Identity for human-mouse comparison is :'+identity)
count2=0
for i in range(0,len(seq_human)):
    if seq_human[i]==seq_random[i]:
        count2=count2+1
#print(count)
identity2=count2/len(seq_human)
identity2=str(identity2*100)+'%'
print('Identity for human-random comparison is:'+identity2)

count3=0
for i in range(0,len(seq_human)):
    if seq_mouse[i]==seq_random[i]:
        count3=count3+1
#print(count)
identity3=count3/len(seq_human)
identity3=str(identity3*100)+'%'

print('Identity for mouse-random comparison is:'+identity3)


