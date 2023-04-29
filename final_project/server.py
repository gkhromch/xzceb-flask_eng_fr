from machinetranslation import translator
from flask import Flask, render_template, request
from machinetranslation import french_to_english, english_to_french
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return french_to_english(textToTranslate)

@app.route("/") 
def renderIndexPage():
    print("I'm here")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
