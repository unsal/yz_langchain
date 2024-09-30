
# pip3 install streamlit 

import yz_prompt_template as pt
import streamlit as st  # use on Terminal as: streamlit run yz_streamlit.py


header_container = st.container()
column_container = st.container()
sidebar_container = st.container()


# Container is just for organizing code. It is optional
# Header Section
with header_container:
    # Use Markdown for Writing Web Text
    st.title("Pet's Name Generator :wave:")

# Body Section
with column_container:
    st.write("---")
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.header("Col 1")

    with col2:
        st.header("Col 2")

    with col3:
        st.header("Col 3")


# Navigation Section
with sidebar_container:
    animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Hamster"))
    pet_color = st.sidebar.text_area(f"What color is your {animal_type}", max_chars=15)

    if pet_color:
        response = pt.generate_pet_name(animal_type, pet_color)

        col2.text(
            response["pet_name"]
        )  # pet_name is the output_key value getting from pt
