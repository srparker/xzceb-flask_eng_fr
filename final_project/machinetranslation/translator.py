"""Translate text between languages using mymemory translator"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate English into French
    """
    french_text = MyMemoryTranslator(source="english", target="french").translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translate French into English
    """
    english_text = MyMemoryTranslator(source="french", target="english").translate(french_text)
    return english_text

if __name__ == "__main__":
    print(french_to_english("""Bonjour"""))
