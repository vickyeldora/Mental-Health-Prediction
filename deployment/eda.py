# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from plotly.express import pie
from PIL import Image

def run():

    # create title
    st.title('Exploratory Data Analysis (EDA)')

    st.markdown('---')
    # create subheader
    st.subheader('Mental Health Dataset')
    
    container = st.container(border=True)
    # add description
    container.write('Exploring the Landscape of Mental Well-being: A Comprehensive Dataset Analysis')

    st.markdown('---')
    st.subheader('About Dataset')
    container = st.container(border=True)
    container.write('This dataset appears to contain a variety of features related to text analysis, sentiment analysis, and psychological indicators, likely derived from posts or text data. Some features include readability indices such as Automated Readability Index (ARI), Coleman Liau Index, and Flesch-Kincaid Grade Level, as well as sentiment analysis scores like sentiment compound, negative, neutral, and positive scores. Additionally, there are features related to psychological aspects such as economic stress, isolation, substance use, and domestic stress. The dataset seems to cover a wide range of linguistic, psychological, and behavioural attributes, potentially suitable for analyzing mental health-related topics in online communities or text data.')

    # Load dataset
    df=pd.read_csv('Mental Health Dataset.csv')
    st.dataframe(df)
    st.button('source', 'https://www.kaggle.com/datasets/bhavikjikadara/mental-health-dataset/discussion/488195', 'Mental Health Dataset') 
    st.markdown('---')

    
    st.write("### Personal Details")
    st.markdown('---')

    
    # Select options
    options = [
        "Gender Distribution",
        "Age Distribution",
        "Income Distribution",
        "Sleep Duration Distribution",
        "Respondent Country",
        "Respondent Occupation"
    ]

    # Selectbox for visualization selection
    selected_option = st.selectbox('Select Visualization', options)

    # Display selected visualization
    if selected_option == "Gender Distribution":
        # create pie chart
        Gender_counts = df['Gender'].value_counts()
        fig = px.pie(values=Gender_counts.values, names=Gender_counts.index, title='Gender Distribution')
        st.plotly_chart(fig)

        # Explanation
        expander = st.expander("See explanation")
        expander.write('''
            The chart above shows the distribution of genders in the dataset. There are more males than females, which could be due to various factors such as societal norms, gender biases, or differences in response rates to the survey.
        ''')
    elif selected_option == "Age Distribution":
        # Plot histogram
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(df['Age'], kde=True, bins=20, color='blue', ax=ax)
        ax.set_xlabel('Age')
        ax.set_ylabel('Frequency')
        ax.set_title('Distribution of Age')
        st.pyplot(fig)

        # Explanation
        expander = st.expander("See explanation")
        expander.write('''
            This is the explanation for the Age column. The age ranges from 20 to 60 years.
        ''')
    elif selected_option == "Income Distribution":
        # Plot histogram
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(df['income'], kde=True, bins=20, color='blue', ax=ax)
        ax.set_xlabel('Income')
        ax.set_ylabel('Frequency')
        ax.set_title('Distribution of Income')
        st.pyplot(fig)

        # Explanation
        expander = st.expander("See explanation")
        expander.write('''
            This is the explanation for the income column. The income varies from Rp 1,500,000 to Rp 8,000,000.
        ''')
    elif selected_option == "Sleep Duration Distribution":
        # Plot histogram
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(df['sleep duration'], kde=True, bins=20, color='blue', ax=ax)
        ax.set_xlabel('Sleep Duration')
        ax.set_ylabel('Frequency')
        ax.set_title('Distribution of Sleep Duration')
        st.pyplot(fig)

        # Explanation
        expander = st.expander("See explanation")
        expander.write('''
            This is the explanation for the sleep duration column. The sleep duration ranges from 3 to 13 hours.
        ''')
    elif selected_option == "Respondent Country":
        # Create country bar
        bar_df = df['Country'].value_counts().reset_index()
        bar_df.columns = ['Country', 'Count']

        # Plot the bar plot
        fig = px.bar(bar_df, x="Country", y="Count", title="Respondent Country")
        fig.update_xaxes(title="Country", tickangle=-90)
        fig.update_yaxes(title="Count")
        st.plotly_chart(fig)

        # Explanation
        expander = st.expander("See explanation")
        expander.write('''
            The chart above shows the distribution of respondents by country in the dataset. The most frequent country is the United States, followed by the United Kingdom, Canada, Ireland, Australia, Netherlands, Germany, Sweden, France, and Brazil. This could be attributed to a higher number of respondents distributing the survey questions in the United States.
        ''')
    elif selected_option == "Respondent Occupation":
        # Create occupation bar
        bar_df = df['Occupation'].value_counts().reset_index()
        bar_df.columns = ['Occupation', 'Count']

        # Plot the bar plot
        fig = px.bar(bar_df, x="Occupation", y="Count", title="Respondent Occupation")
        fig.update_xaxes(title="Occupation")
        fig.update_yaxes(title="Count")
        st.plotly_chart(fig)

        # Explanation
        expander = st.expander("See explanation")
        expander.write('''
            The chart above shows the distribution of respondents by occupation in the dataset. The highest percentage is for housewives at 22.7%, followed by students at 21.1%. Corporate and other occupations are nearly tied at around 21.1% and 18% respectively, while business occupation accounts for 17.1%. The high percentage of housewives may be because they are more likely to be available to participate in surveys compared to individuals in full-time employment.
        ''')
    
    # # create pie chart
    # Gender_counts = df['Gender'].value_counts()  # Get Gender distribution
    # fig = px.pie(values=Gender_counts.values, names=Gender_counts.index, title='Gender Distribution')
    # st.plotly_chart(fig)

    # # Explanation
    # expander = st.expander("See explanation")
    # expander.write('''
    #     The chart above shows the distribution of genders in the dataset. There are more males than females, which could be due to various factors such as societal norms, gender biases, or differences in response rates to the survey.
    # ''')

    # # Select numeric columns
    # num_col = df.select_dtypes(include=np.number).columns.tolist()

    # # Selectbox for column selection
    # selected_column = st.selectbox('Select Column to Visualize', num_col)

    # # Plot histogram
    # fig, ax = plt.subplots(figsize=(10, 6))
    # sns.histplot(df[selected_column], kde=True, bins=20, color='blue', ax=ax)
    # ax.set_xlabel(selected_column)
    # ax.set_ylabel('Frequency')
    # ax.set_title(f'Distribution of {selected_column}')
    # st.pyplot(fig)

    # # Explanation
    # if selected_column:
    #     with st.expander("See explanation"):
    #         if selected_column == 'Age':
    #             st.write('''
    #                 This is the explanation for the Age column. The age ranges from 20 to 60 years.
    #             ''')
    #         elif selected_column == 'income':
    #             st.write('''
    #                 This is the explanation for the income column. The income varies from Rp 1,500,000 to Rp 8,000,000.
    #             ''')
    #         elif selected_column == 'sleep duration':
    #             st.write('''
    #                 This is the explanation for the sleep duration column. The sleep duration ranges from 3 to 13 hours.
    #             ''')    

    # # Create country bar
    # bar_df = df['Country'].value_counts().reset_index()
    # bar_df.columns = ['Country', 'Count']

    # # Plot the bar plot
    # fig = px.bar(bar_df, x="Country", y="Count", title="Respondent Country")
    # fig.update_xaxes(title="Country", tickangle=-90)
    # fig.update_yaxes(title="Count")
    # st.plotly_chart(fig)

    # # Explanation
    # expander = st.expander("See explanation")
    # expander.write('''
    #     The chart above shows the distribution of genders in the dataset. The most frequent country is the United States, followed by the United Kingdom, Canada, Ireland, Australia, Netherlands, Germany, Sweden, France, and Brazil. This could be attributed to a higher number of respondents distributing the survey questions in the United States
    # ''')

    # # Create occupation bar
    # bar_df = df['Occupation'].value_counts().reset_index()
    # bar_df.columns = ['Occupation', 'Count']

    # # Plot the bar plot
    # fig = px.bar(bar_df, x="Occupation", y="Count", title="Respondent Occupation")
    # fig.update_xaxes(title="Country")
    # fig.update_yaxes(title="Count")
    # st.plotly_chart(fig)

    # # Explanation
    # expander = st.expander("See explanation")
    # expander.write('''
    #     The chart above shows the distribution of genders in the dataset. The highest percentage is for housewives at 22.7%, followed by students at 21.1%. Corporate and other occupations are nearly tied at around 21.1% and 18% respectively, while business occupation accounts for 17.1%. The high percentage of housewives may be because they are more likely to be available to participate in surveys compared to individuals in full-time employment.
    # ''')

    # Selectbox for bar
    st.markdown('---')
    st.write("### Health and Lifestyle")

    st.markdown('---')
    st.write("#### Employment and Family History")
    pilihan = st.selectbox('Select Column to Visualize',
                        ('self_employed', 'family_history', 'treatment'))
    if pilihan:
        fig = plt.figure(figsize=(15,5))
        st.bar_chart(df[pilihan].value_counts())
        st.pyplot(fig)
        
        # Explanation
        with st.expander("See explanation"):
            if pilihan == 'self_employed':
                st.write('''
                    This is the explanation for the self_employed column. The majority is "No". This could be because self-employment often requires a higher level of risk tolerance and entrepreneurial spirit, which may not be prevalent among respondents.
                ''')
            elif pilihan == 'family_history':
                st.write('''
                    This is the explanation for the family_history column. "No" is predominant at 58.2%, while "Yes" accounts for 41.8%. The lower percentage of individuals with a family history of mental health issues could be due to underreporting or lack of awareness of family history among respondents.
                ''')
            elif pilihan == 'treatment':
                st.write('''
                    This is the explanation for the treatment column. "Yes" prevails at 54.5%, while "No" stands at 45.5%. The higher percentage of individuals seeking treatment could indicate an increasing awareness and acceptance of mental health issues, as well as improved access to mental health services.
                ''')

    # Selectbox for bar
    st.markdown('---')
    st.write("#### Personal Habits and Stress Management")
    pilihan = st.selectbox('Select Column to Visualize',
                        ('Days_Indoors', 'Growing_Stress', 'Changes_Habits'))
    if pilihan:
        fig = plt.figure(figsize=(15,5))
        st.bar_chart(df[pilihan].value_counts())
        st.pyplot(fig)
        
        # Explanation
        with st.expander("See explanation"):
            if pilihan == 'Days_Indoors':
                st.write('''
                    This is the explanation for the Days_Indoors column. The percentages are quite similar across different ranges, indicating that respondents' indoor activities are evenly distributed across various time periods.
                ''')
            elif pilihan == 'Growing_Stress':
                st.write('''
                    This is the explanation for the Growing_Stress column. "Yes," "Maybe," and "No" have similar percentages in the 30s range, suggesting that stress levels are distributed relatively evenly among respondents.
                ''')
            elif pilihan == 'Changes_Habits':
                st.write('''
                    This is the explanation for the Changes_Habits column. "Yes," "Maybe," and "No" have similar percentages in the 30s range, indicating that respondents' tendencies to change habits are consistent across different categories.
                ''')

    # Selectbox for bar
    st.markdown('---')
    st.write("#### Mental Health Details")
    pilihan = st.selectbox('Select Column to Visualize',
                        ('Mental_Health_History', 'Mood_Swings', 'Coping_Struggles',
                        'Work_Interest', 'Social_Weakness', 'mental_health_interview'))
    if pilihan:
        fig = plt.figure(figsize=(15,5))
        st.bar_chart(df[pilihan].value_counts())
        st.pyplot(fig)
        
        # Explanation
        with st.expander("See explanation"):
            if pilihan == 'Mental_Health_History':
                st.write('''
                    This is the explanation for the Mental_Health_History column. "Yes," "Maybe," and "No" have similar percentages in the 30s range, suggesting that respondents' awareness or acknowledgment of their mental health history is evenly distributed.
                ''')
            elif pilihan == 'Mood_Swings':
                st.write('''
                    This is the explanation for the Mood_Swings column. "Low," "Medium," and "High" have similar percentages in the 30s range, indicating that respondents' experiences of mood swings are distributed relatively evenly across different intensity levels.
                ''')
            elif pilihan == 'Coping_Struggles':
                st.write('''
                    This is the explanation for the Coping_Struggles column. "Yes" is more prevalent than "No," with "Yes" at 52.9% and "No" at 47.1%. This could indicate a significant portion of respondents experiencing coping struggles, possibly due to various stressors or mental health challenges.
                ''')
            elif pilihan == 'Work_Interest':
                st.write('''
                    This is the explanation for the Work_Interest column. "Yes," "Maybe," and "No" have similar percentages in the 30s range, suggesting that respondents' interest in work is consistent across different categories.
                ''')
            elif pilihan == 'Social_Weakness':
                st.write('''
                    This is the explanation for the Social_Weakness column.
                ''')
            elif pilihan == 'mental_health_interview':
                st.write('''
                    This is the explanation for the mental_health_interview column. The majority is "No" at 79.8%, followed by "Maybe" at 17.1%, and "Yes" at 3.1%. The lower percentage of individuals undergoing mental health interviews could be due to various factors such as stigma, lack of awareness, or limited access to mental health services.
                ''')

    # create bar chart
    st.markdown('---')
    st.write("#### Care Options")
    st.write("care_options")
    st.bar_chart(df['care_options'].value_counts())

    # Explanation
    expander = st.expander("See explanation")
    expander.write('''
        The chart above shows the distribution of countries in the dataset. "No" accounts for 55.4%, while "Yes" accounts for 44.6%. The lower percentage of individuals opting for care options could be due to barriers such as cost, stigma, or lack of awareness of available resources.
    ''')

if __name__ == "__main__":
    run()
