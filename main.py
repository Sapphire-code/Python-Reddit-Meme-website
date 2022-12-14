""" from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Drink water bro"

app.run(host="127.0.0.1", port=80) """

from urllib import request, response
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    subreddit = "/wholesomememes"
    # url = "https://meme-api.herokuapp.com/gimme" + sr
    # This fetches memes from all over reddit, which CAN be NSFW, please make sure to uncomment the line below and comment the line below it
    # url = "https://meme-api.com/gimme" + subreddit
    # comment the line below to disable NSFW posts.
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic = meme_pic, subreddit = subreddit)


app.run(host="127.0.0.1", port=80)
