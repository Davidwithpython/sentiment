import streamlit as st
from textblob import TextBlob
st.sidebar.title("About me")
st.sidebar.markdown('''
                    **I am a passionate and detail-oriented Sentiment Analyst with a strong background in natural language processing (NLP) and machine learning.
   My expertise lies in analyzing and interpreting textual data to determine sentiment, emotions, and opinions expressed in various forms of communication, such as social media, customer reviews, and news articles.
           develop by david soni**''')
# st.sidebar.head("menu")
st.sidebar.title("Contact us")
st.sidebar.text("David soni - +919991223125 \n chess id - https://www.chess.com/member/Davidsoni123 \n linkedin id - https://linkedin.com/in/David-Soni-13oct2001 \n Instra id - Sonidavid692")
st.title("Sentiment Analysis Project")
name=st.text_input("enter the Sentiment")
bt=st.button("Predict")
if bt:
    tb=TextBlob(name)
    sen=tb.sentiment[0]
    if sen<0:
        st.error("neg")
        st.image("neg.png")
    elif sen>0:
        st.success("pos")
        st.image("pos.png")
    else:
        st.warning("neutral")
        st.image("neu.png")
