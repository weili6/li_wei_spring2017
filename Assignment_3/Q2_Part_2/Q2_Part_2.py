
# coding: utf-8

# # Question 2 Part 2
# - Use 'employee_compensation' data set.
# - Data contains fiscal and calendar year information. Same employee details exist twice in the dataset. Filter data by calendar year and find average salary (you might have to find average for each of the columns for every employee. Eg. Average of Total Benefits, Average of total compensation etc.) for every employee.
# - Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# - For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value.
# - Display the top 5 Job Families according to this percentage value using df.head().
# - Write the output (jobs and percentage value) to a csv.

# In[1]:

import pandas as pd


# In[2]:

ec = pd.read_csv('../Data/employee_compensation.csv', sep=',')


# In[3]:

df = ec[ec['Year Type'] == 'Calendar'].reset_index(drop=True)  #filter by calender year


# In[4]:

avg_salary = df[['Salaries','Overtime','Other Salaries','Total Salary','Retirement','Health/Dental','Other Benefits','Total Benefits','Total Compensation']].mean(axis=0)
avg_salary   #calculate the average number for each compensation type


# In[5]:

rate = 0.05
ot_df = df[df['Overtime'] > rate*df['Salaries']].reset_index(drop=True)
ot_df.head()     #people whose overtime is greater than 5% of salaries


# In[6]:

benefit_df = df.groupby('Job Family')['Total Benefits','Total Compensation'].mean()
benefit_df['Percent_Total_Benefit'] = benefit_df['Total Benefits']/benefit_df['Total Compensation']
benefit_df = benefit_df.sort_values(by = 'Percent_Total_Benefit', ascending=False)
benefit_df.head()    #group by Job Family and sort


# In[7]:

benefit_df.to_csv('Q2_Part_2.csv', sep=',', index=True)

