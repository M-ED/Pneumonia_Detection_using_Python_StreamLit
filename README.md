
# Pneumonia Classification using Python and Streamlit

This project is a web application for classifying pneumonia using chest X-ray images. The app is built with Python, Streamlit, and a pre-trained deep learning model using Keras.






## Features

- **User-friendly Interface:** Upload chest X-ray images and get instant predictions.
- **Real-time Classification:** The app processes the image and predicts whether the X-ray indicates pneumonia or not.
- **Custom Background:** The app features a customizable background image for an enhanced user experience.

## Prerequisites
- Python 3.9.0 or higher 
- TensorFlow/Keras
- Streamlit
- Pillow
- NumPy

## Installation

1. Clone the repository:

```bash
  git clone https://github.com/M-ED/Pneumonia_Detection_using_Python_StreamLit.git
```

2. Create virtual environment using following commands:
```bash
  conda create -n pneumonia_project python==3.9.0
  conda activate pneumonia_project
```

3. Install the necessary libraries in requirements file
```bash
   pip install -r requirements.txt
```

4. Run the script
```bash
  streamlit run app.py
```
5. Upload a Chest X-ray Image:
- Upload an image in JPEG, JPG, or PNG format.
- The model will classify the image and display the result.


## Model Information
The model used in this project is a convolutional neural network (CNN) trained on a dataset of chest X-ray images. 

## File Structure
- **app.py:** The main file that runs the Streamlit application.
- **utils.py:** Contains helper functions for classification and background setting.
- **model/pneumonia_classifier.h5:** The pre-trained Keras model for pneumonia classification.
- **model/labels.txt:** Contains the labels used by the model for classification.
- **images_2.jpeg:** The background image used in the Streamlit app.

## Example Output
When an image is uploaded, the app will display the X-ray along with the prediction result (e.g., "Pneumonia" or "Normal") and the confidence score.



## Acknowledgements

- OpenCV: [https://opencv.org/](https://opencv.org/)




## License

[MIT](https://choosealicense.com/licenses/mit/)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Author

- [@mohtadia_naqvi](https://github.com/M-ED)

