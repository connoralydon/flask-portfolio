import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"
FLATPAGES_ROOT = "content" # subfolder where content lies
POST_DIR = "posts" # built up HTML?

app = Flask(__name__) # main
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)

# custom routes for blog logic
@app.route("/posts/") # decorator
def posts():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item:item["date"], reverse=False) # ascending order
    return render_template('posts.html', posts=posts)

@app.route("/posts/<name>/") # rendering each sub template
def post(name):
    path = "{}/{}".format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)




# run command
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze() # freeze development build
    else: # app in deve mode
        app.run(host="0.0.0.0", debug = True)


