import json
import time
import threading
import tweepy
import jsonpickle
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import os
path='C:/Users/Yael nidam/Dropbox (MIT)/00_2018_Spring/03_Big_Data/10_github/big-data-spring2018/week-04'
os.chdir(path)
from twitter_keys import api_key, api_secret


def auth(key, secret):
  auth = tweepy.AppAuthHandler(key, secret)
  api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
  # Print error and exit if there is an authentication error
  if (not api):
      print ("Can't Authenticate")
      sys.exit(-1)
  else:
      return api

api = auth(api_key, api_secret)

def parse_tweet(tweet):
  p = pd.Series()
  if tweet.coordinates != None:
    p['lat'] = tweet.coordinates['coordinates'][0]
    p['lon'] = tweet.coordinates['coordinates'][1]
  else:
    p['lat'] = None
    p['lon'] = None
  p['location'] = tweet.user.location
  p['id'] = tweet.id_str
  p['content'] = tweet.text
  p['user'] = tweet.user.screen_name
  p['user_id'] = tweet.user.id_str
  p['time'] = str(tweet.created_at)
  return p

def get_tweets(
    geo,
    out_file,
    search_term = '',
    tweet_per_query = 100,
    tweet_max = 150,
    since_id = None,
    max_id = -1,
    write = False
  ):
  tweet_count = 0
  all_tweets = pd.DataFrame()
  while tweet_count < tweet_max:
    try:
      if (max_id <= 0):
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            since_id = since_id
          )
      else:
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1)
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1),
            since_id = since_id
          )
      if (not new_tweets):
        print("No more tweets found")
        break
      for tweet in new_tweets:
        all_tweets = all_tweets.append(parse_tweet(tweet), ignore_index = True)
        if write == True:
            with open(out_file, 'w') as f:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
      max_id = new_tweets[-1].id
      tweet_count += len(new_tweets)
    except tweepy.TweepError as e:
      # Just exit if any error
      print("Error : " + str(e))
      break
  print (f"Downloaded {tweet_count} tweets.")
  return all_tweets


# Set a Lat Lon
latlng = '42.359416,-71.093993' # Eric's office (ish)
# Set a search distance
radius = '5mi'
# See tweepy API reference for format specifications
geocode_query = latlng + ',' + radius
# set output file location
file_name = 'data/tweets.json'
# set threshold number of Tweets. Note that it's possible
# to get more than one
t_max = 2000

#downloading 80000 tweets took over 3 hours, make sure not to run this accidentally
tweets = get_tweets(
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name
)

#Run this line after running the code
tweets.to_json('C:/Users/Yael nidam/Dropbox (MIT)/00_2018_Spring/03_Big_Data/10_github/big-data-spring2018/week-04/data/tweets_sample.json')

# Check how many tweets were Downloaded
len(tweets)
tweets.shape
tweets.head()


# def for cleaning location
def cleanloc(x):
    bos_list = x[x['location'].str.contains("Boston", case=False)]['location']
    x['location'].replace(bos_list, 'Boston, MA', inplace = True)

    cambridge_list = x[x['location'].str.contains("Cambridge", case=False)]['location']
    x['location'].replace(cambridge_list, 'Cambridge, MA', inplace = True)

    usa = x[x['location'].str.contains("united States", case=False)]['location']
    x['location'].replace(usa, 'USA', inplace = True)

    mass = x[x['location'].str.contains("massachusetts", case=False)]['location']
    x['location'].replace(mass, 'MA', inplace = True)

cleanloc(tweets)

#count the amount of tweets per specific location
tweets[tweets['location'].str.contains('toronto')].groupby('location')['id'].count()

# Count of tweets by location
tweets['location'].value_counts()

#clean duplicates
tweets[tweets.duplicated(subset = 'content', keep = False)]
tweets.drop_duplicates(subset = 'content', keep = False, inplace = True)

# loc_tweets = tweets[tweets['location'] != '']
# count_tweets = loc_tweets.groupby('location')['id'].count()
# count_tweets
# df_count_tweets = count_tweets.to_frame()
# df_count_tweets.columns
# df_count_tweets.columns = ['count']
# df_count_tweets
# df_count_tweets.sort_index()

#dataframe from series
yael = tweets['location'].value_counts().to_frame()
yael
# mask for location count > 5
yael2=yael[yael['location']>5]
#remove rows with no location
yael_chart=yael2.drop([''])

# Create a list of colors (from iWantHue)
colors = ["#697dc6","#5faf4c","#7969de","#b5b246",
          "#cc54bc","#4bad89","#d84577","#4eacd7",
          "#cf4e33","#894ea8","#cf8c42","#d58cc9",
          "#737632","#9f4b75","#c36960"]

# Create a pie chart
plt.pie(yael_chart['location'], labels=yael_chart['location'].keys(), shadow=False, colors=colors)
plt.axis('equal')
plt.tight_layout()
plt.show()

# Trying to understand latlng
tweets['lat'].min()
tweets[tweets['lat']!='NaN']
tweets['lat'].max()
#Finding there are only 9 tweets with latlng values
geoloc=tweets[tweets['lat']==tweets['lat'].max()]
geoloc=tweets[tweets['lat']<0]
len(geoloc)
geoloc

#create scatterplot of all the tweets that are geolocated (i.e. 9 tweets)
scatter_geo1=tweets[tweets['lat']<0]
scatter_geo1.plot.scatter(x='lat', y='lon', s=len(geoloc)*3, alpha=0.6, title ="Scatterplot of latitude and longitude of tweets")

#remove empty location and save to csv
withloc1=tweets[tweets['location']!='']
withloc1.to_csv('tweets.csv', sep=',', index=False)



## Definitions for new search with search tern 'housing'
# Set a Lat Lon

latlng = '42.359416,-71.093993' # Eric's office (ish)
# Set a search distance
radius = '5mi'
# See tweepy API reference for format specifications
geocode_query = latlng + ',' + radius
# set output file location
file_name = 'data/tweets2.json'
# set threshold number of Tweets. Note that it's possible
# to get more than one
t_max = 2000

tweets2 = get_tweets(
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name,
  search_term = 'housing'
)

#Run this line after running the code
tweets.to_json('C:/Users/Yael nidam/Dropbox (MIT)/00_2018_Spring/03_Big_Data/10_github/big-data-spring2018/week-04/data/tweets2.json')

# Check how many tweets were Downloaded
len(tweets2)
tweets2.shape
tweets2.head()

#clean location
cleanloc(tweets2)
tweets

# Count of tweets by location
tweets2['location'].value_counts()

#dataframe from series
housing = tweets2['location'].value_counts().to_frame()
housing
# mask for location count > 9
housing2=housing[housing['location']>=9]
housing2
#remove rows with no location
housing3=housing2.drop([''])
housing3
#It's impossible to create a scatterplot for this sample, because there are no latlng values
scatter_geo2=tweets2[tweets2['lat']<0]
len(scatter_geo2)

#remove empty location and save to csv
withloc=tweets2[tweets2['location']!='']
withloc.to_csv('housing.csv', sep=',', index=False)
