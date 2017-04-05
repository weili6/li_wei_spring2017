
# coding: utf-8

# # Question 3 Part 1
# - Use ‘cricket_matches’ data set.
# - Calculate the average score for each team which host the game and win the game.
# - Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition.
# - Display a few rows of the output use df.head()
# - Generate a csv output.

# In[1]:

import pandas as pd


# In[2]:

cm = pd.read_csv('../Data/cricket_matches.csv', sep=',')


# In[3]:

df = cm[cm['home'] == cm['winner']].reset_index(drop =True)  #find all games that host team won
df['Score'] = 0


# In[4]:

def get_score(row):                  #define a function to decide the score for the host team
    if row['winner'] == row['innings1']:
        row['Score'] = row['innings1_runs']
        return row
    else:
        row['Score'] = row['innings2_runs']
        return row


# In[5]:

df = df.apply(lambda x: get_score(x), axis =1)[['home','Score']]


# In[6]:

df = df.groupby('home',as_index=False).mean()
df.head()                     #group by team name and calculate the average score


# In[7]:

df.to_csv('Q3_Part_1.csv', sep=',', index=False)

