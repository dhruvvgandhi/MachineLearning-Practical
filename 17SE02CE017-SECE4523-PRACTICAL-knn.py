#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


# In[4]:


d=pd.read_excel('knn_datadet.xlsx')
print(d.head(10))


# In[5]:


a=d.iloc[:,0:2]
a.head()


# In[6]:


b=d.iloc[:,-1]
b.head()


# In[7]:


knn=KNeighborsClassifier(n_neighbors=4)
d.shape


# In[8]:


np.sqrt(18)


# In[11]:


knn.fit(a,b)


# In[12]:


knn.predict(a)


# In[13]:


knn.predict([[161,61]])


# In[ ]:




