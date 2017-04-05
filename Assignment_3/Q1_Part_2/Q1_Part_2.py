
# coding: utf-8

# # Question 1 Part 2
# - Use ‘vehicle_collisions’ data set.
# - For each borough, find out distribution of each collision scale. (One car involved? Two? Three? or more?) (From 2015 to present)
# - Display a few rows of the output use df.head().
# - Generate a csv output with five columns ('borough', 'one-vehicle', 'two- vehicles', 'three-vehicles', 'more-vehicles')

# In[10]:

import pandas as pd


# In[11]:

vs = pd.read_csv('../Data/vehicle_collisions.csv', sep=',')


# In[12]:

vs = vs[pd.notnull(vs['BOROUGH'])].reset_index(drop = True) 


# In[13]:

total = 5
vehicle_df = vs[['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]
scale = total - vehicle_df.isnull().sum(axis=1)  #calculate the number of vehicles involved for each accident


# In[14]:

def categorize_scale(row):
    if row['VEHICLES_INVOLOVED'] == 0:
        row['ZERO_VEHICLE_INVOLVED'] += 1
        return row
    if row['VEHICLES_INVOLOVED'] == 1:
        row['ONE_VEHICLE_INVOLVED'] += 1
        return row
    if row['VEHICLES_INVOLOVED'] == 2:
        row['TWO_VEHICLES_INVOLVED'] += 1
        return row
    if row['VEHICLES_INVOLOVED'] == 3:
        row['THREE_VEHICLES_INVOLVED'] += 1
        return row
    else:
        row['MORE_VEHICLES_INVOLVED'] += 1
        return row                                 #define a function to put the number of vehicles involved to the corresponding column


# In[15]:

df = pd.DataFrame({'BOROUGH':vs['BOROUGH'],'VEHICLES_INVOLOVED':scale.values, 'ZERO_VEHICLE_INVOLVED':0, 'ONE_VEHICLE_INVOLVED':0, 'TWO_VEHICLES_INVOLVED':0, 'THREE_VEHICLES_INVOLVED':0, 'MORE_VEHICLES_INVOLVED':0})
df = df.apply(lambda x: categorize_scale(x), axis =1).drop(['VEHICLES_INVOLOVED', 'ZERO_VEHICLE_INVOLVED'], 1)
df.head()                      #apply the function to the dataframe


# In[16]:

df = df.groupby('BOROUGH', as_index=False).sum()     #sum up by BOROUGH


# In[17]:

df = df[['BOROUGH','ONE_VEHICLE_INVOLVED','TWO_VEHICLES_INVOLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_INVOLVED']]
df.head()


# In[18]:

df.to_csv('Q1_Part_2.csv', sep=',', index=False)

