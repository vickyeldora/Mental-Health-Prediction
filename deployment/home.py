# import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title= 'MENTAL HEALTH',
    layout= 'wide',
    initial_sidebar_state='expanded'
)

def run():
    # create title
    st.title('Mental Health is important')

    st.image('https://domf5oio6qrcr.cloudfront.net/medialibrary/14528/conversions/3f85b1b1-9dc7-4a90-855c-dc204646e889-thumb.jpg'
             ,caption='MENTAL HEALTH')
    
    st.markdown('---')
    
    # add description
    container = st.container(border=True)
    container.write('Welcome to our website dedicated to raising awareness about mental health. This page is created to elevate our understanding of mental health')
    container.write('Mental health conditions are not uncommon. Hundreds of millions suffer from them yearly, and many more do over their lifetimes. It’s estimated that 1 in 3 women and 1 in 5 men will experience major depression in their lives. Other conditions, such as schizophrenia and bipolar disorder, are less common but still have a large impact on people’s lives.')
    container.write('Mental illnesses are treatable, and the impact they have can be reduced. Despite this, treatment is often lacking or poor quality, and many feel uncomfortable sharing their symptoms with healthcare professionals or people they know. This also makes it difficult to estimate the actual prevalence of mental illnesses.')
    container.write('To support them, it’s essential to have good data to understand these conditions – how, when, and why they occur, how many people are affected by them, and how they can be treated effectively and safely.')
    container.write('On this page, we show data on the prevalence of mental illnesses and their burden, and people’s attitudes toward mental health.')

if __name__ == '__main__':
    run()