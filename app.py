import streamlit as st 
from OOP import Coffee

st.title("Coffee Bean Volume and Density Calculator")

length = st.number_input("Length")
width = st.number_input("width")
thick = st.number_input("thick")
mass = st.number_input("mass")

if st.button("calculate"):
    coffee = Coffee(length, width, thick, mass)

    volume = coffee.calculate_volume()
    density = coffee.calculate_density()

    st.write("Volume  : ", volume)
    st.write("Density : ", density)