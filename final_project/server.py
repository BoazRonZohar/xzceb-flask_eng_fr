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
    text_to_translate = request.args.get('text_to_translate')
    # translates English to French
    translated_text_to_french = translator.english_to_french(text_to_translate)
    return translated_text_to_french

# defines the route and the method to translate English to French
@app.route('/frenchToEnglish')
def french_to_english():
    """
    method invoked to translate French text to English
    """
    # gets the text to translate
    text_to_translate = request.args.get('text_to_translate')
    # translates French to English
    translated_text_to_english = translator.french_to_english(text_to_translate)
    return translated_text_to_english

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
