
import os
from langdetect import detect, DetectorFactory
from googletrans import Translator

DetectorFactory.seed = 0  # For consistent language detection

def find_files(root, extensions):
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(extensions):
                yield os.path.join(dirpath, filename)


# Improved: Aggregate language detection over file chunks

# Detect if any non-English content is present (ratio > 0)
def detect_language_aggregate(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    chunks = [chunk for chunk in text.split('\n\n') if chunk.strip()]
    if not chunks:
        return 0.0, 'en'
    non_eng_count = 0
    for chunk in chunks:
        try:
            lang = detect(chunk)
            if lang != 'en':
                non_eng_count += 1
        except:
            continue
    ratio = non_eng_count / max(1, len(chunks))
    try:
        lang = detect(text)
    except:
        lang = 'unknown'
    return ratio, lang

def translate_file(filepath, translator):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    # Split into paragraphs for chunked translation
    chunks = [chunk for chunk in text.split('\n\n') if chunk.strip()]
    translated_chunks = []
    for chunk in chunks:
        try:
            translated = translator.translate(chunk, dest='en').text
        except Exception as e:
            print(f"Error translating chunk in {filepath}: {e}")
            translated = chunk  # Fallback: keep original
        translated_chunks.append(translated)
    translated_text = '\n\n'.join(translated_chunks)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(translated_text)

root_dir = '.'  # or your repo path
extensions = ('.txt', '.md')
translator = Translator()


non_english_files = []
for file in find_files(root_dir, extensions):
    ratio, lang = detect_language_aggregate(file)
    if ratio > 0:
        non_english_files.append((file, lang, ratio))

print("Files with any non-English content found:")
for file, lang, ratio in non_english_files:
    print(f"{file} ({lang}) - {ratio:.2%} non-English")

if non_english_files:
    if input("Do you want to translate these files to English? (y/n): ").lower() == 'y':
        for file, _, _ in non_english_files:
            translate_file(file, translator)
            print(f"Translated: {file}")
else:
    print("No non-English files detected.")