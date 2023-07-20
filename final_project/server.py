from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_en = translator.english_to_french(textToTranslate)
    # Write your code here
    return "Translated text to French is: " + translated_en
@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_fr = translator.french_to_english(textToTranslate)
    return "Translated text to English is: " + translated_fr

@app.route("/")
def renderIndexPage():
    # Write the code to render template
       return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
