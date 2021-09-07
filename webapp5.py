# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 17:13:45 2021

@author: gauri
"""

import streamlit as st

st.title('QR INSTRUCTOR APP')
Firstname = st.text_input("First name")
Lastname = st.text_input("Last name")
s = st.text_input('password',type="password")
s = st.text_input(' Re password',type="password")
Email = st.text_input("email")
Mobileno = st.text_input("Mobile number")
city = st.text_input("city")
submit_button = st.button(label='sign up')
if submit_button:
    st.write('signup successfull')