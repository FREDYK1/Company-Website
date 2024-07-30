import streamlit as sl

sl.set_page_config(page_title="Contact Us", page_icon="pics/Contact_Us.png", layout="wide")
sl.header("Contact Us")

with sl.form(key="contact_info"):
    user_email = sl.text_input("Email")
    subject = sl.text_input("Subject")
    row_message = sl.text_area("Message")
    button = sl.form_submit_button("Submit")
    if button:
        sl.success("Message sent successfully!")
