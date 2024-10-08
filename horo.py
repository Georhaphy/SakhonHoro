# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:38:33 2024

@author: user
"""

import streamlit as st
import pandas as pd
from analyzer import *


st.header("กรุณากรอกข้อมูล")
col1, col2, col3, col4, col5, col6 = st.columns(6)


with col1:
   sex = st.selectbox("เพศ", ('ชาย','หญิง'))

    
with col2:
    t = st.time_input('เวลาเกิด' ,step= 60)
    

with col3:
    date = st.selectbox("วันที่เกิด",
    ("1", "2", "3", "4", "5", "6", "7", "8", "9","10", "11", "12","13", "14", "15",
     "16", "17", "18", "19", "20", "21", "22", "23", "24","25", "26", "27","28", "29", "30", "31"))

    

with col4:
    month =  st.selectbox( "เดือนที่เกิด",
    ("มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
     "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"))

with col5:
    year =  st.text_input( "พ.ศ.ที่เกิด")    
    
    
with col6:
    st.write
    predict = st.button("ทำนาย")
    
