import streamlit as st
import json
import os

# Set the page title and icon
st.set_page_config(page_title="TechCompass", page_icon="🧭")

# Title and introduction
st.title("TechCompass")
st.markdown("""
Welcome to TechCompass, your guide through the realms of data engineering, programming, automation techniques, and more. This project aims to provide foundational guides and resources to help individuals navigate the basics and intricacies of technology.

### Database Optimization Guide
Below is the JSON viewer for the Database Optimization Guide. You can view the guide directly or download the JSON file for your reference.
""")

# Link to download the database optimization JSON file
st.markdown("[Download Database Optimization Guide](data/DBOptimization.json")

# JSON viewer
json_file_path = r"data/DBOptimization.json"
if os.path.exists(json_file_path):
    with open(json_file_path, "r") as json_file:
        db_optimization_guide = json.load(json_file)
        st.json(db_optimization_guide)
else:
    st.error("The database optimization JSON file could not be found. Please make sure the file exists in the 'data' folder.")
