from deep_translator import GoogleTranslator

def translate_text(text, source_lang, target_lang):
    """
    Translate text from one language to another using the Google Translate API.

    Args:
        text (str): The text to be translated.
        source_lang (str): The source language code (e.g., 'en', 'es', 'fr').
        target_lang (str): The target language code (e.g., 'es', 'fr', 'en').

    Returns:
        str: The translated text.
    """
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    translation = translator.translate(text)
    return translation

if __name__ == "__main__":
    # Example usage
    input_text = "Hello, how are you?"
    source_language = "en"
    target_language = "es"

    translated_text = translate_text(input_text, source_language, target_language)
    print(f"Original text: {input_text}")
    print(f"Translated text: {translated_text}")
