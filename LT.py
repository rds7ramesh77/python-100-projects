#Python program for  Interractive Language Translator 


""" Language Translator is one of those apps that helped a lot while studying maning language.

Google language Translator API helps us to create our translator using python.

The googletrans API created by Google developers was used earlier to translate any text using python.


But now the new API from the Google developers known as google_trans_new is used for the same task.


"""

from google_trans_new import google_translator
import streamlit as st
translator = google_translator()
st.title("Language Translator")
text = st.text_input("Enter a text")
translate = translator.translate(text, lang_tgt='fr')
st.write(translate)

#To run this program type this in command 
#streamlit run file name.py 