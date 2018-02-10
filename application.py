from flask import Flask, redirect, render_template, request, url_for

import helpers
from analyzer import Analyzer
import os
import sys

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))
        
    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    
    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)
    
    # analyze each tweet and get sentiments frequency
    if(tweets==None):
        positive, negative, neutral = 0.0, 0.0, 0.0
    else:
        positive, negative, neutral = 0.0, 0.0, 0.0
        if(len(tweets)!=0):
            for i in tweets:
                s = analyzer.analyze(i)
                if s > 0:
                    positive+=1
                elif s < 0:
                    negative+=1
                else:
                    neutral+=1
            positive = positive/len(tweets)
            negative = negative/len(tweets)
            neutral = neutral/len(tweets)

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
