from flask import Flask, render_template, request
from app import app

@app.route("/")
def index_view():
    return render_template('index.html')

