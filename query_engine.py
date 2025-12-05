import os
from dotenv import load_dotenv
from llama_index.core import StorageContext, load_index_from_storage

load_dotenv()

def chat_starten():
    
    speicher_ordner = "./storage"
    
    if not os.path.exists(speicher_ordner):
        return

    uebergabe = StorageContext.from_defaults(persist_dir=speicher_ordner)
    index = load_index_from_storage(uebergabe)

    query_engine = index.as_query_engine()
    
    print("PDF wurde gelesen.")
    print("q oder exit zum Beenden eintippen.")
    
    while True:
        frage = input("Deine Frage: ")
        
        if frage.lower() in ["q", "exit"]:
            break
            
        if not frage.strip():
            continue
            
        print("Suche nach Antworten...")
        
        try:
            antwort = query_engine.query(frage)
            
            print(f"Antwort: {antwort}")
            print("-" * 40)
            
        except Exception as e:
            print(f"Fehler bei der Antwort: {e}")

if __name__ == "__main__":
    chat_starten()
