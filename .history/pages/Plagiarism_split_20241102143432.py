import streamlit as st
import pyperclip
import clipboard
import requests
from bs4 import BeautifulSoup
st.write("Split article for free Plagiarism")




url = st.text_input("Enter the URL of the article")

def fetch_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        article_text = ' '.join([para.get_text() for para in paragraphs])
        return article_text
    else:
        st.error("Failed to fetch the article. Please check the URL and try again.")
        return ""

if st.button("Fetch Article"):
    fetched_article = fetch_article(url)
    if fetched_article:
        st.session_state.fetched_article = fetched_article
        st.echo("Article fetched successfully!")

if 'fetched_article' in st.session_state:
    txt_field = st.text_area("Article", st.session_state.fetched_article,key="url")
else:
    txt_field = st.text_area("Article",key="url")

num_words_in_text = len(txt_field.split())
st.write(f"Number of words in the article: {num_words_in_text}")

def split_text_by_words(text, num_words):
    words = text.split()
    return [' '.join(words[i:i + num_words]) for i in range(0, len(words), num_words)]

def copy_text_to_clipboard(text):
    clipboard
    pyperclip.copy(text)
    st.success("Text copied to clipboard!")

num_words = st.number_input("Number of words per chunk", min_value=1, value=1000, step=500)

if 'chunks' not in st.session_state:
    st.session_state.chunks = []

if st.button("Split Text"):
    st.session_state.chunks = split_text_by_words(txt_field, num_words)

for i, chunk in enumerate(st.session_state.chunks):
    st.write(f"Paragraph {i + 1}:")
    with st.container(height=500):
        st.code(chunk)
        #st.button("Copy", on_click=copy_text_to_clipboard, args=(chunk,), key=f"copy_{i}")
        st.divider()
