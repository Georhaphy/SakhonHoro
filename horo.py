# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:38:33 2024

@author: user
"""

import streamlit as st
import pandas as pd
from analyzer import *


st.header("กรุณากรอกข้อมูล")
col1, col2, col3, col4, col5  = st.columns([2,2,1,2.5,2])


with col1:
   sex = st.selectbox("เพศ", ('ชาย','หญิง'))

    
with col2:
    t = st.time_input('เวลาเกิด' ,step= 60)
    

with col3:
    date = st.selectbox("วันที่เกิด",
    ("01", "02", "03", "04", "05", "06", "07", "08", "09","10", "11", "12","13", "14", "15",
     "16", "17", "18", "19", "20", "21", "22", "23", "24","25", "26", "27","28", "29", "30", "31"))

    

with col4:
    month =  st.selectbox( "เดือนที่เกิด",
    ("มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
     "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"))

with col5:
    year =  st.text_input( "พ.ศ.ที่เกิด")    
    
    
predict = st.button("ทำนาย")

if predict:
   st.write(calyearpillar(date,month,year))
