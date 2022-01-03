from re import S
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
  jum_artikel = []
  for i in range(10): 
    sim[i] = np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)
    jum_artikel.append(i)
  
  jum_value=[]
  # Sort the values 
  sim_sorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)
  # Print the articles and their similarity values
  for k, v in sim_sorted:
    if v != 0.0:
      st.write("Nilai Similaritas:", v)
      with st.expander("Lihat Artikel"):
        st.write(doc[k])
        st.write()
        jum_value.append(v)

  total_artikel=len(jum_artikel)
  relevant_artikel=len(jum_value)
  
  precission = relevant_artikel/total_artikel
  recall = total_artikel / relevant_artikel
  f_score = 2*precission*recall/precission+recall

  st.write( )
  st.write( )

  st.write('precission = ',precission)
  st.write("Recall = ",recall)
  st.write("F-Score = ",f_score)

  