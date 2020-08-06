#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import sklearn.metrics as sm


# In[2]:


dataset = make_blobs(n_samples =50 ,n_features=2,centers=4,cluster_std=1.6,random_state=50)


# In[3]:


dataset


# In[4]:


points =dataset[0]


# In[5]:


plt.scatter(dataset[0][:,0],dataset[0][:,1])


# In[6]:


import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering


# In[7]:


hc = AgglomerativeClustering(n_clusters=4,affinity='euclidean',linkage='ward')


# In[8]:


y_hc = hc.fit_predict(points)


# In[11]:


plt.scatter(points[y_hc == 0,0], points[y_hc == 0,1], s = 100 ,c='green')
plt.scatter(points[y_hc == 1,0], points[y_hc == 1,1], s = 100 ,c='red')
plt.scatter(points[y_hc == 2,0], points[y_hc == 2,1], s = 100 ,c='black')
plt.scatter(points[y_hc == 3,0], points[y_hc == 3,1], s = 100 ,c='blue')


# In[12]:


dendrogram = sch.dendrogram(sch.linkage(points,method='ward'))


# In[ ]:




