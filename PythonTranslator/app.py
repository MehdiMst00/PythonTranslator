from flask import Flask, request
from aiogoogletrans import Translator
import asyncio
app = Flask(__name__)

translator = Translator()
loop = asyncio.get_event_loop()

@app.route('/')
def home():
    return "Welcome to translator api!!!"

@app.route('/api/v1/translate', methods=["GET","POST"])
def translate():
    data = {}
    dest = ""
    text = ""

    if request.method == "GET":
        dest = request.args.get('dest')
        text = request.args.get('text')

    elif request.method == "POST":
         dest = request.json.get('dest')
         text = request.json.get('text')
    else:
        return data

    if text is None or dest is None:
        return data

    result = loop.run_until_complete(translator.translate(text, dest=dest))
    data['translatedText'] = result.text

    return data

if __name__ == '__main__':
    app.run()