# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 09:46:14 2022

@author: reyze
"""


import random 
import numpy as np
import string 
#create radom alphabet array
alphabet=[]
file_name='spamiam.txt'
string1='abcdefghijklmnopqrstuvwxyz'
wordsbook=[]
for i in string1:
    alphabet.append(i)
for i in range(0,10):
    for k in range(0,10):
     words=[]
     for w in range(0,4):
        a=random.choice(alphabet)
        words.append(a)
     str1 = "".join(words)
     wordsbook.append(str1)
wordsbook=np.array(wordsbook)
wordsbook= wordsbook.reshape(10,10)
print('---------this is radom select 4 words letter----------')
print(wordsbook)
#find words
print("---------------find words in rows and columns-----------------")
f=open("4words.txt","r")
res= f.readlines()
a_words=[]
for word in res:
    a_words.append(word.strip("\n"))
for i in range(0,10):
    for k in range(0,10):
        for w in a_words:
            if wordsbook[i][k]==w:
                print(str(i)+"  "+str(k))
#find the new pob
f = open(file_name, "r")
res = f.readlines()
t = list()
for cur in res:
# strip方法去除每一行的换行符
 t.append(list(cur.strip("\n")))
    # t为一个二维列表
f.close()
letter_d={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
letter_p={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
for content in t:
    for letter in content:
        for count in range(0,26):
            if letter.lower()==alphabet[count]:
                letter_d[alphabet[count]]=letter_d[alphabet[count]]+1
total=0
p=[]
for count in range(0,26):
    total=total+letter_d[alphabet[count]]
for count in range(0,26):
     letter_p[alphabet[count]]=letter_d[alphabet[count]]/total
     p.append(letter_p[alphabet[count]])
p1 = np.array(p)

wordsbook=[]
for i in range(0,10):
    for k in range(0,10):
     words=[]
     for w in range(0,4):
        index = np.random.choice(alphabet, p = p1.ravel())
        words.append(index)
     str1 = "".join(words)
     wordsbook.append(str1)
wordsbook=np.array(wordsbook)
wordsbook= wordsbook.reshape(10,10)
print('---------this is spamiam select 4 words letter----------')
print(wordsbook)
#find words
print("---------------find words in rows and columns-----------------")
f=open("4words.txt","r")
res= f.readlines()
a_words=[]
for word in res:
    a_words.append(word.strip("\n"))
for i in range(0,10):
    for k in range(0,10):
        for w in a_words:
            if wordsbook[i][k]==w:
                print(str(i)+"  "+str(k))
#find the new prob for c
f = open(file_name, "r")
res = f.readlines()
t = list()
for cur in res:
# strip方法去除每一行的换行符
 t.append(list(cur.strip("\n")))
    # t为一个二维列表
f.close()
letter_d={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
letter_d_plus={'a':letter_d,'b':letter_d,'c':letter_d,'d':letter_d,'e':letter_d,'f':letter_d,'g':letter_d,'h':letter_d,'i':letter_d,'j':letter_d,'k':letter_d,'l':letter_d,'m':letter_d,'n':letter_d,'o':letter_d,'p':letter_d,'q':letter_d,'r':letter_d,'s':letter_d,'t':letter_d,'u':letter_d,'v':letter_d,'w':letter_d,'x':letter_d,'y':letter_d,'z':letter_d}
for i in alphabet:
    letter_d_plus[i]=letter_d.copy()
for content in t:
    length=0
    while length<len(content):
        for count in range(0,26):
            if content[length].lower()==alphabet[count] and (length+1)<len(content):
                for count2 in range(0,26):
                 if content[length+1].lower()==alphabet[count2]:
                  letter_d_plus[alphabet[count]][alphabet[count2]]=letter_d_plus[alphabet[count]][alphabet[count2]]+1
        length=length+1
for i in alphabet:
    total=0
    for w in alphabet:
     total=total+letter_d_plus[i][w]
    if total!=0:
     for k in alphabet:
      letter_d_plus[i][k]=letter_d_plus[i][k]/total

wordsbook=[]
for i in range(0,10):
    for k in range(0,10):
     words=[]
     index = np.random.choice(alphabet, p = p1.ravel())
     words.append(index)
     for w in range(0,3):
      for i in alphabet:
        if index==i:
            p_p=letter_d_plus[i]
            p2=[]
            for k in alphabet:
              p2.append(p_p[k])
            p2=np.array(p2)
            index2=np.random.choice(alphabet, p = p2.ravel())
            words.append(index2)
     str1 = "".join(words)
     wordsbook.append(str1)
wordsbook=np.array(wordsbook)
wordsbook= wordsbook.reshape(10,10)
print('---------this is spamiam select 4 words letter_plus_mode----------')
print(wordsbook)
#find words
print("---------------find words in rows and columns-----------------")
f=open("4words.txt","r")
res= f.readlines()
a_words=[]
for word in res:
    a_words.append(word.strip("\n"))
for i in range(0,10):
    for k in range(0,10):
        for w in a_words:
            if wordsbook[i][k]==w:
                print(str(i)+"  "+str(k))
#2d
wordsbook=[]
for i in range(0,10):
    for k in range(0,10):
     words=[]
     index = np.random.choice(alphabet, p = p1.ravel())
     words.append(index)
     for w in range(0,3):
      for i in alphabet:
        if index==i:
            p_p=letter_d_plus[i]
            p2=[]
            for k in alphabet:
              p2.append(p_p[k])
            p2=np.array(p2)
            index2=np.random.choice(alphabet, p = p2.ravel())
            words.append(index2)
     str1 = "".join(words)
     wordsbook.append(str1)
wordsbook=np.array(wordsbook)
wordsbook= wordsbook.reshape(10,10)
print('---------this is spamiam select 4 words letter_plus_mode plus----------')
print(wordsbook)
#find words
print("---------------find words in rows and columns-----------------")
f=open("4words.txt","r")
res= f.readlines()
a_words=[]
for word in res:
    a_words.append(word.strip("\n"))
for i in range(0,10):
    for k in range(0,10):
        for w in a_words:
            if wordsbook[i][k]==w:
                print(str(i)+"  "+str(k))

       
            
        





