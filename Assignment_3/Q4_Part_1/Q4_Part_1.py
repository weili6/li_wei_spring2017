
# coding: utf-8

# # Question 4 Part 1
# - Use ‘movies_awards’ data set.
# - You are supposed to extract data from the awards column in this dataset and split it into several columns. An example is given below.
# - The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.)
# - You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award.
# - If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated).
# - Create two separate columns for each award category (won and nominated).
# - Write your output to a csv file.

# In[18]:

import pandas as pd


# In[19]:

ma = pd.read_csv('../Data/movies_awards.csv', sep=',')


# In[20]:

ma = ma[ma['Awards'].notnull()]        #find all movies which have awards
ma['Awards_won'] = ma['Awards'].str.extract('(\d+) win', expand=True)    #extract the number of awards won
ma['Awards_nominated'] = ma['Awards'].str.extract('(\d+) nomination', expand=True)  #extract the number of awards nominated


# In[21]:

def strip_plural(title):
    if str(title).endswith('s'):
        return str(title)[:-1]
    else:
        return str(title)         #define a function to strip 's' for plural


# In[22]:

ma[['Won_num','Won_name']] = ma['Awards'].str.extract('Won (\d+) (.*). Another', expand=True)   #extract the name and number of awards won
ma[['Nominated_num','Nominated_name']]= ma['Awards'].str.extract('Nominated for (\d+) (.*). Another', expand=True)  #extract the name and number of awards nominated


# In[23]:

ma['Won_name']= ma['Won_name'].apply(lambda x: strip_plural(x))
ma['Nominated_name']= ma['Nominated_name'].apply(lambda x: strip_plural(x))


# In[24]:

ma = ma.drop_duplicates()        #drop all duplicated entries
df1 = ma[['imdbID','Won_name','Won_num']]
df1 = df1.pivot(index = 'imdbID', columns='Won_name', values='Won_num').drop(['nan'],1)
df1 = df1.add_suffix('_won')           #pivot dataframe so that the unique values in won_name volumn will be convert to new column names

df2 = ma[['imdbID','Nominated_name','Nominated_num']]
df2 = df2.pivot(index = 'imdbID', columns='Nominated_name', values='Nominated_num').drop(['nan'],1)
df2 = df2.add_suffix('_nominated')


# In[25]:

df = pd.concat([df1,df2],axis =1)    


# In[26]:

sub_df = ma[['imdbID','Title','Awards','Awards_won','Won_num','Awards_nominated','Nominated_num']].sort_values(by='imdbID')
sub_df.set_index('imdbID',inplace=True)
result_df = sub_df.join(df, how='inner')
result_df.head()         #merge all sub-dataframes


# In[27]:

result_df = result_df.fillna(0)


# In[28]:

result_df['Awards_won'] = result_df['Awards_won'].astype(int) + result_df['Won_num'].astype(int)   #calculate total awards won for each movie
result_df['Awards_nominated'] = result_df['Awards_nominated'].astype(int) + result_df['Nominated_num'].astype(int)  #calculate total awards nominated for each movie


# In[29]:

result_df = result_df.drop(['Won_num','Nominated_num'], axis =1)   #drop unnecessary columns
result_df.head()


# In[30]:

result_df.to_csv('Q4_Part_1.csv', sep=',', index=False)

