#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn import svm

import matplotlib.pyplot as plt
import seaborn as sns;sns.set(font_scale=1.2)

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


recipes =pd.read_csv("recipes.csv")
recipes


# In[5]:


sns.lmplot('Flour','Sugar',data=recipes,hue='Type',
          palette='Set1',fit_reg=False,scatter_kws={"s":70});


# In[8]:


ingrediants=recipes[['Flour','Milk','Sugar','Butter','Egg','Baking Powder','Vanilla','Salt']]
ingrediants=recipes[['Flour','Sugar']]
type_label=np.where(recipes['Type']=='Muffin',0,1)

recipes_features=recipes.columns.values[1:].tolist()
recipes_features


# In[10]:


model=svm.SVC(kernel='linear')
model.fit(ingrediants,type_label)


# In[12]:


w=model.coef_[0]
a=-w[0]/w[1]
xx=np.linspace(30,60)
yy=a*xx-(model.intercept_[0])/w[1]

b=model.support_vectors_[0]
yy_down=a*xx + (b[1]-a*b[0])
b=model.support_vectors_[1]
yy_up=a*xx + (b[1]-a*b[0])


# In[14]:


sns.lmplot('Flour','Sugar',data=recipes,hue='Type',palette='Set1',fit_reg=False,scatter_kws={"s":70})
plt.plot(xx,yy,linewidth=2,color='black');


# In[15]:


sns.lmplot('Flour','Sugar',data=recipes,hue='Type',palette='Set1',fit_reg=False,scatter_kws={"s":70})
plt.plot(xx,yy,linewidth=2,color='black')
plt.plot(xx,yy_down,'k--')
plt.plot(xx,yy_up,'k--')
plt.scatter(model.support_vectors_[:,0],model.support_vectors_[:,1],
           s=80,facecolors='none');


# In[16]:


def muffin_or_cupcake(flour,sugar):
    if(model.predict([[flour,sugar]]))==0:
        print('You\'re looking at a muffin recipe!')
    else:
         print('You\'re looking at a cupcake recipe!')


# In[17]:


muffin_or_cupcake(50,20)


# In[18]:


sns.lmplot('Flour','Sugar',data=recipes,hue='Type',palette='Set1',fit_reg=False,scatter_kws={"s":70})
plt.plot(xx,yy,linewidth=2,color='black')
plt.plot(20,20,'yo',markersize='9');


# In[19]:


muffin_or_cupcake(40,20)


# In[20]:


sns.lmplot('Flour','Sugar',data=recipes,hue='Type',palette='Set1',fit_reg=False,scatter_kws={"s":70})
plt.plot(xx,yy,linewidth=2,color='black')
plt.plot(40,20,'yo',markersize='9');

