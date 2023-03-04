#!/usr/bin/env python
# coding: utf-8

# In[1]:


# How to call Numpy

import numpy as np


# In[2]:


# import pandas

import pandas as pd


# In[3]:


# create a numpy array by converting lists 

Vec = np.array ([1,2,3,4,5,6,7,9,11])


# In[4]:


print(Vec)


# In[5]:


# create a matrix

Matrix = np.array([[1,2,3],[5,5,7],[2,7,6],[1,9,4]])


# In[6]:


print(Matrix)


# In[7]:


# Transpose of Matrix

print(Matrix.T)


# In[8]:


x  = np.sqrt(199999999)


# In[9]:


print(x)


# In[10]:


#all about arrays

vec1 = np.arange (0,300)


# In[11]:


print(vec1)


# In[12]:


vec = np.arange(2,50,10)


# In[13]:


print(vec)


# In[14]:


#linespace:- linear spacing where both 1st and last is inclusive

vec3=np.linspace(0,20,10)


# In[15]:


print(vec3)


# In[16]:


#Reshape

vec3.reshape(5,2)


# In[17]:


#Zeros & Ones 

mat2=np.zeros([4,4])


# In[18]:


print(mat2)


# In[19]:


mat3=np.ones([3,3])


# In[20]:


print(mat3)


# In[21]:


#Identify Matrix
mat4=np.eye(5)


# In[22]:


print(mat4)


# In[23]:


mat5 = mat4.T


# In[24]:


print(mat5)


# In[25]:


# vectors can be added & substracted of same size

vec1=np.arange(1,6)


# In[26]:


print(vec1)


# In[27]:


vec2=np.arange(5,10)


# In[28]:


print(vec2)


# In[29]:


vec1+vec2


# In[30]:


vec1-vec2


# In[31]:


vec1*vec2


# In[32]:


vec1/vec2


# In[33]:


print(1/vec1)


# In[34]:


print(1/vec2)


# In[35]:


print(np.sqrt(vec1))


# In[36]:


#Unique value in an array
vec7=np.array(["Orange","mango","apple","tomato","4","apple","rice","Mango"])


# In[37]:


print(vec7)


# In[38]:


print(np.unique(vec7))


# In[39]:


#generate random variable
rand_mat=np.random.rand(10,10) #uniform random variable


# In[40]:


print(rand_mat)


# In[41]:


#Mean(mean)
z=np.mean(rand_mat)


# In[42]:


print(z)


# In[43]:


#Max
np.max(rand_mat)


# In[44]:


#Min
np.min(rand_mat)


# In[45]:


#Logical Entries
rand_vec=np.random.randn(20)


# In[46]:


print(rand_vec)


# In[47]:


print(rand_vec>0)


# In[48]:


print(rand_vec[rand_vec>0])


# In[49]:


print(rand_vec[rand_vec>1])


# In[ ]:




