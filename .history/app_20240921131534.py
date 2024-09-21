import streamlit as st
from stc.my_list import *

st.write("""
# Ai prompt generate
""")
col1, col2, col3 = st.columns(3)

    
with col:
    tone_voice_choice = st.selectbox("Tone of Voice", tone_voice)
with col3:
    pov = st.selectbox("Point of View", point_of_view)
