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

col4,col5 =st.columns(2)
with col4:
    number_words=st.number_input("Words count",min_value=500,max_value=3000,step=500,value=800)
with col5:
    contains_selection=st.multiselect("Contains",options=contains,default=contains)


btn=st.button("Generate")

if btn:
    
