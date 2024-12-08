# Pixel8ed---CV-Project

# 🌪️ Natural Disaster Detection Using CNN and Streamlit 🌊

This project uses Convolutional Neural Networks (CNN) to detect images resembling natural disasters. The model is integrated into a user-friendly **Streamlit** app where users can upload images and see color channel graphs, with the option to classify the image as either a **natural disaster** or **non-disaster**.

---

## 🔧 Features

- **📷 Image Upload**: Upload an image of any type to be analyzed.
- **🌈 Color Channel Visualization**: View the Red, Green, and Blue channel graphs of the uploaded image.
- **⚡ Detect**: Click the "Detect" button to analyze the image using the trained CNN model.
- **💡 Natural Disaster Classification**: The model classifies the image into **Natural Disaster** or **Non-Disaster**.

---

## 🚀 Installation

### Prerequisites

- Python 3.x
- `streamlit` for the web app interface
- `tensorflow` for the CNN model

### Steps to Run Locally

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/natural-disaster-detection.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd natural-disaster-detection
    ```

3. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - For Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - For macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

The app should now be running at `http://localhost:8501/` or at `http://192.168.0.106:8501`.

---

## 🧑‍💻 Technologies Used

- **Python** 🐍
- **TensorFlow** for CNN Model 🧠
- **Streamlit** for Web App 📊
- **Matplotlib** for Data Visualization 📈
- **NumPy** for Numerical Operations 🧮

---

## 📂 Project Structure

```plaintext
natural-disaster-detection/
│
├── app.py              # Streamlit app
├── model.h5            # Trained CNN model
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── image_processing.py            # Helper functions for image processing
└── 505.jpg
└── 0006.png
```

## 📱 Demo 
https://github.com/user-attachments/assets/b500a164-df8e-4077-92c8-0da2bc7d4dbf
