#!/usr/bin/env python
# coding: utf-8

# # Retrieving Tweets from the Twitter API via Tweepy

# In[1]:


# %load_ext dotenv
get_ipython().run_line_magic('reload_ext', 'dotenv')
get_ipython().run_line_magic('dotenv', '')


# ## Loading in Packages

# In[1]:


import tweepy
import os
import pandas as pd
import time


# ## Importing Authentication for API

# In[3]:


API_KEY = os.environ.get('API_KEY')
API_SECRET_KEY = os.environ.get('API_SECRET_KEY')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')


# In[4]:


if "'" in API_SECRET_KEY:
    API_SECRET_KEY = API_SECRET_KEY.replace("'", '')


# In[5]:


auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)


# ## Acquiring Tweets Relating to Suicidal Ideation/Poor Mental Health

# In[6]:


indicator_queries = ['commit suicide', 'kill myself', 'want to die', 'hate myself']


# In[7]:


count = 5000
tweets_df = pd.DataFrame(columns=['Created At', 'Tweet'])


# In[8]:


for text_query in indicator_queries:
    try:
     # Creation of query method using parameters
     tweets = tweepy.Cursor(api.search,q=text_query).items(count)

     # Pulling information from tweets iterable object
     tweets_list = [[tweet.created_at, tweet.text] for tweet in tweets]

     # Creation of dataframe from tweets list
     # Add or remove columns as you remove tweet information
     query_df = pd.DataFrame(tweets_list, columns=['Created At', 'Tweet'])
    
     tweets_df = tweets_df.append(query_df)

    except BaseException as e:
        print('failed on_status,',str(e))
        time.sleep(3)


# In[9]:


tweets_df.reset_index().drop(['index'], axis=1)


# In[10]:


tweets_df.to_csv('./indicator_tweets.csv')

