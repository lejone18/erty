import streamlit as st 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from joblib import load

st.title("Welcome To Youth Cybersecurity Awareness & CyberBullying Detection")

# Assuming you have loaded your dataset into X_train, X_test, Y_train, Y_test
# Also assuming you have defined vec, best_model, and new_input as per the previous code

st.title("BULLYING DETECTION")
input_test = st.text_input("ENTER WORDS HERE")

button_clicked = st.button("GET TYPE OF BULLY")
if button_clicked:
    # Load your model using joblib
    Lrdetect_Model = load('kha90.joblib')
    
    # Make prediction
    predicted_label = Lrdetect_Model.predict([input_test])
    
    # Display prediction
    st.text(predicted_label)
