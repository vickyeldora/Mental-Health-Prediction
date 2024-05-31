import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime

# Load the files
with open('best_model.pkl','rb') as file_1: # rb = read binary
    model_lin = pickle.load(file_1)

def run():

    st.title('Hello!')
    st.write('Please fill out this form as honestly and accurately as possible. Rest assured, your data and personal information are safe with us.')
    
    with st.form('Input Data for Prediction'):

        # Date and time input
        input_datetime_str = st.text_input("Date and Time MM/DD/YYYY HH:MM", "05/09/2024 12:00",help="Enter the current date and time")
        if input_datetime_str:
            try:
                input_datetime = datetime.strptime(input_datetime_str, "%m/%d/%Y %I:%M")
                st.write("Selected datetime:", input_datetime)
            except ValueError:
                st.error("Invalid input format. Please use the format MM/DD/YYYY HH:MM")

        st.title('Personal Details')

        age = st.slider('How old are you?', min_value=15, max_value=100, value=25, help='Enter your current age')
        sex = st.radio("What is your gender?", options=('Male', 'Female'))
        country = st.selectbox('Where are you from?', options=('United States', 'United Kingdom', 'Nigeria', 'Netherlands',
                                                               'Georgia', 'Canada', 'Singapore', 'Australia', 'Belgium',
                                                               'Germany', 'Ireland', 'Greece', 'Sweden', 'Switzerland',
                                                               'South Africa', 'Brazil', 'France', 'New Zealand', 'Colombia',
                                                               'Portugal', 'Finland', 'Denmark', 'Poland', 'India',
                                                               'Czech Republic', 'Israel', 'Mexico', 'Moldova', 'Philippines',
                                                               'Russia', 'Italy', 'Croatia', 'Costa Rica', 'Thailand'),help='Choose the country you currently live in')
        occupation = st.selectbox('What is your occupation?', options=('Business', 'Corporate', 'Housewife', 'Student', 'Others'),help='Choose your current occupation')
        income = st.number_input('What is your income?', min_value=0, max_value=8000000, value=2000000, help='Enter your monthly income in rupiah (Rp)')
        
        st.markdown('---')
        st.title('Health and Lifestyle')

        st.markdown('---')
        st.header('Employment and Family History')
        self_employed = st.radio("Are you self-employed?", options=('Yes', 'No'))
        family_history = st.radio("Do you have a family history of mental health illness?", options=('Yes', 'No'))
        treatment = st.radio("Have you sought treatment for a mental health condition?", options=('Yes', 'No'))

        st.markdown('---')
        st.header('Personal Habits and Stress Management')
        days_indoors = st.selectbox('How long do you typically stay indoors?', options=('1-14 days', '15-30 days', '31-60 days', 'Go out every day', 'More than 2 months'))
        growing_stress = st.radio("Do you easily get stressed?", options=('Yes','Maybe','No'))
        changes_habits = st.radio("Do you frequently find yourself unconsciously changing habits?", options=('Yes','Maybe','No'))
        
        st.markdown('---')
        st.header('Mental Health Details')
        mental_health_history = st.radio("Have you ever had any mental health issues previously?", options=('Yes','Maybe','No'))
        mood_swings = st.radio("Do your moods shift easily?", options=('Low', 'Medium', 'High'))
        coping_struggles = st.radio("Are you struggling with your coping mechanisms?", options=('Yes', 'No'))
        work_interest = st.radio("Are you interested in working?", options=('Yes','Maybe','No'))
        social_weakness = st.radio("Do you experience social weaknesses?", options=('Yes','Maybe','No'))
        mental_health_interview = st.radio("Would you bring up a mental health issue with a potential employer in an interview?", options=('Yes','Maybe','No'))
        
        st.markdown('---')
        submit = st.form_submit_button('Submit Form')
        pass

        df_inf = {
            'Timestamp':input_datetime_str, 
            'Age':age,
            'income':income,
            'duration':income,
            'Gender': sex, 
            'Country':country,
            'Occupation':occupation,
            'self_employed':self_employed,
            'family_history':family_history,
            'treatment':treatment,
            'Days_Indoors':days_indoors,
            'Growing_Stress':growing_stress,
            'Changes_Habits':changes_habits,
            'Mental_Health_History':mental_health_history,
            'Mood_Swings':mood_swings,
            'Coping_Struggles':coping_struggles,
            'Work_Interest':work_interest,
            'Social_Weakness':social_weakness,
            'mental_health_interview':mental_health_interview}

        #DATAFRAME
        df_new = pd.DataFrame([df_inf])
        if submit:
            st.info('Your answers have been recorded.', icon="ℹ️")  

            if submit:
                y_pred_inf = model_lin.predict(df_new)
                st.subheader("Prediction whether you need mental health care or not!")
                if y_pred_inf[0] == 1:
                    st.success("Yes, You Need Mental Health Care", icon="🤗")
                    st.snow()
                    
                elif y_pred_inf[0] == 0:
                    st.success("No, You Don't Need Mental Health Care", icon="😊")
                    st.balloons()
        
        # #DATAFRAME
        # df_new = pd.DataFrame([df_inf])
        # if submit:
        #     st.info('Your answers have been recorded.', icon="ℹ️")  
        #     y_pred_inf = model_lin.predict(df_new)
        #     st.subheader("Prediction whether you need mental health care or not!")
        #     if y_pred_inf[0] == 1:
        #         st.success("Yes, You Need Mental Health Care", icon="🤗")
        #         st.snow()
        #     elif y_pred_inf[0] == 0:
        #         st.success("No, You Don't Need Mental Health Care", icon="😊")
        #         st.balloons()

if __name__ == '__main__':
    run()