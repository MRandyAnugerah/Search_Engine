import streamlit as st
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from crawl import crawl
from preprocessing import preprocessing
from tfidf import tfidf
from similar_articles import get_similar_articles

st.title('Search Engine Sederhana')
st.write()
col1, col2 = st.columns(2)
with col1 : 
    st.markdown('Pada Website : [bola.kompas.com](https://bola.kompas.com/)')
    st.caption('Alfin 201810370311057')
    st.caption('Randy 201810370311051')
    st.caption('Aries 201810370311076')
    st.markdown('Temu Kembali Informasi 7B')
# with col2 : st.image('seach-engine-concept-removebg-preview.png')

a=st.markdown("")
q1 = st.text_input('Masukan pencarian kata :')
vectorizer = TfidfVectorizer()
r = requests.get('https://bola.kompas.com/')

if st.button('searching'):
    # Call the function
    crawling = crawl(r)
    pre = preprocessing(crawling )
    tf_idf= tfidf(pre, vectorizer)
    get_similar_articles(q1, tf_idf, vectorizer, crawling)