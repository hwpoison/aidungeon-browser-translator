from deep_translator import GoogleTranslator
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app)


@app.route('/translate/<text>')
def translate(text):
    from_lang = request.args.get('from')
    to_lang = request.args.get('to')
    translator = GoogleTranslator(from_lang, to_lang)

    if from_lang is None or to_lang is None or text is None:
        return jsonify({'error': 'Missing parameters'}), 400 

    translation = translator.translate(text.replace(':', '='))
    if translation is None:
        translation = text

    translation = translation.replace("=",":") # for chat style translation
    return jsonify({'translation': translation}), 200

if __name__ == '__main__':
    app.run()