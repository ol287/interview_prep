from deep_translator import GoogleTranslator

class Translator:
    def __init__(self, source_lang, target_lang):
        """
        Initializes the Translator class with source and target languages.

        Args:
            source_lang (str): The source language code (e.g., 'en', 'es', 'fr').
            target_lang (str): The target language code (e.g., 'es', 'fr', 'en').
        """
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.translator = GoogleTranslator(source=source_lang, target=target_lang)
        self.cache = {}

    def translate(self, text):
        """
        Translates text from the source language to the target language, using caching to avoid repeated translations.

        Args:
            text (str): The text to be translated.

        Returns:
            str: The translated text.
        """
        if text in self.cache:
            return self.cache[text]

        translation = self.translator.translate(text)
        self.cache[text] = translation
        return translation

    def change_language(self, source_lang=None, target_lang=None):
        """
        Changes the source or target language.

        Args:
            source_lang (str, optional): The new source language code.
            target_lang (str, optional): The new target language code.
        """
        if source_lang:
            self.source_lang = source_lang
        if target_lang:
            self.target_lang = target_lang
        self.translator = GoogleTranslator(source=self.source_lang, target=self.target_lang)

if __name__ == "__main__":
    # Example usage
    translator = Translator("en", "es")
    input_text = "Hello, how are you?"
    translated_text = translator.translate(input_text)
    print(f"Original text: {input_text}")
    print(f"Translated text: {translated_text}")

    # Example of changing languages
    translator.change_language(target_lang='fr')
    translated_text = translator.translate(input_text)
    print(f"Translated to French: {translated_text}")
