import eda, predict, home
import streamlit as st

navigation = st.sidebar.selectbox('Navigation',['Home Page','EDA','Form Prediction'])

st.sidebar.markdown('# About')
st.sidebar.write("Mental health is an essential aspect of our overall well-being, yet it is often overlooked or stigmatized in society. It encompasses our emotional, psychological, and social well-being, influencing how we think, feel, and act in our daily lives. Taking care of our mental health is just as important as taking care of our physical health. It involves finding a balance in life, managing stress effectively, maintaining positive relationships, and seeking support when needed. By prioritizing mental health and engaging in self-care practices such as mindfulness, exercise, and seeking therapy or counseling when necessary, we can enhance our resilience and lead fulfilling lives. Let's work together to break the stigma surrounding mental health and create a supportive environment where everyone feels empowered to prioritize their well-being.")

if navigation == 'EDA':
    eda.run()
elif navigation == 'Form Prediction':
    predict.run()
else:
    home.run()
