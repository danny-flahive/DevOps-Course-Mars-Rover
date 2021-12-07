from flask import Flask, render_template, request, redirect, url_for
from app.api_caller import get_image_info


app = Flask(__name__)

@app.route('/')
def index():
    image_url, image_description = get_image_info()
    return render_template('index.html', landing_image=image_url, image_description=image_description)

@app.route('/mars')
def mars():
    return render_template('mars.html')

@app.route("/request", methods=["GET"])
def request_handler():
    #date = request.form.get("user_dateinput")
    date = request.args.get("user_dateinput")
    image_url, image_description = get_image_info(date)
    return render_template('index.html', landing_image=image_url, image_description=image_description)
