#!/usr/bin/env python
# coding: utf-8

# HackerRank
# 
# Left Rotation 
# 
# 

# In[4]:


d = 4
n = 5 
arr = [1, 2, 3, 4, 5]
arr = arr[d:] +arr[:d] 
arr


# In[7]:


d = 4
n = 5 
arr = [1, 2, 3, 4, 5]
for i in range(d):
       arr =arr[1:] +[arr[0]]
return arr

