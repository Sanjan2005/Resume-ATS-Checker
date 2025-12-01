import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf

from dotenv import load_dotenv

load_dotenv()  ## load env variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


##gemini pro response

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content(input)
    return response.text

# def input_pdf_text(uploaded_file):
#     reader = pdf.PdfReader(uploaded_file)
#     text = ""
#     for page in reader(len(reader.pages)):
#         page = reader.pages[page]
#         text+=str(page.extract_text())
#     return text

def input_pdf_text(uploaded_file):
    from PyPDF2 import PdfReader
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


## prompt templete

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer,Machine Leaning engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes and mention action verbs needed. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""


## steamlit app

st.title("AI powered ATS")
st.text("Improve your Resume ATS")
jb = st.text_area("Paste the job Description")
uploaded_file = st.file_uploader("Upload your resume",type="pdf",help="please upload the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt)
        st.subheader(response)
