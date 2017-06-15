import re
import csv
import praw
import datetime

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("all")

comment_log_file = "pinkguys_reply_log.csv"


def save_reply(reply):
    with open(comment_log_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(reply)
# end def save_reply

for comment in subreddit.stream.comments():
    if comment.author != "pinkguybot":
        for name in ['Filthy Frank', 'Joji', 'George Miller', 'Franku', 'TVFilthyFrank', 'Pink Guy',
                     'Pinkguy', 'DizastaMusic', 'TooDamnFilthy']:
            if re.search(name, comment.body, re.IGNORECASE):
                pink_reply = "Eyy Boss!    http://i.imgur.com/aWm4kcr.jpg"
                try:
                    comment.reply(pink_reply)
                    reply = [str(datetime.datetime.now()), str(comment.id), str(name), str(comment.subreddit)]
                    save_reply(reply)
                    print(reply)
                except:
                    print("Sorry Boss!")
                break
