import numpy as np
import streamlit as st

def get_similar_articles(q, df, vec, doc):
  st.write("query:", q)
  st.write("Berikut artikel dengan nilai cosine similarity tertinggi: ")
  # Convert the query become a vector
  q = [q]
  q_vec = vec.transform(q).toarray().reshape(df.shape[0],)
  sim = {}
  #Calculate the similarity
  for i in range(10): 
    sim[i] = np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)

  # Sort the values 
  sim_sorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)
  # Print the articles and their similarity values
  for k, v in sim_sorted:
    if v != 0.0:
      st.write("Nilai Similaritas:", v)
      with st.expander("Lihat Artikel"):
        st.write(doc[k])
        st.write()