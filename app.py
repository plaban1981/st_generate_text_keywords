import streamlit as st
from PIL import Image
import requests
import pandas as pd
import os
import json
#
image_path = "image.png"
image = Image.open(image_path)

st.set_page_config(page_title="Generate Text From Keywords App", layout="centered")
st.image(image, caption='Generate Text From Keywords')
#
# page header
st.title(f"Generate Text From Keywords App")
with st.form("Generate Text From Keywords"):
   text1 = st.text_input("Enter text here")
   submit = st.form_submit_button("Generate")
   #
   if submit:    
        print(text1)
        #
        with open("input.txt", "wb") as f:
            f.write(text1.encode("utf-8"))
        os.chmod("input.txt", 0o777)
        # Keyword Extraction API
        url = "https://app.aimarketplace.co/api/marketplace/models/generate-text-from-keywords-53a9cfb7/predict/"
        payload={'data': open('input.txt','rb')}
        headers = {'Authorization': 'Api-Key jxdddWRd.vH45HRECUx1m8oOMfIluhsMg7FSA6rPu','Cache-Control': 'no-cache'}

        response = requests.request("POST", url, headers=headers, files=payload)
        #
        print(response.text)
        # output header
        st.header("Generated Text")
        # output results
        st.success(response.text.split("response")[1].split(" keywords")[1].replace("}","").replace("]","").replace('"','').replace('\\',''))