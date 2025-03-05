import streamlit as st
from textblob import TextBlob
st.sidebar.title("about")
st.sidebar.markdown("**david soni**")
# st.sidebar.head("menu")
st.sidebar.title("contact us")
st.sidebar.text("david @ 9991223125 \n khushboo @ 112222 \n Seema @ 3332224")
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
