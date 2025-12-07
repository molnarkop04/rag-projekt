import streamlit as st
import os
from dotenv import load_dotenv
from llama_index.core import StorageContext, load_index_from_storage, VectorStoreIndex
from daten_laden import dokumente_einlesen

load_dotenv()
speicher = "./storage"

st.set_page_config(page_title="KI-Assistent", page_icon=None)
st.title("WALL E - Assistent")

@st.cache_resource
def lade_suchmaschine():

    if not os.path.exists(speicher):
        return None
    
    uebergabe = StorageContext.from_defaults(persist_dir=speicher)
    index = load_index_from_storage(uebergabe)

    return index.as_query_engine()

def index_neu_bauen():

    with st.spinner("Lese PDFs und baue Index... (Das kostet Geld bei OpenAI)"):

        docs = dokumente_einlesen()
        index = VectorStoreIndex.from_documents(docs)
        index.storage_context.persist(persist_dir=speicher)
        st.success("Index erfolgreich neu erstellt!")

        return index.as_query_engine()

with st.sidebar:
    st.header("Einstellungen")
    st.write("Lege neue PDFs in den Ordner data und klicke hier:")
    
    if st.button("Index neu erstellen / Aktualisieren"):

        st.session_state.engine = index_neu_bauen()
        st.session_state.messages = []

if "engine" not in st.session_state:
    engine = lade_suchmaschine()
    if engine:
        st.session_state.engine = engine
    else:
        st.info("Kein Index gefunden. Bitte klicke links auf Index erstellen.")
        st.stop()


if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

if frage := st.chat_input("Stelle deine Frage zu den Dokumenten..."):
    
    with st.chat_message("user"):

        st.markdown(frage)

    st.session_state.messages.append({"role": "user", "content": frage})

    with st.chat_message("assistant"):

        with st.spinner("Denke nach..."):

            antwort_objekt = st.session_state.engine.query(frage)
            antwort_text = str(antwort_objekt)
            
            st.markdown(antwort_text)
    
    st.session_state.messages.append({"role": "assistant", "content": antwort_text})
