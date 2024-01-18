import streamlit as st
import pickle

# Function to load the trained model
def load_trained_model():
    model_path = 'best_model.pickle'

    try:
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        return model
    except FileNotFoundError:
        st.error(f"Error: Model file '{model_path}' not found.")
        return None
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Function to predict using the loaded model
def predict(input_data, model):
    try:
        prediction = model.predict(input_data)[0]
        return f'Predicted Iris Species: {prediction}'
    except Exception as e:
        return f"Error predicting: {e}"

# Streamlit app
st.title('Iris Flower Prediction App')

# Input attributes
sepal_length = st.slider('Sepal Length', min_value=0.0, max_value=10.0, value=5.0)
sepal_width = st.slider('Sepal Width', min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.slider('Petal Length', min_value=0.0, max_value=10.0, value=1.5)
petal_width = st.slider('Petal Width', min_value=0.0, max_value=10.0, value=0.2)

# Load the trained model
model = load_trained_model()

# Button to submit prediction
if st.button('Submit'):
    if model is not None:
        input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
        result = predict(input_data, model)
        st.success(result)

# Display NIM and name
st.sidebar.text("NIM: 2020230053")
st.sidebar.text("Name: Tri Febriyanto")
