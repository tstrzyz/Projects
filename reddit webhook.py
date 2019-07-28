import requests
import praw
import time
n = """https://www.reddit.com/?state=good&code=3S-XMiO3LQs7ZK-GNTMedRKte1M
https://www.reddit.com/api/v1/authorize?client_id=iuTJp7rcVqQQMg&response_type=code&
    state=good&redirect_uri=https://www.reddit.com/&duration=permanent&scope=identity, edit, flair, history, modconfig, modflair, modlog, modposts, modwiki, mysubreddits, privatemessages, read, report, save, submit, subscribe, vote, wikiedit, wikiread"""

reddit = praw.Reddit(client_id='iuTJp7rcVqQQMg',
                     client_secret='eXM3qVr5EXSi4naJrg7PEeyAXHM',
                     redirect_uri='https://www.reddit.com/',
                     user_agent='testscript by /u/tstrzyz',
                     refresh_token='51759624691-4xxI7kOCEk9_zWxmJhdJ5vUi6q0'
                     )


subreddit = reddit.subreddit("hentai")
for submission in subreddit.hot(limit=None):
    requests.post(url="""https://discordapp.com/api/webhooks/604070862064451600/_xEU6u03l31TQwREqIOQuTSoRyqqsid5pFHgkaNtMgDFEXgRetSanxr4tlkRmeMdb1ks"""
    ,data={"content":("{} {}").format(submission.title,submission.url)})
    time.sleep(60)

