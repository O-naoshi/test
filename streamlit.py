# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:08:55 2021

@author: naoshi
"""
import streamlit as st

text = st.text_input('あなたの名前を教えてください')
'あなたの名前は、 ', text, 'です' 

condition = st.slider('あなたの今の調子は？',0, 100, 50)
'コンディション:',condition

from PIL import Image

