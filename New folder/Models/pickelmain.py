import streamlit as st 
import pickle
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics

st.title("Welcome To Youth Cybersecurity Awareness & CyberBullying Dection")

# Assuming you have loaded your dataset into X_train, X_test, Y_train, Y_test
# Also assuming you have defined vec, best_model, and new_input as per the previous code

st.title("BULLYING DETECTION")
input_test = st.text_input("ENTER WORDS HERE")

button_clicked = st.button("GET TYPE OF BULLY")
if button_clicked:
    # Load your model
    Lrdetect_Model = pickle.load(open('lejone_model.pkl', 'rb'))
    
    # Make prediction
    predicted_label = Lrdetect_Model.predict([input_test])
    
    # Display prediction
    st.text(predicted_label)
