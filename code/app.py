import os

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello():
    bg_color = os.getenv('BG_COLOR','black')
    text_color = os.getenv('TEXT_COLOR','white')
    return render_template('index.html', name='My flask project', BG_COLOR = bg_color, TEXT_COLOR = text_color )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
