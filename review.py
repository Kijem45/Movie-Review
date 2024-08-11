import streamlit as st
import pickle as pk

#load model
pipeline = pk.load(open("model_pipeline.pk1", "rb"))

# streamlit input
review = st.text_input("Enter Movie Review")

if st.button("Predict"):
    #make prediction
    result = pipeline.predict([review])

    #display the result
    if result[0] == 1:
        st.write("Positive review")
    else:
        st.write("Negative Review")