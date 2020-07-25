#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


# In[2]:


d=pd.read_csv('customer_dataset.csv')
print(d.head(10))


# In[6]:


a=d.iloc[:,1:4]
a.head()


# In[7]:


b=d.iloc[:,-1]
b.head()


# In[8]:


knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(a,b)


# In[9]:


b_pred=knn.predict(a)
b_predict = pd.DataFrame(data = [b_pred,b.values])
b_predict


# In[10]:


knn.predict([[65,200,2]])


# In[17]:


from sklearn.model_selection import train_test_split
a_train,a_test,b_train,b_test = train_test_split(a,b,test_size=.3,random_state=1)
knn.fit(a_train,b_train)


# In[19]:


b_test_pred=knn.predict(a_test)
b_test_pred


# In[20]:


b_test


# In[21]:


b_test.values


# In[22]:


prediction_output =pd.DataFrame(data=[b_test_pred,b_test.values])
prediction_output

