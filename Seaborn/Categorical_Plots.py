
# coding: utf-8



# In[5]:

import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[6]:

tips = sns.load_dataset('tips')
tips.head()


# ## barplot and countplot
# 


# In[8]:

sns.barplot(x='sex',y='total_bill',data=tips)


# In[10]:

import numpy as np


# You can change the estimator object to your own function, that converts a vector to a scalar:

# In[11]:

sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)


# ### countplot
# 
# 
# In[13]:

sns.countplot(x='sex',data=tips)


# ## boxplot and violinplot
# 

# In[22]:

sns.boxplot(x="day", y="total_bill", data=tips,palette='rainbow')


# In[25]:

# Can do entire dataframe with orient='h'
sns.boxplot(data=tips,palette='rainbow',orient='h')


# In[26]:

sns.boxplot(x="day", y="total_bill", hue="smoker",data=tips, palette="coolwarm")


# ### violinplot

# In[27]:

sns.violinplot(x="day", y="total_bill", data=tips,palette='rainbow')


# In[37]:

sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',palette='Set1')


# In[36]:

sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',split=True,palette='Set1')


# ## stripplot and swarmplot


# In[38]:

sns.stripplot(x="day", y="total_bill", data=tips)


# In[39]:

sns.stripplot(x="day", y="total_bill", data=tips,jitter=True)


# In[42]:

sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1')


# In[43]:

sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1',split=True)


# In[44]:

sns.swarmplot(x="day", y="total_bill", data=tips)


# In[47]:

sns.swarmplot(x="day", y="total_bill",hue='sex',data=tips, palette="Set1", split=True)


# ### Combining Categorical Plots

# In[61]:

sns.violinplot(x="tip", y="day", data=tips,palette='rainbow')
sns.swarmplot(x="tip", y="day", data=tips,color='black',size=3)


# ## factorplot
# 
# factorplot is the most general form of a categorical plot. It can take in a **kind** parameter to adjust the plot type:

# In[15]:

sns.factorplot(x='sex',y='total_bill',data=tips,kind='bar')

