

#file with class and twitter credentials
from engine import *

#random number generationa and csv file manipulation
import random, csv

#empty variables
post = ""
title = ""
image = ""
link = ""

#seperator for output
seperator = " - "

#random number from 0 to 9 (10 numbers)
random = random.randint(0,9)

#get posts from csv file and choose one at random
with open('posts.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line = 0
    for row in csv_reader:
        if line == random:
            title = row["title"]
            image = row["image"]
            link = row["link"]
        line += 1
    print(f'Processed {line} lines.')

#inset data from csv file to create post class
post = Post(title, image, link)

#tweet text content
tweet = post.title + seperator + post.link

#upload image to twitter TWEEPY 4.0
image = api.simple_upload(image)

#send tweet to twitter with image id from upload above TWEEPY 4.0
api.update_status(tweet, media_ids = [image.media_id])

# checking variables on console
print(post.title)
print(post.image)
print(post.link)
print(random)
print(tweet)

#RESOURCES
#https://www.geeksforgeeks.org/self-in-python-class/
#https://www.pythoncentral.io/how-to-generate-a-random-number-in-python/
#https://realpython.com/python-csv/