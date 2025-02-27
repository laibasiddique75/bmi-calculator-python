import streamlit as st

st.set_page_config(page_title="BMI CALCULATOR", page_icon="😊", layout="centered")

st.title("Bmi Calculator In Python")
st.markdown("## Apna body mass index (BMI) calculator kry. Neechy apna **weight and height** enter kry.")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg):", min_value=1.0, format="%.2f")

with col2:
    height = st.number_input("Height (m):", min_value=0.5, format="%.2f")  # More realistic min height

if height > 0 and weight > 0:
    bmi = weight / (height ** 2)  # BMI formula
    st.subheader("Apka BMI h:")
    st.markdown(f"**{bmi:.2f}**", unsafe_allow_html=True)

    if bmi < 18.5:
        st.error("You are underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("You are normal weight")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight")
    else:
        st.error("Obesity 🚨")
else:
    st.info("Please enter a valid weight and height")
