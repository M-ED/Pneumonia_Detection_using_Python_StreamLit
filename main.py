import streamlit as st
from keras.models import load_model
from PIL import Image
from utils import classify, set_background

set_background(r'C:\Users\Fame\Desktop\Projects_2024\Computer_Vision_Intermediate_Projects\Pneumonia_Classification_using_Python_and_Streamlit\images_2.jpeg')

## set title
st.title('Pneumonia classification')

## set header
st.header('Please upload a chest x-ray image.')

## upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

## load classifier
model=load_model(r'C:\Users\Fame\Desktop\Projects_2024\Computer_Vision_Intermediate_Projects\Pneumonia_Classification_using_Python_and_Streamlit\model\pneumonia_classifier.h5')

## load class name
with open(r'C:\Users\Fame\Desktop\Projects_2024\Computer_Vision_Intermediate_Projects\Pneumonia_Classification_using_Python_and_Streamlit\model\labels.txt', 'r') as f:
    class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
    f.close()
print(class_names)

## display image
if file is not None:
    image=Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)
    
## classify image
class_name, conf_score = classify(image, model, class_names)    

## write classification
st.write("## {}".format(class_name))
st.write("## score: {}".format(conf_score))