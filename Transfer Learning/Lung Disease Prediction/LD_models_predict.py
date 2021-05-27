# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 08:41:24 2021

@author: Jennifer Rajkumar
"""

import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import sklearn
import os
import numpy as np
from tensorflow import keras
import streamlit as st
from PIL import Image



st.title('**Lung Disease Classification App**')

st.write("""          
         * This app ***Predicts*** the Lung Disease based on the given ***Image*** file. 
         * The Lung Diseases may belong to one of the following classes: 'BacterialPneumonia', 'COVID-19', 'Normal', 'ViralPneumonia'.
         * The app uses ***Keras Applications*** pre-trained models **VGG16, InceptionV3 and ResNet50** for Feature Extraction and integrated into additional classification layers for Prediction.
         * The front end was developed using the ***streamlit*** application
         * ***Google Colab*** was used for training the models.
         
         * DataSource: 'https://www.kaggle.com/darshan1504/covid19-detection-xray-dataset'
         """)
         
def load_image(image_file):
	img = Image.open(image_file)    
	return img

def model_pred(file_path,model_name,sel_model,img_ht,img_width):
    class_names = ['BacterialPneumonia', 'COVID-19', 'Normal', 'ViralPneumonia']
    
    test_img = keras.preprocessing.image.load_img(file_path, target_size=(img_ht,img_width))

    img_array = keras.preprocessing.image.img_to_array(test_img)
    
    if model_name == 'VGG16':
        img_array = tf.keras.applications.vgg16.preprocess_input(img_array) 
    elif model_name == 'InceptionV3':
        img_array = tf.keras.applications.inception_v3.preprocess_input(img_array)
    else:
        img_array = tf.keras.applications.resnet50.preprocess_input(img_array)
        
    img_array = tf.expand_dims(img_array, 0)

    prediction = sel_model.predict(img_array)
    score = tf.nn.softmax(prediction[0])    

    st.write("{} Prediction:".format(model_name))
    
    st.write("This image most likely belongs to {} class."
              .format(class_names[np.argmax(score)]))    

def upload_predict_file(img_file):    
    
    with open(img_file.name, "wb") as f:
        f.write(img_file.getbuffer()) 
        
    
    model_select = st.selectbox("please choose the Model for prediction..",options=['<select>','VGG16' ,'InceptionV3', 'ResNet50'])
    
    with st.spinner(text='Please wait for the model to load..'):        
                    
        if model_select == 'VGG16':
            model_name = 'VGG16'
            sel_model = tf.keras.models.load_model("C:/Users/Bruno_Raj/Desktop/LD_classify/best_VGG16_model.h5")
            img_ht = 224
            img_width = 224
        elif model_select == 'InceptionV3':
             model_name = 'InceptionV3'
             sel_model = tf.keras.models.load_model("C:/Users/Bruno_Raj/Desktop/LD_classify/best_InceptionV3_model.h5")
             img_ht = 299
             img_width = 299           
        else:
            model_name = 'ResNet50'
            sel_model = tf.keras.models.load_model("C:/Users/Bruno_Raj/Desktop/LD_classify/best_ResNet50_model.h5")
            img_ht = 224
            img_width = 224             
                
              
    model_pred(img_file.name,model_name,sel_model,img_ht,img_width)    
    
    
    
image_file = st.file_uploader("Please Upload an Image..",type=['png','jpeg','jpg'])

if image_file is not None:    
    img = load_image(image_file)    
    st.image(img)
    upload_predict_file(image_file)