from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory

app = Flask(__name__)

@app.route('/home')
def home():    
    return render_template("index.html")