
# coding: utf-8

# # Question 2 Part 1
# - Use 'employee_compensation' data set.
# - Find out the highest paid departments in each organization group by calculating mean of total compensation for every department.
# - Output should contain the organization group and the departments in each organization group with the total compensation from highest to lowest value.
# - Display a few rows of the output use df.head().
# - Generate a csv output.

# In[7]:

import pandas as pd


# In[8]:

ec = pd.read_csv('../Data/employee_compensation.csv', sep=',')


# In[9]:

df = ec.groupby(["Organization Group", "Department"], as_index=False)['Total Compensation'].mean() #group data by 'organization group' and 'department' and calculate the average compensation for each department
df.head()


# In[10]:

df = df.groupby('Organization Group', as_index=False).apply(lambda x : x.sort_values(by = 'Total Compensation', ascending=False).reset_index(drop=True))
df.head()   #sort by average compensation in each organization group


# In[11]:

df.to_csv('Q2_Part_1.csv', sep=',', index=False)

