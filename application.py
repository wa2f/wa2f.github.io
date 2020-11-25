from flask import Flask, redirect, jsonify, render_template, request, session

app = Flask(__name__)

# login box start here
@app.route("/")
def index():
    return render_template("index.html")

