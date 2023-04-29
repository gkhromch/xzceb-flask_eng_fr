import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Set up the authenticator
auth = IAMAuthenticator(apikey)

# Create the Language Translator instance
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = auth
)

# Set the service URL
language_translator.set_service_url(url)

def english_to_french(english_text = ''):
    if not english_text:
        return ''

    res = language_translator.translate(
        text = english_text,
        model_id = 'en-fr'
    ).get_result()

    return res['translations'][0]['translation']


def french_to_english(french_text = ''):
    if not french_text:
        return ''

    res = language_translator.translate(
        text = french_text,
        model_id = 'fr-en'
    ).get_result()

    return res['translations'][0]['translation']
