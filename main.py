import streamlit as st
import pickle
import pandas as pd

# Load the saved model
model_file = 'crop_rec.pickle'
loaded_model = pickle.load(open(model_file, 'rb'))

def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    # Make prediction
    prediction = loaded_model.predict([[N, P, K, temperature, humidity, ph, rainfall]])
    return prediction[0]

def main():
    st.title('Crop Recommendation System')
    # Input fields for user to input data
    st.subheader('Enter Environmental Data:')
    N = st.number_input('Nitrogen (N)', min_value=0, max_value=100, value=50)
    P = st.number_input('Phosphorus (P)', min_value=0, max_value=100, value=50)
    K = st.number_input('Potassium (K)', min_value=0, max_value=100, value=50)
    temperature = st.number_input('Temperature', min_value=0, max_value=50, value=25)
    humidity = st.number_input('Humidity', min_value=0, max_value=100, value=50)
    ph = st.number_input('pH', min_value=0.0, max_value=14.0, value=7.0, step=0.1)
    rainfall = st.number_input('Rainfall', min_value=0, max_value=500, value=250)

    # Predict button
    if st.button('Predict'):
        result = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
        st.success(f'The recommended crop is: {result}')

if __name__ == '__main__':
    main()

