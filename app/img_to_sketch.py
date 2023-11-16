import cv2
import numpy as np
import streamlit as st
from PIL import Image
import artistic as art    

st.title("Artistic Effects")
img_file=st.file_uploader("Upload your image",type=['jpg','png','jpeg'])

if img_file:
    #org_img=Image.open(img_file)
    #org_img=np.array(org_img)
    org = cv2.imdecode(np.fromstring(img_file.read(), np.uint8), 1)
    org_img=cv2.cvtColor(org, cv2.COLOR_BGR2RGB) 
    wt=art.watercolour(org_img)
    sk=art.sketch(org_img)
    psk=art.pencil(org_img)
    st.image([org_img,sk,wt])
    st.image(list(psk))

