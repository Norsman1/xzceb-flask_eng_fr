"""
translator.py - Translates text from English to Franch and vice versa
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This function translates the input string english_text to French
    """
    #write the code here
    french_text = MyMemoryTranslator(source='en-US', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    This function translates the input string french_text to English
    """
    #write the code here
    english_text = MyMemoryTranslator(source='french', target='en-GB').translate(french_text)
    return english_text
