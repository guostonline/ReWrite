import streamlit as st
from stc.my_list import *
from stc.county_list import *

st.write("""
# Ai prompt generate
""")
keyword = st.text_input("Keyword")
col1, col2, col3 = st.columns(3)

    
with col1:
    tone_voice_choice = st.selectbox("Tone of Voice", tone_voice)
with col2:
    pov = st.selectbox("Point of View", point_of_view)
with col3:
    country = st.selectbox("County", options=target_country,)

col4,col5 =st.columns(3)
with number_words=st.number_input("Words count",min_value=500,max_value=3000,step=500,value=800)
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