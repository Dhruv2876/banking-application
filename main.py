import uuid
from datetime import datetime
import streamlit as st

from src.account_create import user

users_data=[]
validations=[]
st.write("User Details")

name=st.text_input(label="", placeholder="Provide your complete name")
phone=st.text_input(label="", placeholder="Provide your 10 digit mobile No.")
email=st.text_input(label="", placeholder="Provide your email with @ keyword")
aadhar=st.text_input(label="", placeholder="Provide your 12 digit aadhar no.")
address=st.text_input(label="", placeholder="Provide your permanent addresss")

obj_user=user(name,phone,email,aadhar,address)

if name:
    if name.isalpha():
        validations.append(True)
if phone:
     if phone.isdigit():
        if len(phone) == 10:
            validations.append(True)
if email:
 if "@" in email:
    validations.append(True)

if aadhar:
    if aadhar.isdigit():
        if len(aadhar) ==12:
            validations.append(True)
   
account_btn = st.button("SUBMIT")

if account_btn and validations.count(True)==4:
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
    st.success("User Created")
    # save to data\users.txt file
elif validations.count(True)!=0:
    st.error("Error in adding user")