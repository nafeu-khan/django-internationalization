import os
from googletrans import Translator
import polib

###---------process-----------------------
# just put this file while locale folder is adjacent 

# pip install polib googletrans==4.0.0-rc1

# python translate_po_files.py


# for language
# django-admin makemessages -l es


#compile from po to mo
# django-admin compilemessages
### -----------------------------

# Function to translate text using Google Translate
def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

# Function to translate a .po file
def translate_po_file(po_file_path, target_language):
    po = polib.pofile(po_file_path)
    for entry in po.untranslated_entries():
        if entry.msgid:  # Ensure the msgid is not empty
            translation = translate_text(entry.msgid, target_language)
            entry.msgstr = translation
    po.save()

if __name__ == "__main__":
    # Specify the locale directory and target language
    locale_dir = "locale/bn" #specify target po files folder . for exmple for bangla locale/bn after "makemessages -l bn"
    target_language = "bn"  # Adjust target language as necessary
    
    # Translate all .po files in the locale directory
    for root, dirs, files in os.walk(locale_dir):
        for file in files:
            if file.endswith(".po"):
                po_file_path = os.path.join(root, file)
                print(f"Translating {po_file_path}")
                translate_po_file(po_file_path, target_language)
                print(f"Translation complete for {po_file_path}")
