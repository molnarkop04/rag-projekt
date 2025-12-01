import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader

load_dotenv()

def dokumente_einlesen():
    
    if not os.path.exists("./data"):
        print("Der Ordner 'data' existiert nicht.")
        return []

    # Der Reader schaut in den Ordner und holt alles raus (PDFs, Textdateien)
    reader = SimpleDirectoryReader(input_dir="./data")
    dokumente = reader.load_data()
    
    return dokumente

if __name__ == "__main__":
    
    try:
        alle_dokumente = dokumente_einlesen()
        
        if alle_dokumente:
            print(f"Gesamtanzahl der Pakete (Chunks/Seiten): {len(alle_dokumente)}")
            print("="*60)
            
            for index, doc in enumerate(alle_dokumente):
                print(f" Paketnummer: {index + 1}")
                print(f"ID (Intern): {doc.id_}")
                print(f"Metadaten: {doc.metadata}")
                
                text_vorschau = doc.text[:100].replace('\n', ' ')
                print(f"Inhalt: {text_vorschau}...")
                
                print("-" * 60)
                
        else:
            print("Keine Dokumente gefunden.")
            
    except Exception as e:
        print(f"Fehler. {e}")