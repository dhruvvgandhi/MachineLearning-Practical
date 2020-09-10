#!/usr/bin/env python
# coding: utf-8

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.datasets import make_circles
# from mpl_toolkits.mplot3d import Axes3D

# In[5]:


import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.datasets import make_circles 
from mpl_toolkits.mplot3d import Axes3D


# In[71]:


X,Y=make_circles(n_samples=100,noise=0.01)


# In[72]:


plt.scatter(X[:,0],X[:,1],c=Y,marker= '*')
plt.show()


# In[73]:


X1=X[:,0].reshape((-1,1))
X2=X[:,1].reshape((-1,1))
X3=(X1**2+X2**2)
X=np.hstack((X,X3))


# In[75]:


fig=plt.figure()
axes=fig.add_subplot(111,projection='3d')
axes.scatter(X1,X2,X1**5,X2**5,c=Y,depthshade=True)
plt.show()


# In[76]:


from sklearn import svm


# In[77]:


svc=svm.SVC(kernel = 'linear')
svc.fit(X,Y)


# In[78]:


w=svc.coef_
b=svc.intercept_


# In[79]:


x1=X[:,0].reshape((-1,1))
x2=X[:,1].reshape((-1,1))
x1,x2=np.meshgrid(x1,x2)
x3= -(w[0][0]*x1 + w[0][1]*x2+b)/w[0][2]


# In[80]:


fig=plt.figure()
axes2=fig.add_subplot(111,projection='3d')
axes2.scatter(X1,X2,X1**2+X2**2,c=Y,depthshade=True)
axes1=fig.gca(projection='3d')
axes1.plot_surface(x1,x2,x3,alpha=0.1)
plt.show()


# In[ ]:




