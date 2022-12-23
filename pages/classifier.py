import streamlit as st
import pandas as pd

# Used for loading the model 
from transformers import pipeline

# Load Model and Tokenizer 

def load_model(path_to_model):
    classifier = pipeline("text-classification",path_to_model)
    return classifier


def predict(text, classifier): 
    pred = classifier(text)[0]
    return pred['label'], round(pred['score'],2)

st.markdown("# Classifier Demo")
st.sidebar.header("Classifier Demo")

import os

data_load_state = st.text('Loading ...')
path_to_model = "./skill_classifier/models/bert-best-model/"
model = load_model(path_to_model)
data_load_state.text("Done! (Ready to go)")

print(model)
st.markdown("""
# Skills Classifier 

Welcome to the Demo of German - Skills Classifier. 

Please add a text in German to classify your skills. 

Valid classes are: Soft, Tech or None ( neither of the previous ones)
""")

with st.form(key='classifier_form'):
    text = st.text_area("Add your German text to be classified here!")
    submit = st.form_submit_button(label='Classify my skills')

if submit:    

    if text:
        st.write(f"{text}")
        col1, col2 = st.columns(2)
        pred, score = predict(text, model)
        print(pred, score)

        with col1:
            st.success(f"Skill Predicted: {pred} ")
        with col2: 
            st.success(f"Confidence: {score}")
else:
        st.write("You need to write a Text before submission!")    
