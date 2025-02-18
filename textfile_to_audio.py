import os
import numpy as np
import scipy.io.wavfile as wav
from bark import generate_audio, SAMPLE_RATE

TEXT_FILE = "text.txt"  # Die Datei mit dem Eingabetext
OUTPUT_FILE = "output.wav"  # Die Ausgabe-Audiodatei
MAX_CHUNK_LENGTH = 300  # Maximale Zeichenanzahl pro Chunk (kann angepasst werden)

def read_text_from_file(filename):
    """Erkennt den Text aus der Datei und teilt ihn in kleinere Absätze auf."""
    if not os.path.exists(filename):
        print(f"⚠️ Datei '{filename}' nicht gefunden! Bitte erstelle sie mit deinem Text.")
        return None
    
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read().strip()
    
    if not text:
        print("⚠️ Die Datei ist leer. Bitte füge Text hinzu.")
        return None
    
    return split_text_into_chunks(text, MAX_CHUNK_LENGTH)

def split_text_into_chunks(text, max_length):
    """Teilt langen Text in kleinere Abschnitte, damit Bark es besser nutzt."""
    sentences = text.replace("\n", " ").split(". ")  # Trenne am Satzende
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= max_length:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def main():
    print("\n Bark AI Sprachsynthese - Text aus Datei")

    text_chunks = read_text_from_file(TEXT_FILE)
    if text_chunks is None:
        return

    print(f"📖 {len(text_chunks)} Textabschnitte gefunden. Generiere Audio...")

    all_audio = []
    for i, chunk in enumerate(text_chunks):
        print(f"🎤 Abschnitt {i+1}/{len(text_chunks)}: {chunk[:50]}...")  # Zeigt nur den Anfang des Textes
        audio_array = generate_audio(chunk)
        all_audio.append(audio_array)

    # Alle generierten Audio-Chunks zusammenfügen
    final_audio = np.concatenate(all_audio)

    # Speichern der kombinierten Audiodatei
    wav.write(OUTPUT_FILE, SAMPLE_RATE, np.int16(final_audio * 32767))

    print(f"✅ Fertig! Die Datei wurde als '{OUTPUT_FILE}' gespeichert.")
    os.system(f'start {OUTPUT_FILE}')  # Öffnet die Datei direkt in Windows

if __name__ == "__main__":
    main()
