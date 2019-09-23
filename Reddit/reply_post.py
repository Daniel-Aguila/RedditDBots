#!/usr/bin/python
import praw
import pdb
import prawcore
import re
import os


# Create the Reddit instance
reddit = praw.Reddit('bot1')
print(reddit.user.me())
#Assume file doesn't exist
if not os.path.isfile("posts_reply_to.txt"):
    posts_replied_to =[]
    #Create an empty list
else:

    #The 'with' keyword, opens the file, closes it, and handle any errors
    #so no need for try-catch blocks
    with open("post_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        #separates the posts by new line
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit("SquirrelsUH")

for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        #re.IGNORECASE ignores wether the letters are in capital or not, or amix
        if re.search("i love python", submission.title, re.IGNORECASE):
            #write the reply
            #reply() is a function that adds a comment to the current submission
            submission.reply("NO, YOU MUST LOVE C++!")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

#Now we write to remember the id to our list
with open("post_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")