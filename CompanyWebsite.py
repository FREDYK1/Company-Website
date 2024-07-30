import streamlit as sl
import pandas

sl.set_page_config(layout="wide")

sl.title("The Best Company")
content = """
Tech Innovate, founded in 2010, leads in technological advancements, offering innovative software solutions to enhance 
business operations globally. Our services span cloud computing, AI, and custom software development, underpinned by 
core values of innovation, integrity, and inclusivity. Recognized among the "Top 50 Most Innovative Companies," we're
committed to societal and environmental betterment through technology. As we look to the future, our goal is to expand
our offerings and market presence, driving forward with solutions that benefit our customers and the world.
Lets introduce you to the team members:
"""
sl.write(content)

sl.subheader("Our Team")

col1, col2, col3 = sl.columns([1, 1, 1])

df = pandas.read_csv("trials/csvs/data.csv")

with col1:
    for index, row in df[:4].iterrows():
        sl.header(F"{row['first name'].title()} {row['last name'].title()}")
        sl.write(row["role"])
        sl.image(F"trials/pics/{row['image']}")

with col2:
    for index, row in df[4:8].iterrows():
        sl.header(F"{row['first name'].title()} {row['last name'].title()}")
        sl.write(row["role"])
        sl.image(F"trials/pics/{row['image']}")

with col3:
    for index, row in df[8:].iterrows():
        sl.header(F"{row['first name'].title()} {row['last name'].title()}")
        sl.write(row["role"])
        sl.image(F"trials/pics/{row['image']}")
