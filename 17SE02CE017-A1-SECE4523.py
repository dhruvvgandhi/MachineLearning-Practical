#!/usr/bin/env python
# coding: utf-8

# In[4]:


def Hamming_Distance():
    flag1=0
    flag2=0
    flag3=0
    resultstr=''
    while flag1!=1:
        a=list(input("enter first binary string:"))
        flag1=cheakbinary(a)
        
    while flag2!=1 or flag3!=1:
        b=list(input("enter second binary string:"))
        flag2=cheakbinary(b)
        flag3=cheaklenth(b,a) 
    x,y=0,0
    for i in range(len(a)):
        if a[i]=='1':
            x=x+1
        if b[i]=='1':
            y=y+1
    count=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            count=count+1
            resultstr=resultstr+'1'
        else:
            resultstr=resultstr+'0'
    stra=''.join(a)
    strb=''.join(b)
    print(stra)
    print(strb)
    print(resultstr)
    print(count)
# cheak if the lenth of both the string is equal or not   
def cheaklenth(sample1,sample2):
    if len(sample1)==len(sample2):
        return 1
    else:
        print('lenth of string b should be equal to a')
        return 0
#cheak if the string is in binary or not
def cheakbinary(sample):
    count1=0
    for i in sample:
        if i=='0' or i=='1':
            count1=count1+1
    if count1==len(sample):
        return 1
    else:
        print('string is not in binary please enter again')
        return 0
#calling hamming distance function
Hamming_Distance()        


# In[33]:


class Distance:
    def euclidean(self, x, y):        
        d = 0.0
        for k in range(len(x)):
            d += abs((x[k]-y[k]))**2
        return d**(1.0/2.0)
    
    def manhattan(self, x, y):
        d=0.0
        for k in range(len(x)):
            d += abs((x[k]-y[k]))
        return d
    
    def minkowski(self, x, y, p):
        d = 0.0
        for k in range(len(x)):
            d+= abs((x[k]-y[k]))**p
        return d**(1.0/p)

# Given Data 
a = [10, 20, 15, 10, 5]
b = [12, 24, 18, 8, 7]
dist = Distance()
print("Euclidean Distance:")
print(dist.euclidean(a,b))
print("")
print("Manhattan Distance:")
print(dist.manhattan(a,b))
print("")
print("Minkowski Distance:")
print(dist.minkowski(a,b,1))
print(dist.minkowski(a,b,2))


# In[ ]:




