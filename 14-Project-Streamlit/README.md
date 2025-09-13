# Streamlit Installation and Usage Guide

This guide explains how to install Streamlit on both Linux and Windows machines and how to run a Streamlit program.

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
    python3 -m venv venv
    source venv/bin/activate
    ```
    > Replace `venv` with any name you prefer for your virtual environment.

3. **Install Streamlit using pip:**
    ```bash
    pip install streamlit
    ```

---

### b. Installing Streamlit on **Windows**

1. **(Optional) Create and activate a virtual environment:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```
    > Replace `venv` with any name you prefer.

2. **Install Streamlit using pip:**
    ```powershell
    pip install streamlit
    ```

---

## 4. Running a Streamlit Program

### Instructions to Run `streamlit_1.py` and `streamlit_2.py`

### Running `streamlit_1.py`

1. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install required package:**
   ```sh
   pip3 install plotly
   ```

3. **Run the script (example):**
   ```sh
   python streamlit_1.py
   ```

4. **Deactivate the virtual environment:**
   ```sh
   deactivate
   ```

5. **(Optional) Remove the virtual environment files:**
   ```sh
   rm -rf venv
   ```

---

### Running `streamlit_2.py`

1. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install required packages:**
   ```sh
   pip3 install streamlit
   pip3 install plotly
   pip3 install statsmodels
   ```

3. **Run the script (example):**
   ```sh
   python streamlit_2.py
   ```

4. **Deactivate the virtual environment:**
   ```sh
   deactivate
   ```

5. **(Optional) Remove the virtual environment files:**
   ```sh
   rm -rf venv
   ```

---

**Note:**  
- Ensure you are in the correct directory before running these commands.
- Removing the `venv` folder will delete the virtual environment and all installed packages.

---

## 6. Troubleshooting

- If you encounter issues, ensure Python and pip are correctly installed.
- For permission errors, try using `pip install --user streamlit`.
- If you installed in a virtual environment, ensure it's activated before running commands.

---

Happy Streamlit-ing!
