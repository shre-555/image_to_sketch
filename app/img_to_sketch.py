import cv2
import numpy as np
import streamlit as st
from PIL import Image
import artistic as art
from random import randint
import feedback_analyzer

st.title("Artistic Effects")
img_file=st.file_uploader("Upload your image",type=['jpg','png','jpeg'])

options = ('Black and White - Expert',\
     'Black and White - Novice',\
     'Colour - Expert',\
     'Colour - Novice',
     'Cannot decide - Pick for me')

option = st.selectbox(
    'Select the type of sketch',
    options,
    index = None,
    placeholder="Select type")

if img_file and option:
    #org_img=Image.open(img_file)
    #org_img=np.array(org_img)
    org = cv2.imdecode(np.fromstring(img_file.read(), np.uint8), 1)
    org_img=cv2.cvtColor(org, cv2.COLOR_BGR2RGB)

    if option == options[4]:
        sketch_type = options[randint(0,len(options))-1]
    else:
        sketch_type = option

    if sketch_type == 'Black and White - Expert':
        sk=art.sketch(org_img)
    elif sketch_type == 'Black and White - Novice':
        psk=art.pencil(org_img)
        sk=psk[0]
    elif sketch_type == 'Colour - Expert':
        sk=art.watercolour(org_img)
    elif sketch_type == 'Colour - Novice':
        psk=art.pencil(org_img)
        sk=psk[1]

    "Original"
    st.image(org_img)
    sketch_type + ' Sketch'
    st.image(sk)

    feedback = st.text_input('Tell us how you found our app')
    if feedback:
        st.write(feedback_analyzer.get_reply(feedback))


