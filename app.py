import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import model_from_json
from tensorflow.keras.utils import plot_model
import os

# Function to create a model from the code input
def create_model_from_code(code_str):
    try:
        # Use exec() to create a model from the code string
        local_vars = {}
        exec(code_str, {}, local_vars)
        
        # Assuming the model is created in the code with a variable name 'model'
        model = local_vars.get('model', None)
        if model:
            return model
        else:
            return "Model not defined correctly."
    except Exception as e:
        return f"Error in creating model: {str(e)}"

# Function to save and display model architecture
def visualize_model(model):
    try:
        # Save the model architecture visualization
        plot_model(model, to_file='model_architecture.png', show_shapes=True, show_layer_names=True)
        return 'model_architecture.png'
    except Exception as e:
        return f"Error in visualizing model: {str(e)}"

# Streamlit interface
st.title("Neural Network Architecture Visualization Tool")
st.write("Paste your model code in the input box below:")

# Input box for model code
model_code = st.text_area("Model Code", height=200)

if st.button("Visualize Architecture"):
    if model_code.strip():
        # Create model from code
        model = create_model_from_code(model_code)
        
        if isinstance(model, str):  # In case of error in creating the model
            st.error(model)
        else:
            # Visualize the model architecture
            model_img_path = visualize_model(model)
            
            if model_img_path.endswith(".png"):
                st.image(model_img_path, caption="Model Architecture")
            else:
                st.error(model_img_path)
    else:
        st.error("Please input valid model code.")
