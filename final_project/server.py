"""
This server translates English text to French and French text to English
"""
from flask import Flask, render_template, request
from machinetranslation import translator

# creats an object of the flask class as a web application
app = Flask('Web Translator')

# defines the route and the method to translate English to French
@app.route('/englishToFrench')
def english_to_french():
    """
    method invoked to translate English text to French
    """
    # gets the text to translate
    textToTranslate = request.args.get('textToTranslate')
    TranslatedTextToFrench = translator.english_to_french(textToTranslate)
    # translates English to French
    return TranslatedTextToFrench
 
# defines the route and the method to translate English to French
@app.route('/frenchToEnglish')
def french_to_english():
    """
    method invoked to translate French text to English
    """
    # gets the text to translate
    textToTranslate = request.args.get('textToTranslate')
    # translates French to English
    TranslatedTextToEnglish = translator.french_to_english(textToTranslate)
    return TranslatedTextToEnglish

# defines the root route
@app.route("/")
def homepage():
    """
    method that renders the index.html
    """
    return render_template("index.html")

# runs the app on port 8080
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
