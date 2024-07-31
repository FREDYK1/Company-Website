import pandas
import streamlit as sl
from email_implementation import email_send

sl.set_page_config(page_title="Contact Us", page_icon="pics/Contact_Us.png", layout="wide")
sl.header("Contact Us")

df = pandas.read_csv("Subjects.csv")

with sl.form(key="contact_info"):
    user_email = sl.text_input("Email")
    subject = sl.selectbox("Subject", df["Subject"])
    raw_message = sl.text_area("Message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {subject}
{raw_message}
"""
    button = sl.form_submit_button("Submit")
    if button:
        email_send(message)
        sl.success("Message sent successfully!")
