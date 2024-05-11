import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Our client, Farmy & Foods is a company in the agricultural sector that produces and harvests "
        f"different types of food.\n"
        f"* Their cherry plantations have been presenting powdery mildew, "
        f"which is a fungal disease that affects a wide range of plants.\n"
        f"* Currently, the process is to manually verify if a given cherry tree contains powdery mildew. "
        f"An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying "
        f"visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee "
        f"applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. "
        f"The company has thousands of cherry trees located in multiple farms across the country. "
        f"As a result, this manual process is not scalable due to time spent in the manual process inspection.\n"
        f"* To save time in this process, the IT team suggested an ML system that is capable of detecting "
        f"instantly, using a tree leaf image, if it is healthy or has powdery mildew. A similar manual process "
        f"is in place for other crops for detecting pests, and if this initiative is successful, there is a  "
        f"realistic chance to replicate this project to all other crops.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops."
        f"The available dataset contains 4208 images of healthy and powdery mildew containing leaves.\n"
        )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/md-ash-dot/mildew-detector/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate "
        f"a cherry leaf that is healthy from one that contains powdery mildew. \n"
        f"* 2 - The client is interested in predicting if a cherry tree is healthy or contains powdery mildew. "
        )
