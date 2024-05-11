import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* Healthy cherry leaves look fresh and green across the entire surface of leaf " 
    )
    st.info(
        f"This hypothesis proved to be right.\n"
        f"* Created image monatge of healthy and powdery mildew containing cherry leaves.\n"
        f"* Plotted a histogram of color values of average healthy and powdery mildew containing cherry leaves. "
    )
    st.write(
        f"We have found through the image monatge of images of the cherry leaves and histogram of "
        f"color values of average healthy and powdery mildew containing cherry leaves, the green channel had a wider"
        f"range in healthy cherry leaves and predominantly green across the entire surface of the leaf "
        f"compared to cherry leaves with powdery mildew in it. While the leaves with Powdery Mildew have discloration "
        f"on various spots or throughout the entire leaf.  "
    )

    st.success(
        f"* Disntinct feautures in Variability of cherry leaves containing Powdery Mildew " 
    )
    st.info(
        f"This hypothesis proved to be right.\n"
        f"* Displayed plot of mean and standard deviation of cherry leaves containing Powdery Mildew. "
    )
    st.write(
        f"We have found through the average variability of images of powdery mildew containing cherry leaves, "
        f"typically the leaves are not so fresh with discolouration. The white spots and marks caused by Powdery Mildew, "
        f"found on the samples of the leaves are present across the entire surface with no specific region containing "
        f"more or less. The edges of the leaves are darker and are more pronounced. These can be observed as distinct "
        f"features through variability of the cherry leaves containing Powdery Mildew. "
    )

    st.success(
        f"* Absence of white spots and discolouration in Variability of Healthy cherry leaves " 
    )
    st.info(
        f"This hypothesis proved to be right.\n"
        f"* Displayed plot of mean and standard deviation of healthy cherry leaves."
    )
    st.write(
        f"We have found through the average variability of images of healthy cherry leaves, typically the leaves are fresh "
        f"and the surface is predominantly green, with no spots and marks, like observed in cherry leaves with powdery mildew. "
        f"The edges are not so dark and pronounced like in leaves with powdery mildew and are smooth comparatively. These can "
        f"be observed in all regions of the leaf as clear signs and distinctive features through variability. "
    )

    st.success(
        f"* Patterns from difference between the averages of Healthy and Powdery Mildew containg cherry leaves helps to differentiate them." 
    )
    st.info(
        f"This hypothesis proved to be right.\n"
        f"* Displayed plot of difference between mean healthy and mean powdery mildew cherry leaves."
    )
    st.write(
        f"We have found through the study of difference between the averages of Healthy and Powdery Mildew containg cherry leaves, "
        f"The patterns such as white spots, marks, dark pronounced edges in cherry leaves with powdery mildew, and the patterns "
        f"found in the healthy leaves being predominantly green and having smooth edges and not pronounced. We are able to find "
        f"distinctive patterns through this study. "
    )

    st.warning(
        f"Business requirement 1 of client has been met. Our study has analysed:\n"
        f"* Average images and variability images for each class (healthy or powdery mildew).\n"  
        f"* The differences between average healthy and average powdery mildew cherry leaves.\n"
        f"* An image montage for each class."
    )

    st.success(
        f"* A Machine learning model can be created with the dataset provided to predict if a leaf contains powdery Mildew." 
    )
    st.info(
        f"This hypothesis proved to be right.\n"
        f"* Created and trained a tensor flow CNN convolution neural network model.\n"
        f"* Evaluated model performance for an accuracy of 99.76%.\n"
        f"* Predicted successfully using the trained model on new data."
    )
    st.write(
        f"The disntinctive features of healthy and powdery mildew containing leaves which could be manually tested currently "
        f"could be used to train a ML model. A CNN convolution neural network model was able to be trained from the images "
        f"in the dataset and augmented images generated. And the model was able to successfully predict from uploaded images "
        f"of sample leaves and tell if it contained powdery mildew at successful accuracy of 99.76%. "
    )

    st.warning(
        f"Business requirement 2 of client has been met. An ML system that is capable of predicting whether a cherry leaf "
        f"is healthy or contains powdery mildew has been delivered using Neural Networks to map the relationships between the "  
        f"features and the labels. In our case a CNN Convolution neural network was used. "
    )
