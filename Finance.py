
# coding: utf-8



# In[3]:

from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
get_ipython().magic('matplotlib inline')



# In[4]:

start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)


# In[5]:

# Bank of America
BAC = data.DataReader("BAC", 'google', start, end)

# CitiGroup
C = data.DataReader("C", 'google', start, end)

# Goldman Sachs
GS = data.DataReader("GS", 'google', start, end)

# JPMorgan Chase
JPM = data.DataReader("JPM", 'google', start, end)

# Morgan Stanley
MS = data.DataReader("MS", 'google', start, end)

# Wells Fargo
WFC = data.DataReader("WFC", 'google', start, end)


# In[6]:

# Could also do this for a Panel Object
df = data.DataReader(['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC'],'google', start, end)


# ** Create a list of the ticker symbols (as strings) in alphabetical order. Call this list: tickers**

# In[7]:

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']


# ** Use pd.concat to concatenate the bank dataframes together to a single data frame called bank_stocks. Set the keys argument equal to the tickers list. Also pay attention to what axis you concatenate on.**

# In[8]:

bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC],axis=1,keys=tickers)


# ** Set the column name levels (this is filled out for you):**

# In[9]:

bank_stocks.columns.names = ['Bank Ticker','Stock Info']


# ** Check the head of the bank_stocks dataframe.**

# In[10]:

bank_stocks.head()


# 
# ** What is the max Close price for each bank's stock throughout the time period?**

# In[11]:

bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()



# In[12]:

returns = pd.DataFrame()


# In[13]:

for tick in tickers:
    returns[tick+' Return'] = bank_stocks[tick]['Close'].pct_change()
returns.head()




# In[14]:

#returns[1:]
import seaborn as sns
sns.pairplot(returns[1:])




# In[15]:


returns.idxmin()


# citigroup stock split in May 2011, but also JPM day after inauguration.
returns.idxmax()


# ** Take a look at the standard deviation of the returns, which stock would you classify as the riskiest over the entire time period? Which would you classify as the riskiest for the year 2015?**

# In[17]:

returns.std() # Citigroup riskiest


# In[18]:

returns.ix['2015-01-01':'2015-12-31'].std() 

# ** Create a distplot using seaborn of the 2015 returns for Morgan Stanley **

# In[19]:

sns.distplot(returns.ix['2015-01-01':'2015-12-31']['MS Return'],color='green',bins=100)


# ** Create a distplot using seaborn of the 2008 returns for CitiGroup **

# In[20]:

sns.distplot(returns.ix['2008-01-01':'2008-12-31']['C Return'],color='red',bins=100)




# In[21]:

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().magic('matplotlib inline')

# Optional Plotly Method Imports
import plotly
import cufflinks as cf
cf.go_offline()


# In[22]:

for tick in tickers:
    bank_stocks[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()


# In[23]:

bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot()


# In[23]:

# plotly
bank_stocks.xs(key='Close',axis=1,level='Stock Info').iplot()


# ## Moving Averages


# In[24]:

plt.figure(figsize=(12,6))
BAC['Close'].ix['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg')
BAC['Close'].ix['2008-01-01':'2009-01-01'].plot(label='BAC CLOSE')
plt.legend()


# ** Create a heatmap of the correlation between the stocks Close Price.**

# In[25]:

sns.heatmap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)




# In[26]:

sns.clustermap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)


# In[27]:

close_corr = bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr()
close_corr.iplot(kind='heatmap',colorscale='rdylbu')



# In[28]:

BAC[['Open', 'High', 'Low', 'Close']].ix['2015-01-01':'2016-01-01'].iplot(kind='candle')


# In[29]:

MS['Close'].ix['2015-01-01':'2016-01-01'].ta_plot(study='sma',periods=[13,21,55],title='Simple Moving Averages')




# In[30]:

BAC['Close'].ix['2015-01-01':'2016-01-01'].ta_plot(study='boll')

