# Streamlit Installation and Usage Guide

This guide explains how to install Streamlit on both Linux and Windows machines and how to run a basic Streamlit program.

---

## 1. What is Streamlit?

[Streamlit](https://streamlit.io/) is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.

---

## 2. Prerequisites

- Python 3.7 or above
- pip (Python package manager)

> **Tip:** It is recommended to use a virtual environment to avoid dependency conflicts.

---

## 3. Installation

### a. Installing Streamlit on **Linux**

1. **Update your system packages (optional):**
    ```bash
    sudo apt update
    ```

2. **(Optional) Create and activate a virtual environment:**
    ```bash
    python3 -m venv 14-Project-Streamlit-env
    source 14-Project-Streamlit-env/bin/activate
    ```

3. **Install Streamlit using pip:**
    ```bash
    pip install 14-Project-Streamlit
    ```

---

### b. Installing Streamlit on **Windows**

1. **(Optional) Create and activate a virtual environment:**
    ```powershell
    python -m venv streamlit-env
    .\streamlit-env\Scripts\activate
    ```

2. **Install Streamlit using pip:**
    ```powershell
    pip install streamlit
    ```

---

## 4. Running a Streamlit Program

1. **Create a Streamlit Python script**

    Example: `app.py`
    ```python
    import streamlit as st

    st.title('Hello, Streamlit!')
    st.write('Welcome to your first Streamlit app!')
    ```

2. **Run the Streamlit app**

    On both Linux and Windows, use the following command in your terminal:
    ```bash
    14-Project-Streamlit run app.py
    ```

3. **Access the app**

    After running the command, Streamlit will provide a local URL (usually `http://localhost:8501`) that you can open in your browser.

---

## 5. Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Community Forum](https://discuss.streamlit.io/)

---

## 6. Troubleshooting

- If you encounter issues, ensure Python and pip are correctly installed.
- For permission errors, try using `pip install --user streamlit`.
- If you installed in a virtual environment, ensure it's activated before running commands.

---

Happy Streamlit-ing!
