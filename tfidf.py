import streamlit as st
import pandas as pd

def tfidf(documents_clean, vec):
    # Instantiate a TfidfVectorizer object
    # It fits the data and transform it as a vector
    X = vec.fit_transform(documents_clean)
    # Convert the X as transposed matrix
    X = X.T.toarray()
    # Create a DataFrame and set the vocabulary as the index
    df = pd.DataFrame(X, index=vec.get_feature_names())
    st.dataframe(df)
    return df