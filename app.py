"""Flask app.

An app that uses the QuoteEngine and MemeGenerator modules
to generate a random captioned image or
to create a user defined meme.
"""

import os
import random
import requests
from flask import Flask, render_template, abort, request
from PIL import UnidentifiedImageError

from QuoteEngine import Ingestor
from MemeGenerator import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs.extend([os.path.join(root, name) for name in files])

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    if request.method == 'POST':
        image_url = request.form['image_url']
        body = request.form['body']
        author = request.form['author']

        tmp = './tmp/tmp_app.png'
        try:
            r = requests.get(image_url)
            with open(tmp, 'wb') as img:
                img.write(r.content)
            path = meme.make_meme(tmp, body, author)
            os.remove(tmp)
            return render_template('meme.html', path=path)
        except UnidentifiedImageError:
            abort(400, description='Invalid URL for the meme image')
    path = None
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
