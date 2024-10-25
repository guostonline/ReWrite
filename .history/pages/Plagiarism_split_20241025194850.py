import streamlit as st
import pyperclip

st.write("Split article for free Plagiarism")

txt_field = st.text_area("Article")
num_words_in_text = len(txt_field.split())
st.write(f"Number of words in the article: {num_words_in_text}")

def split_text_by_words(text, num_words):
    words = text.split()
    return [' '.join(words[i:i + num_words]) for i in range(0, len(words), num_words)]

def copy_text_to_clipboard(text):
    pyperclip.copy(text)
    st.success("Text copied to clipboard!")

num_words = st.number_input("Number of words per chunk", min_value=1, value=1000, step=500)
if st.button("Split Text"):
    chunks = split_text_by_words(txt_field, num_words)
    
    for i, chunk in enumerate(chunks):
        st.write(f"Paragraph {i + 1}:")
        st.write(chunk)
        st.button("Copy", on_click=copy_text_to_clipboard, args=(chunk,), key=i)
        st.divider()
        
