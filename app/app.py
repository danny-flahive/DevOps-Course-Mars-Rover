from flask import Flask, render_template, request, redirect, url_for
from app.api_caller import get_image_url


app = Flask(__name__)

@app.route('/')
def index():
    image_url=get_image_url()
    return render_template('index.html', landing_image=image_url)

@app.route('/mars')
def mars():
    return render_template('mars.html')