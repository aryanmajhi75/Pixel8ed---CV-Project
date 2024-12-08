import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

category = "Wildfire"

# Set the dark theme
st.set_page_config(page_title="Natural Disaster Analysis", layout="wide")
st.markdown("""
<style>
    body {
        background-color: #0e1117;
        color: white;
        font-family: Arial, sans-serif;
    }
    .card {
            background-color: #2c2f3f;
            border-radius: 30px;
            padding: 20px;
            margin: 20px;
        }
    .stButton button {
            background-color: #636efa;
            color: white;
            border-radius: 30px;
            padding: 10px 20px;
            font-size: 16px;
        }
    .stFileUploader input[type="file"] {
            background-color: #636efa;
            color: white;
        }
</style>
""", unsafe_allow_html=True)

st.title("Natural Disaster Analysis - Team Pixel8ed")
st.markdown('<hr>', unsafe_allow_html=True)

uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg"], label_visibility="hidden")
detect_button = st.button("Detect")

col1, col2 = st.columns(2)

with col1:
  if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_container_width=True)

  if detect_button:
    st.markdown(f"<h1 style='text-align: center; color: white; font-size: 40px;'>{category}</h1>", unsafe_allow_html=True)

with col2:
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        image_data = np.array(image)
        red = image_data[:, :, 0].flatten()
        green = image_data[:, :, 1].flatten()
        blue = image_data[:, :, 2].flatten()

        color_option = st.radio("Select color to display:", ("All", "Red", "Green", "Blue"))

        if color_option == "All":
            data = {
                "Red": np.mean(red),
                "Green": np.mean(green),
                "Blue": np.mean(blue)
            }
            df = pd.DataFrame(data.items(), columns=["Color", "Average Intensity"])
            # Create a bar chart with respective colors for each channel
            fig, ax = plt.subplots()
            ax.bar(df["Color"], df["Average Intensity"], color=['red', 'green', 'blue'])
            ax.set_ylabel("Average Intensity")
            st.pyplot(fig)

        elif color_option == "Red":
            st.subheader("Red Channel Intensity")
            fig, ax = plt.subplots()
            ax.bar([0], np.mean(red), color='red')
            ax.set_xticks([0])
            ax.set_xticklabels(["Red"])
            ax.set_ylabel("Average Intensity")
            st.pyplot(fig)

        elif color_option == "Green":
            st.subheader("Green Channel Intensity")
            fig, ax = plt.subplots()
            ax.bar([0], np.mean(green), color='green')
            ax.set_xticks([0])
            ax.set_xticklabels(["Green"])
            ax.set_ylabel("Average Intensity")
            st.pyplot(fig)

        elif color_option == "Blue":
            st.subheader("Blue Channel Intensity")
            fig, ax = plt.subplots()
            ax.bar([0], np.mean(blue), color='blue')
            ax.set_xticks([0])
            ax.set_xticklabels(["Blue"])
            ax.set_ylabel("Average Intensity")
            st.pyplot(fig)

    else:
        st.write("No image uploaded")

st.markdown("## Authors :")

image1 = Image.open("2347104.jpg").rotate(90)
st.image(image1, width=150,caption="ANUPAM KUMAR 2347104")
# st.write("ANUPAM KUMAR 2347104")

image2 = Image.open("2347107.jpg").rotate(90)
st.image(image2, width=150,caption="ARYAN MAJHI 2347107")
# st.write("ARYAN MAJHI 2347107")