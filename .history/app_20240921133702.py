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

template=f'''
Objective:
Generate a high-quality, SEO-optimized article targeting [Target Country] using the following keywords: [Keywords]. The article should have a compelling and powerful title that attracts readers and performs well in search engine rankings.

Parameters to Customize:

Target Country: [Enter the country you are targeting]
Keywords: [List your SEO keywords separated by commas]
Title: Create a beautiful and powerful title incorporating the primary keyword.
Tone: [Select your desired tone]
Voice: [Choose between Active or Passive]
Point of View (POV): [First person, Second person, Third person]
Number of Words: [Specify word count]
Additional Instructions: [Any additional requirements]

'''