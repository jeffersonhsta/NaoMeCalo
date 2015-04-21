from flask import Flask, send_file

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
  return send_file('./index.html')

