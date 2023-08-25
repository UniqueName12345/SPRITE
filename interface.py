import scratchattach as scr
from flask import Flask, render_template, request
app = Flask(__name__)

def with_offset(function):
    offset = 0
    result = []
    while True:
        returned = function(offset=offset)
        if not returned:
            break
        result += returned
        offset += 40
    return result

def load_user_data(username):
    user = scr.get_user(username)
    followers = with_offset(user.followers)
    following = with_offset(user.following)
    comment_count = len(user.comments())
    projects = with_offset(user.projects)

    return user, {
        "followers": followers,
        "following": following,
        "comment_count": comment_count,
        "projects": projects
    }

@app.route("/users/<username>")
def user(username):
	user, info = load_user_data(username)
	return render_template("user.html", user=user, info=info, len=len)

@app.route("/")
def root():
    return render_template("root.html")

if __name__ == "__main__":
    app.run(debug=True)