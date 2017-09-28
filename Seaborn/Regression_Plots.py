
# coding: utf-8

# In[1]:

import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[2]:

tips = sns.load_dataset('tips')


# In[3]:

tips.head()


# ## lmplot()

# In[5]:

sns.lmplot(x='total_bill',y='tip',data=tips)


# In[6]:

sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')


# In[13]:

sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm')


# In[16]:

sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm',
           markers=['o','v'],scatter_kws={'s':100})


# ## Using a Grid
# 

# In[28]:

sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')


# In[30]:

sns.lmplot(x="total_bill", y="tip", row="sex", col="time",data=tips)


# In[24]:

sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm')


# ## Aspect and Size
# 
# Seaborn figures can have their size and aspect ratio adjusted with the **size** and **aspect** parameters:

# In[36]:

sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm',
          aspect=0.6,size=8)


