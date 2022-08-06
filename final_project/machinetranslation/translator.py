"""
This module translates English text to French text
and French text to English text using IBM Watson Language translator
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

# imports apikey and url of IBM Watson Language translator from .env file
apikey = os.environ['apikey']
url = os.environ['url']

# IBM Watson Language translator IAMAuthenticator
authenticator = IAMAuthenticator(apikey)

# an instance of the IBM Watson Language translator
language_translator = LanguageTranslatorV3(
    version ='2022-08-03',
    authenticator = authenticator
)

language_translator.set_service_url(url)

# function to translate English text to French text using IBM Watson Language translator
def english_to_french(english_text):
    """
    translate English text to French text using IBM Watson Language translator
    """
    french_text = language_translator.translate(english_text,model_id='en-fr').get_result()
    # returns translation to French
    return french_text['translations'][0]['translation']

# function to translate French text  to English text using IBM Watson Language translator
def french_to_english(french_text):
    """
    translate French text to English text using IBM Watson Language translator
    """
    english_text = language_translator.translate(french_text,model_id='fr-en').get_result()
    # returns translation to English
    return english_text['translations'][0]['translation']

# Tests the functions
print('Sun in French is: ', english_to_french('sun'))
print('Street in French is:', english_to_french('street'))
print('How wre you? in French is:', english_to_french('How are you?'))
print('Soleil in English is: ', french_to_english('sun'))
print('rue in English is:', french_to_english('rue'))
print('Comment es-tu? in English is:', french_to_english('Comment vas-tu?'))