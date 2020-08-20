#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


centers=[[0.5,2],[-1,-1],[1.5,-1]]


# In[5]:


X,y=make_blobs(n_samples=400,centers=centers,cluster_std=0.5,random_state=0)


# In[7]:


X= StandardScaler().fit_transform(X)


# In[8]:


plt.figure(figsize=(10,6))
plt.scatter(X[:,0],X[:,1],c=y,cmap='Paired')


# In[9]:


from sklearn.cluster import DBSCAN
db = DBSCAN(eps=0.4,min_samples=20)


# In[10]:


db.fit(X)


# In[12]:


y_pred=db.fit_predict(X)


# In[13]:


plt.figure(figsize=(10,6))
plt.scatter(X[:,0],X[:,1],c=y_pred,cmap='Paired')
plt.title("Clusters determined by DBSCAN")


# In[15]:


db.labels_[db.labels_==-1].size


# In[ ]:




