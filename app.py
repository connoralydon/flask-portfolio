# app.py


import sys
from flask import Flask, render_template, url_for, request, redirect
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
from datetime import datetime

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md" # post-fix
FLATPAGES_ROOT = "content" # where to find data for flatpages
POSTS_DIR = "posts"
PORTFOLIO_DATA_PATH = "portfolio" # flatpages doens't need the md



app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__) # to set project fongi settings

# index/portfilio
@app.route("/")
def index():
    # include two most recent blog posts
    # include two most recent projects 
    
    portfolio_data = flatpages.get_or_404(PORTFOLIO_DATA_PATH)
    return render_template("index.html", portfolio_data=portfolio_data)

# blog index page
@app.route("/posts/")
def posts():
    # iterating through flatpages if the path starts with desired directory
    posts = [p for p in flatpages if p.path.startswith(POSTS_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=False) # sorting oldest to newest
    return render_template('posts.html', posts=posts)
    # 

# blogpost
@app.route("/posts/<name>/")
def post(name):
    path = f"{POSTS_DIR}/{name}"
    post = flatpages.get_or_404(path)
    return render_template("post.html",post=post)


# running dev or build
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] =="build":
        freezer.freeze()
    else: # dev
        app.run(host="0.0.0.0", port=80, debug=True)