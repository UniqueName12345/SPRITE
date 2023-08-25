import scratchattach as scr
import flask

@app.route("/")
def root():
    return flask.render_template("index.html")