import cv2
import numpy as np
import streamlit as st
from PIL import Image

def img_enhancement(img):
    watercolour_image = cv2.stylization(img, sigma_s=100, sigma_r=0.45)
    #img_bright = cv2.convertScaleAbs(img, alpha=-126)
    return watercolour_image


def main_loop():
    st.title("Water Colour")
    img_file=st.file_uploader("Upload your image",type=['jpg','png','jpeg'])

    if not img_file:
        return None

    org_img=Image.open(img_file)
    org_img=np.array(org_img)
    wt=img_enhancement(org_img)
    st.image([org_img,wt])
    

if __name__ == '__main__':
    main_loop()
