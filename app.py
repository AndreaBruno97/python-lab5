from flask import Flask, render_template, redirect, url_for, request, session
import db_interaction
app = Flask(__name__)

@app.route('/')
def inizio():
    return redirect(url_for("index"))

@app.route('/index')
def index():
    return  render_template("index.html")


if __name__ == '__main__':
    app.run()
