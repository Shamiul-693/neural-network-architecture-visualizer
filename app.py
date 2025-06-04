import streamlit as st
import tensorflow as tf
from tensorflow.keras.utils import plot_model

# Function to create a model from the input code
def create_model_from_code(code_str):
    try:
        # Prepare a local environment to execute the code
        local_vars = {}
        exec(code_str, {}, local_vars)

        # Extract the model from the executed code (assumes 'model' variable is used)
        model = local_vars.get('model', None)
        
        if model:
            return model
        else:
            return "Model not defined correctly. Please ensure the 'model' variable is defined in your code."
