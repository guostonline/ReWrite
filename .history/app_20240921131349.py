import streamlit as st
from stc.my_list import *

st.write("""
# Ai prompt generate
""")
st.columns=
keyword=st.text_input("Keyword")
tone_voice_chouse=st.selectbox("tone_voice",tone_voice)
pov=st.selectbox("Point of view",point_of_view)