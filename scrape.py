import os
import pandas as pd
from datetime import datetime

import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from textblob import TextBlob
from wordcloud import WordCloud

import matplotlib.pyplot as plt



class driver:

    stop_words = stopwords.words("english")


    def __init__(self,term):

        self.search_term = term
        self.df = None

    def scrape(self):

        today = datetime.now()
        date = today.strftime("%Y-%m-%d")

        arg = "twitter-search"
        os.system(f'snscrape --jsonl --progress --max-results 200 {arg} "{self.search_term} until:{date}" > text-query-tweets.json')
    
    def get_dataframe(self):

        tweets_df = pd.read_json("text-query-tweets.json", lines=True)
        self.df = tweets_df[["renderedContent"]]

        self.df = self.df.rename(columns={"renderedContent": "tweets"})
    
    def tweet_clean(self,tweet):
        clean_tweet = re.sub(r"@[a-zA-Z0-9]+", "", tweet)  # removes mentions
        clean_tweet = re.sub(
            r"#[a-zA-Z0-9]+\s", "", clean_tweet
        )  # removes hashtags and blank spaces
        clean_tweet = " ".join(
            word for word in clean_tweet.split() if word not in self.stop_words
        )  # removing all the stopwords from the tweet
        return clean_tweet
    
    def clean_tweets(self):
        self.df["cleaned_tweets"] = self.df["tweets"].apply(self.tweet_clean)

    def calcPolarity(self,tweet):
        return TextBlob(tweet).sentiment.polarity

    def calcSubjectivity(self,tweet):
        return TextBlob(tweet).sentiment.subjectivity

    def segmentation(self,polarity):
        if polarity > 0:
            return "positive"
        elif polarity == 0:
            return "neutral"
        else:
            return "negative"
    
    def analysis(self):
        self.df["polarity"] = self.df["cleaned_tweets"].apply(self.calcPolarity)
        self.df["subjectivity"] = self.df["cleaned_tweets"].apply(self.calcSubjectivity)
        self.df["segmentation"] = self.df["polarity"].apply(self.segmentation)
    
    def top_3_positive(self):
        positive = self.df.sort_values(by=["polarity"], ascending=False).head(3)
        return [x for x in positive["tweets"]]
    
    def top_3_negative(self):
        negative = self.df.sort_values(by=["polarity"], ascending=True).head(3)
        return [x for x in negative["tweets"]]

    def generate_wordcloud(self):
        consolidated = " ".join(word for word in self.df["cleaned_tweets"])

        word_cloud = WordCloud(
            width=400, height=200, random_state=20, max_font_size=120
        ).generate(consolidated)

        return word_cloud
    
    
    
    








    
