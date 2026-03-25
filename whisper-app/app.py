import os 
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key = os.getenv('API_KEY'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods = ['POST'])
def upload_audio():
    pass

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5123, debug = True)