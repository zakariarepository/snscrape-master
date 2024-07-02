import snscrape.modules.twitter as sntwitter

import pandas as pd

import itertools

df = pd.DataFrame()

tweets = sntwitter.TwitterSearchScraper('"#Elonmusk" ').get_items()

for tweet in tweets :
    print(tweets)
# df = pd.DataFrame(itertools.islice(tweets, 100))

# df = df[['date', 'id', 'content', 'user']]

# df.to_csv( 'scraped-tweets.csv', index=False)