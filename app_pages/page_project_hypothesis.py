import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    # st.success(
    #     f"* We suspect powdery mildew contained leaves have clear marks/signs, "
    #     f"typically the leaf is not so fresh and has discoloration and shows signs of a dying leaf. "
    #     f"Small white spots on both the surface and the underside of leaves can be noticed, "
    #     f"that can differentiate them from an healthy leaf. \n\n"
    #     f"* An Image Montage shows that typically a powdery mildew leaf has white spots across it. "
    #     f"Average Image, Variability Image and Difference between Averages studies did not reveal "
    #     f"any clear pattern to differentiate one from another."

    # )

    st.success(
        f"* Disntinct feautures in Variability of cherry leaves containing Powdery Mildew " 
    )
    st.write(
        f"We have found through the average variability of images of powdery mildew containing cherry leaves, "
        f"typically the leaves are not so fresh with discolouration. The white spots and marks caused by Powdery Mildew, "
        f"found on the samples of the leaves are present across the entire surface with no specific region containing "
        f"more or less. These can be observed as distinct features through variability "
    )

    st.success(
        f"* Absence of any distinctive features in Variability of Healthy cherry leaves " 
    )
    st.write(
        f"We have found through the average variability of images of healthy cherry leaves, typically the leaves are fresh "
        f"and the surface is predominantly green, with no spots and marks, like observed in cherry leaves with powdery mildew "
        f"Since all regions of the leaf show no clear signs, we are unable to find any distinctive features through variability "
    )

    st.success(
        f"* Patterns from difference between the averages of Healthy and Powdery Mildew containg cherry leaves" 
    )
    st.write(
        f"We have found through the study of difference between the averages of Healthy and Powdery Mildew containg cherry leaves, "
        f"No clear patterns were found since the white spots and marks in cherry leaves with powdery mildew were found throughout "
        f"the entire surface with no specic regions of the leaf. We are unable to find any distinctive patterns through this study. "
    )
