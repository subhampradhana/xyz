import pandas as pd
import tweepy
import json
from datetime import datetime
import s3fs

access_key = "upn201JaNotMdtFAReieRoUqS"
access_secret = "HO45XfATfJx8HquP0JgPBwzBhUqY4cjcvJ8kz5t1kWtQSKPEIN"
consumer_key = "1417744537-tiLNQrefivYFUsKFBPNLYs19NMUE1JDOn5GR7c2"
consumer_secret = "c4tEELu1foIr62i6oP8W0EzoJeD2ICcHPGDPcaEad6Vun"

# Twitter authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# Creating a twitter API
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name = "@RNTata2000",
                            # 200 is the maximum allowed count
                            count = 200,
                            include_rts = False,
                            # necessary to keep full_text
                            tweet_mode = 'extended' 
                            )

tweets_list = []
for tweet in tweets:
    text = text._json["full_text"]
    
    refined_tweets = {"user": tweet.user.screen_name,
                      'favorite_count':tweet.favorite_count,
                      'retweet_count': tweet.favorite_count,
                      'created_at':tweet.created_at}
    tweets_list.append(refined_tweets)

df = pd.DataFrame(tweets_list)
df.to_csv('ratan tata tweet history')