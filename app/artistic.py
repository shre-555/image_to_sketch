import cv2
import numpy as np

def watercolour(img):
    watercolour_image = cv2.stylization(img, sigma_s=100, sigma_r=0.45)
    #img_bright = cv2.convertScaleAbs(img, alpha=-126)
    return watercolour_image

def sketch(img):
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    b1=cv2.GaussianBlur(gray,(45,45),0)
    f= cv2.divide(gray, b1, scale=256)
    return f

def pencil(inp_img):
    img_pencil_sketch, pencil_color_sketch = cv2.pencilSketch( 
        inp_img, sigma_s=50, sigma_r=0.07, shade_factor=0.0825) 
    return img_pencil_sketch,pencil_color_sketch
