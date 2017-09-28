
# coding: utf-8


# In[1]:

import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[7]:

flights = sns.load_dataset('flights')


# In[10]:

tips = sns.load_dataset('tips')


# In[11]:

tips.head()


# In[4]:

flights.head()


# ## Heatmap

# In[12]:

tips.head()


# In[14]:

# Matrix form for correlation data
tips.corr()


# In[16]:

sns.heatmap(tips.corr())


# In[19]:

sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)


# Or for the flights data:

# In[23]:

flights.pivot_table(values='passengers',index='month',columns='year')


# In[24]:

pvflights = flights.pivot_table(values='passengers',index='month',columns='year')
sns.heatmap(pvflights)


# In[30]:

sns.heatmap(pvflights,cmap='magma',linecolor='white',linewidths=1)


# ## clustermap
# 
# The clustermap uses hierarchal clustering to produce a clustered version of the heatmap. For example:

# In[31]:

sns.clustermap(pvflights)



# In[34]:

# More options to get the information a little clearer like normalization
sns.clustermap(pvflights,cmap='coolwarm',standard_scale=1)

