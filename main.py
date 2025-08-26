import uuid
from datetime import datetime
import streamlit as st

users_data=[]

st.write("User Details")
name=st.text_input(label="", placeholder="Provide your complete name")
phone=st.text_input(label="", placeholder="Provide your 10 digit mobile No.")
email=st.text_input(label="", placeholder="Provide your email with @ keyword")
aadhar=st.text_input(label="", placeholder="Provide your 12 digit aadhar no.")
address=st.text_input(label="", placeholder="Provide your permanent addresss")

account_btn = st.button("SUBMIT")
if account_btn:
    data = {
        "id": uuid.uuid1(),
        "name": name,
        "phone": phone,
        "email": email,
        "aadhar": aadhar,
        "address": address,
        "created": datetime.now(),
        "status": 1
    }
    users_data.append(data)
    st.write(f"User Created: {data}")
    # save to data\users.txt file
# else:
#     st.write("Error in adding user")