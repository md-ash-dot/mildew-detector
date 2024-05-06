import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect powdery mildew contained leaves have clear marks/signs, "
        f"typically the leaf is not so fresh and has discoloration and shows signs of a dying leaf. "
        f"Small white spots on both the surface and the underside of leaves can be noticed, "
        f"that can differentiate them from an healthy leaf. \n\n"
        f"* An Image Montage shows that typically a powdery mildew leaf has white spots across it. "
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."

    )

    