
import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.utils import plot_model
import os
import tempfile
from PIL import Image

# Title of the Web App
st.title("Neural Network Architecture Visualizer")

# Input box for model code
st.subheader("Step 1: Input Model Code")
model_code = st.text_area(
    "Enter Keras/TensorFlow model code here",
    '''
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])
'''
)

# Button to generate the model architecture visualization
if st.button('Generate Architecture'):
    try:
        # Define a safe environment for running the code
        exec(model_code)
        
        # Generate the model architecture image
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
            plot_model(model, to_file=tmpfile.name, show_shapes=True, show_layer_names=True)
            
            # Open the image file for display
            img = Image.open(tmpfile.name)
            st.image(img, caption='Neural Network Architecture', use_column_width=True)
            
            # Provide download link
            tmpfile.close()
            st.download_button(
                label="Download Model Architecture",
                data=open(tmpfile.name, "rb").read(),
                file_name="model_architecture.png",
                mime="image/png"
            )
    except Exception as e:
        st.error(f"Error: {str(e)}")
