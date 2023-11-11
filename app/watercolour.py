import cv2
import numpy as np
import streamlit as st
from PIL import Image

def watercolour(img):
    watercolour_image = cv2.stylization(img, sigma_s=100, sigma_r=0.45)
    #img_bright = cv2.convertScaleAbs(img, alpha=-126)
    return watercolour_image

def sketch(img):
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    b1=cv2.GaussianBlur(gray,(45,45),0)
    f= cv2.divide(gray, b1, scale=256)
    return f
    

st.title("Water Colour")
img_file=st.file_uploader("Upload your image",type=['jpg','png','jpeg'])

if img_file:
    org_img=Image.open(img_file)
    org_img=np.array(org_img)
    wt=watercolour(org_img)
    sk=sketch(org_img)
    st.image([org_img,sk])

