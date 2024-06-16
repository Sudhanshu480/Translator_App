import streamlit as st
from googletrans import Translator, LANGUAGES

translator = Translator()

def translate(text, source, target):
    translation = translator.translate(text, src=source, dest=target)
    return translation.text


st.set_page_config(page_title="Translator App", page_icon=":books:")
st.title("Translator App :books:")
st.subheader("Translate text between different languages instantly...")

st.sidebar.header("Language Selection")
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "Hindi": "hi",
    "German": "de",
    "Chinese (Simplified)": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru",
    "Portuguese": "pt"
}

source_lang = st.sidebar.selectbox("Source Language", options=list(languages.keys()))
target_lang = st.sidebar.selectbox("Target Language", options=list(languages.keys()))

text = st.text_area("Enter text to translate")

if st.button("Translate"):
    if not text:
        st.warning("Please enter text to translate")
    else:
        with st.spinner("Translating..."):
            translated_text = translate(text, languages[source_lang], languages[target_lang])
        st.success("Done!!!")
        st.markdown("### Translation:")
        st.write(translated_text)


st.sidebar.markdown("""
---
### About
This app uses Google's translation service to translate text between different languages. Simply enter your text, select the source and target languages, and click on the translate button to see the translation.
""")


st.sidebar.markdown("""
---
Created by Sudhanshu
""")
