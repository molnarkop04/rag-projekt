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
        docs = dokumente_einlesen()
        print(docs)
        print(docs[0].text[:200] + "...")
    
            
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")