import streamlit as st
from cv_code import get_colored_image

st.title("Color Picker")

st.sidebar.header("Adjust RGB Values and Switch")
switch = st.sidebar.selectbox("Switch", [0, 1], format_func=lambda x: "ON" if x == 1 else "OFF")
r = st.sidebar.slider("Red", 0, 255, 0)
g = st.sidebar.slider("Green", 0, 255, 0)
b = st.sidebar.slider("Blue", 0, 255, 0)

img = get_colored_image(r, g, b, switch)

st.image(img, caption=f"Color: RGB({r}, {g}, {b})" if switch else "Color: OFF", use_column_width=True)
