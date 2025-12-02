import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex
from daten_laden import dokumente_einlesen

load_dotenv()

def index_bauen():

    dokumente = dokumente_einlesen()
    
    if not dokumente:
        print("Keine Dokumente erhalten.")
        return
    
    index = VectorStoreIndex.from_documents(dokumente)
    
    speicher_ordner = "./storage"

    index.storage_context.persist(persist_dir=speicher_ordner)

if __name__ == "__main__":
    try:
        index_bauen()
    except Exception as e:
        print(f"Fehler. {e}")