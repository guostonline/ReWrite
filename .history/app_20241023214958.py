import streamlit as st
from stc.my_list import *
from stc.county_list import *

st.write("""
# Ai prompt generate
""")
keyword = st.text_input("Keyword")
col1, col2, col3 = st.columns(3)
#st.page_link("your_app.py", label="Home", icon="🏠")
st.slider.page_link("pages/page1.py", label="Page 1", icon="1️⃣")
st.slider.page_link("pages/page2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")
    
with col1:
    tone_voice_choice = st.selectbox("Tone of Voice", tone_voice)
with col2:
    pov = st.selectbox("Point of View", point_of_view)
with col3:
    country = st.selectbox("County", options=target_country,index=185)

col4,col5 =st.columns(2)
with col4:
    number_words=st.number_input("Words count",min_value=500,max_value=3000,step=500,value=800)
with col5:
    contains_selection=st.multiselect("Contains",options=contains,default=contains)

template=f'''
Objective:
Generate a high-quality, SEO-optimized article targeting {country} using the following keywords: {keyword}. The article should have a compelling and powerful title that attracts readers and performs well in search engine rankings.

Parameters to Customize:

Target Country: {country}
Keywords: {keyword}
Title: Create a beautiful and powerful title incorporating the primary keyword (max 160 caracteres prefere a number and positive word).

tone Voice: {tone_voice_choice}
Point of View (POV): {pov}
Number of Words: {number_words}
Additional Instructions: {contains}

'''
btn=st.button("Generate")
def copy_text_to_clipboard(text):
    import pyperclip
    pyperclip.copy(text)
    st.success("Text copied to clipboard!")

if btn:
    st.write(template)
    st.button("copy", on_click=copy_text_to_clipboard, args=(template,))






