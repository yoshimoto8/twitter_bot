import configparser
import twitter as tw

config = configparser.ConfigParser()
config.read('config.ini')

auth = tw.OAuth(consumer_key=config['twitter_API']['CONSUMER_KEY'],
                consumer_secret=config['twitter_API']['CONSUMER_SECRET'],
                token=config['twitter_API']['TOKEN'],
                token_secret=config['twitter_API']['TOKEN_SECRET'])

t = tw.Twitter(auth=auth)

t.statuses.update(status="pythonからtwitterへの投稿テストです！")
