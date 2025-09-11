from flask import Flask, render_template
import random
import json
import requests

for i in range(99):
    cord = random.randint(1,100)

r = requests.get('https://api.github.com/events')

app = Flask(__name__)

en_file = "en.json"

@app.route("/")
def index():
    return render_template("index.html", en_file="", cord=cord)

if __name__ == '__main__':
    app.run(debug=True)
