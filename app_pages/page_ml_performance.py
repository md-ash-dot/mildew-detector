import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    version = 'v1'

    st.write("## Ml Performance Metrics")

    st.write("### Average Image size in dataset")

    average_image_size = plt.imread(f"outputs/{version}/avg_img_size.png")
    st.image(average_image_size, caption='Average Image Size - Width average: 256 Height average: 256')
    st.info(
        f"The average image size in the dataset provided was found to have an average width of 256 "
        f"pixels and an average height of 256 pixels"
    )
    st.write("---")

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')

    st.write("### Sunburst nested pie plot - Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_sunburst_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.info(
        f"The label frequencies in the train, test and validation set were found to be\n"
        f"* train - healthy: 1472 images\n"
        f"* train - powdery_mildew: 1472 images\n"
        f"* validation - healthy: 210 images\n"
        f"* validation - powdery_mildew: 210 images\n"
        f"* test - healthy: 422 images\n"
        f"* test - powdery_mildew: 422 images\n"
    )
    st.write("---")


    st.write("### Model History")
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.info(
        f"The model learning curve was used to check the model for over-fitting "
        f"and under-fitting by plotting loss and accuracy."
    )
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))
    
    