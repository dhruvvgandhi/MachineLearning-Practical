#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
from apyori import apriori


# In[3]:


pip install apyori


# In[5]:


sd=pd.read_csv("apriority.csv",header=None)
sd


# In[6]:


sd.shape


# In[7]:


r=[]
for i in range(0,22):
    r.append([str(sd.values[i,j])for j in range(0,6)])
r


# In[11]:


ar=apriori(r,min_support=0.50,min_confidence=0.80,min_left=1.2,min_length=2)
ars=list(ar)
print(len(ars))
print()
print(ars)


# In[ ]:




