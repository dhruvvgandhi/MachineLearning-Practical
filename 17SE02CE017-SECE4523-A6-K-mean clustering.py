#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


# In[23]:


dataset = make_blobs(n_samples=100,n_features=2,centers=4,cluster_std=1.8,random_state=50)


# In[24]:


dataset


# In[25]:


points=dataset[0]


# In[26]:


plt.scatter(dataset[0][:,0],dataset[0][:,1])


# In[27]:


from sklearn.cluster import KMeans


# In[28]:


kmean=KMeans(n_clusters=4)


# In[29]:


kmean.fit(points)


# In[30]:


clusters=kmean.cluster_centers_


# In[31]:


clusters


# In[32]:


y_km=kmean.fit_predict(points)


# In[33]:


y_km


# In[40]:


plt.scatter(points[y_km == 0,0], points[y_km == 0,1], s = 50, c='green')
plt.scatter(points[y_km == 1,0], points[y_km == 1,1], s = 50, c='orange')
plt.scatter(points[y_km == 2,0], points[y_km == 2,1], s = 50, c='blue')
plt.scatter(points[y_km == 3,0], points[y_km == 3,1], s = 50, c='red')
plt.scatter(clusters[0][0],clusters[0][1],marker='+',s=200,c='black')
plt.scatter(clusters[1][0],clusters[1][1],marker='*',s=200,c='black')
plt.scatter(clusters[2][0],clusters[2][1],marker='+',s=200,c='black')
plt.scatter(clusters[3][0],clusters[3][1],marker='*',s=200,c='black')


# In[ ]:




