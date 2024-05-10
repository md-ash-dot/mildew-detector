import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* Healthy cherry leaves look fresh and green across the entire surface of leaf " 
    )
    st.info(
        f"This hypothesis proved to be right. "
    )
    st.write(
        f"We have found through the image monatge of images of the cherry leaves, the leaves are very green across "
        f"the entire surface of the leaf compared to cherry leaves with powdery mildew in it. While the leaves with "
        f"Powdery Mildew have discloration on various spots or throughout the entire leaf.  "
    )

    st.success(
        f"* Disntinct feautures in Variability of cherry leaves containing Powdery Mildew " 
    )
    st.info(
        f"This hypothesis proved to be right. "
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
        f"This hypothesis proved to be right. "
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
        f"This hypothesis proved to be right. "
    )
    st.write(
        f"We have found through the study of difference between the averages of Healthy and Powdery Mildew containg cherry leaves, "
        f"The patterns such as white spots, marks, dark pronounced edges in cherry leaves with powdery mildew, and the patterns "
        f"found in the healthy leaves being predominantly green and having smooth edges and not pronounced. We are able to find "
        f"distinctive patterns through this study. "
    )

    st.success(
        f"* A Machine learning model can be created with the dataset provided to predict if a leaf contains powdery Mildew." 
    )
    st.info(
        f"This hypothesis proved to be right. "
    )
    st.write(
        f"The disntinctive features of healthy and powdery mildew containing leaves which could be manually tested currently "
        f"could be used to train a ML model. A CNN convolution neural network model was able to be trained from the images "
        f"in the dataset and augmented images generated. And the model was able to successfully predict from uploaded images "
        f"of sample leaves and tell if it contained powdery mildew at successful accuracy of 99.76%. "
    )
