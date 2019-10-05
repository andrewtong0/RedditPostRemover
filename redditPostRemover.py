import praw
import time
import os
import datetime

subredditName = ''          # Subreddit to scan posts on
userName = ''               # Username to scan posts on
titles = []                 # Array of string to match titles against

reddit = praw.Reddit(client_id=os.environ.get('client_id'),
                     username=os.environ.get('praw_username'),
                     password=os.environ.get('praw_password'),
                     client_secret=os.environ.get('client_secret'),
                     user_agent="Remove Post Script")

while True:
    try:
        submissions = reddit.subreddit(subredditName).new(limit=200)
        # submissions = reddit.redditor(userName).submissions.top('all')
        for submission in submissions:
            for title in titles:
                if title in submission.title:
                    print(str(datetime.datetime.now()) + " | Removed post: " + submission.title)
                    submission.mod.remove()
        time.sleep(600)
        # raise Exception("test")
    except:
        print("Error occurred; restarting...")
        pass
