import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello, Streamlit : ")
st.write(":streamlit: This is your first streamlit app")
st.text(" Lets get started ")


name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.success(f"Hello, {name}!")

# Displaying data and charts
df = pd.DataFrame(np.random.randn(10,2), columns=['A' , 'B'])
st.line_chart(df)
st.line_chart(df)

#Media layout and advance widget
st.sidebar.title("Navigation")
st.image("image.webp")

upload_file = st.file_uploader("upload a csv ", type='csv')
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.title(" Text and Marksdown Demo")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**,*Italic*, 'Code' , [Link](https://streamlit.io)")
st.code("for i in range(5): print(i)", language="python")
st.text_input("What's your name?")
st.text_area("write something..")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple","Banana","Mango"])
st.multiselect("choose toppings",["Cheese","Tomato"])
st.radio("pick one", ["Option A","Option B"])
st.checkbox("I agree to the terms")

if st.checkbox("Show Details"):
   st.info("Here are more details...")

option = st.radio("Choose view", ["Show Chart","Show Table"])
if option == "Show Chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")

    
#login form
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password",type="password")
    submitted = st.form_submit_button("login")

    if submitted:
        st.success(f"Welcome, {username}!")