
import streamlit as st

st.write("page1")

txt_field=st.text_area("Article")

def split_text_by_words(text, num_words):
    words = text.split()
    for i in range(0, len(words), num_words):
        yield ' '.join(words[i:i + num_words])

def copy_text_to_clipboard(text):
    import pyperclip
    pyperclip.copy(text)
    st.success("Text copied to clipboard!")
# Example usage
num_words = st.number_input("Number of words per chunk", min_value=1, value=1000,step=500)
if st.button("Split Text"):
    chunks = list(split_text_by_words(txt_field, num_words))
    for i, chunk in enumerate(chunks):
        st.write(f"Chunk {i + 1}:")
        st.write(chunk)
        st.button("copy", on_click=copy_text_to_clipboard, args=(template,))
        
