from flask import Flask, request
from machinetranslation import translator

app = Flask("My translation app", static_folder ="static")

@app.route('/')
def hello():
    return "Hello World"

@app.route('/englishToFrench', methods=['GET'])
def translateEnglishFench(english):
    args = request.args
    englishText = args.get('englishText')
    french = translator.english_to_french(englishText)
    return(french)

@app.route('/frenchToEnglish', methods=['GET'])
def translateFenchEnglish(french):
    args = request.args
    frenchText = args.get('frenchText')
    english = translator.french_to_english(frenchText)
    return(english)

if __name__ == "__main__":
    app.run(debug=True)
