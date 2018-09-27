import praw
import random 

#Client_ID & Secret, Passoword, Username
reddit = praw.Reddit(client_id = '', client_secret= '', password = '', username = '', user_agent = '' )

#Subreddits which the bot can post on 
subreddit = reddit.subreddit("weirdlittlebot")

# Keyphrase which calls the bot. 
keyphrase = "!DankMeme"
keyphrase2 = "!SurrealMeme"

#Function randomly chooses a post from the hot posts from the Dankmemes subreddit
def dankgen():
    links=[]
    submission = reddit.subreddit("DankMemes").hot(limit=10)
    for post in submission:
        links.append(post.url)
    return random.choice(links)

def surrealgen():
    links=[]
    submission = reddit.subreddit("SurrealMemes").hot(limit=10)
    for post in submission:
        links.append(post.url)
    return random.choice(links)

#Main loop, replies to comments containing the keyphrase with a link to the meme. 
while True:
    print("Initializing bot...")
    for comment in subreddit.stream.comments():
        if keyphrase.lower() in comment.body.lower():
            print("Keyphrase detected.")
            meme = dankgen()
            print("Posting meme...")
            comment.reply("[Here's one of the dankest memes I could find]({})".format(meme))
        elif keyphrase2.lower() in comment.body.lower():
            print("Keyphrase detected.")
            meme = surrealgen()
            print("Posting meme...")
            comment.reply("[This meme is totes surreal af]({})".format(meme))
            



    

