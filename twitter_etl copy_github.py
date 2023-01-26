import pandas as pd
import tweepy
import json
from datetime import datetime
import s3fs

def run_twitter_etl():

    access_key = "xxxxxxxxxxxx"
    access_secret = "xxxxxxxxxxxxxxxxx"
    consumer_key = "xxxxxxxxxxxxxxxxxxxx"
    consumer_secret = "xxxxxxxxxxxxxxxxxx"

    #establishing connection between local system and twitter api
    #twitter authentication

    auth = tweepy.OAuthHandler(access_key,access_secret)
    auth.set_access_token(consumer_key,consumer_secret)


    #creating an api object
    # helps us to access functions inside twitter api 
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name='@elonmusk',#we are fetching tweets from elon musks account
                            count=200,# no of tweets
                            include_rts = False,#we can also extract tweets which are retweeted
                            tweet_mode ='extended'#to get the entire extended tweet
                            )
    # print(tweets)
    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user":tweet.user.screen_name,
                        'text':text,
                        'favorite_count':tweet.favorite_count,
                        'retweet_count':tweet.retweet_count,
                        'created_at' :tweet.created_at
                    }

        tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    #df.to_csv("elonmusk_twitter_data.csv")
    df.to_csv("s3://twitter-airflow-ansel/elonmusk_twitter_data.csv")
#run_twitter_etl()