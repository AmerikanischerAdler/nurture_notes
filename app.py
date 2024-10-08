#!/opt/homebrew/bin/python3.11

import requests
from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/journal')
def journal():
    return render_template('journal.html')

@app.route('/editor')
def editor():
    return render_template('editor.html')

if __name__ == '__main__':
    app.run(debug=True)

