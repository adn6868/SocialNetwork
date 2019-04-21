from flask import Flask, render_template
import markdown
import os
# ENV PYTHONPATH / test_project


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/googleSignin')
def googleSignin():
    return render_template('googleSignin.html')


@app.route('/facebookSignin')
def facebookSignin():
    return render_template('facebookSignin.html')


@app.route('/blogs')
def blogs():
    return render_template('blogs.html', blogs=blogs)
