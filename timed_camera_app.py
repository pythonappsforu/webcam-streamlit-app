import streamlit as st
import cv2
from datetime import datetime


st.title("Motion Detector")
start = st.button("Start Camera")

if start:
    camera = cv2.VideoCapture(0)
    streamlit_image = st.image([])
    while True:
        check,frame = camera.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        cv2.putText(img=frame,text=datetime.now().strftime('%d-%b-%Y'),org=(20,30),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=.5,color=(250,225,225),thickness=2,lineType=cv2.LINE_AA)
        cv2.putText(img=frame,text=datetime.now().strftime('%H:%M:%S '),org=(20, 50), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=.5, color=(250, 0, 0), thickness=2,lineType=cv2.LINE_AA)
        streamlit_image.image(frame)