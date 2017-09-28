
# coding: utf-8



# In[1]:

import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot,plot
init_notebook_mode(connected=True) 



# In[2]:

import pandas as pd


# In[3]:

df = pd.read_csv('2014_World_Power_Consumption')


# ** Check the head of the DataFrame. **

# In[4]:

df.head()




# In[5]:

data = dict(
        type = 'choropleth',
        colorscale = 'Viridis',
        reversescale = True,
        locations = df['Country'],
        locationmode = "country names",
        z = df['Power Consumption KWH'],
        text = df['Country'],
        colorbar = {'title' : 'Power Consumption KWH'},
      ) 

layout = dict(title = '2014 Power Consumption KWH',
                geo = dict(showframe = False,projection = {'type':'Mercator'})
             )


# In[6]:

choromap = go.Figure(data = [data],layout = layout)
plot(choromap,validate=False)


# ## USA Choropleth
# 
# ** Import the 2012_Election_Data csv file using pandas. **

# In[7]:

usdf = pd.read_csv('2012_Election_Data')


# ** Check the head of the DataFrame. **

# In[8]:

usdf.head()


# ** Now create a plot that displays the Voting-Age Population (VAP) per state. 
# In[9]:

data = dict(type='choropleth',
            colorscale = 'Viridis',
            reversescale = True,
            locations = usdf['State Abv'],
            z = usdf['Voting-Age Population (VAP)'],
            locationmode = 'USA-states',
            text = usdf['State'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 1)),
            colorbar = {'title':"Voting-Age Population (VAP)"}
            ) 


# In[10]:

layout = dict(title = '2012 General Election Voting Data',
              geo = dict(scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )


# In[11]:

choromap = go.Figure(data = [data],layout = layout)
plot(choromap,validate=False)

