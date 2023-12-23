from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import random
load_dotenv()

WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')

app = Flask(__name__)

"""
options = [
    {"color" :"#f82", "label":"Stack"},
    {"color" :"#0bf", "label":"10"},
]
"""



@app.route('/')
def index():
    tele_user = request.args.get('tele_user')
    options = list(request.args.get('options'))
    new_options = []
    for option in options:
            colors = ['#fc0c8e', '#fd8a1a', '#fde334', '#acfb13', '#21d1fd', '#ee0f58', 
                      '#fb7a08', '#fdf12f', '#36e8f3', '#8b1df2',
                      '#e71919', '#fb8637', '#fdef0a', '#57e9f6', '#1683e8']
            #color = "#" + "%06x" % random.randint(0, 0xFFFFFF)
            color = random.choice(colors)
            new_options.append({ "color" : str(color), "label" : str(option)})

    return render_template('index.html', sectors = options, tele_user = tele_user, host = WEBHOOK_HOST)

if __name__ == '__main__':
    app.run(debug=True)
    