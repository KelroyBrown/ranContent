
#class for posts
class Post:
    def __init__(self, title, image, link):
        self.title = title
        self.image = image
        self.link = link
        
# @Jamaipanese Twitter login for "Jamaipanese" app
import tweepy

consumer_key = 'add your own'
consumer_secret = 'add your own'
access_token = 'add your own'
access_token_secret = 'add your own'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)