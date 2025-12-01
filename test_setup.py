# KI-Testskript zur Überprüfung der OpenAI-Integration

import os
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

print("--------------------------------------------------")
if not api_key:
    print("❌ FEHLER: Key nicht gefunden!")
else:
    print(f"✅ Key gefunden: {api_key[:5]}...")
    print("⏳ Teste Verbindung zu OpenAI...")
    
    try:
        # Wir nutzen gpt-3.5-turbo
        llm = OpenAI(model="gpt-3.5-turbo")
        response = llm.complete("Sag die Summe von 2+42.")
        
        print(f"🤖 OpenAI antwortet: {response}")
        print("--------------------------------------------------")
        print("🎉 SUCCESS: Dein System läuft!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
print("--------------------------------------------------")