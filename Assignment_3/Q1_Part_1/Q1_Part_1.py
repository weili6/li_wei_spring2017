
# coding: utf-8

# # Question 1 Part 1
# - Use ‘vehicle_collisions’ data set.
# - For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City.
# - Display a few rows of the output use df.head().
# - Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’).

# In[18]:

import pandas as pd


# In[19]:

vs = pd.read_csv('../Data/vehicle_collisions.csv', sep=',')


# In[20]:

vs_16 = vs[vs['DATE'].apply(lambda x: x.split('/')[2] == '16')]               #get all 2016 collisions data


# In[21]:

nyc = vs_16['DATE'].apply(lambda x: x.split('/')[0]).value_counts()           #get the number of collisions in new york in each month
nyc.index = nyc.index.astype(int)
nyc = nyc.sort_index()


# In[22]:

mh = vs_16[vs_16['BOROUGH'] == 'MANHATTAN']['DATE'].apply(lambda x: x.split('/')[0]).value_counts()
mh.index = mh.index.astype(int)
mh = mh.sort_index()                               #get the number of collisions in manhattan in each month


# In[23]:

df_nyc = pd.DataFrame({'MONTH':nyc.index, 'NYC':nyc.values})
df_mh = pd.DataFrame({'MONTH':mh.index, 'MANHATTAN':mh.values})
df = pd.merge(df_mh,df_nyc)                        #merge month series with collisions series


# In[24]:

df['PERCENTAGE'] = df['MANHATTAN']/df['NYC']       #calculate percentage for each month


# In[25]:

df = df[['MONTH','MANHATTAN','NYC','PERCENTAGE']]
df.head()


# In[26]:

df.to_csv('Q1_Part_1.csv', sep=',', index=False)

