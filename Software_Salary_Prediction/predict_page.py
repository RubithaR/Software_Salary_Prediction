import streamlit as st
import pickle          # load the data
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file: # read bite
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_age = data["le_age"]
le_education = data["le_education"]
le_dev = data["le_dev"]
le_employment = data["le_employment"]

def show_predict_page():
    st.set_page_config(
        page_title="Salary Prediction",
        page_icon="💼",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.markdown(
        """
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);'>
            <h1 style='text-align: center; font-size: 50px; color: #4CAF50; font-family: Arial, sans-serif;'>
                Software Developer Salary Prediction
            </h1>
            <p style='text-align: center; color: #555; font-size: 18px;'>
                Make informed career decisions with our machine learning-powered salary prediction tool.
            </p>
        </div>
        
        """,
        unsafe_allow_html=True
    )

    countries = (
        'Pakistan', 'Austria', 'Turkey', 'France',
       'United States of America',
       'United Kingdom of Great Britain and Northern Ireland', 'Bulgaria',
       'Greece', 'Brazil', 'Germany', 'Italy', 'Ukraine',
       'Russian Federation', 'South Africa', 'Czech Republic', 'Canada',
       'Iran, Islamic Republic of...', 'Other', 'Switzerland', 'Belgium',
       'India', 'Ireland', 'Romania', 'Spain', 'Lithuania', 'Netherlands',
       'Slovenia', 'Singapore', 'Japan', 'Sweden', 'Poland', 'Norway',
       'Portugal', 'Finland', 'Israel', 'Serbia', 'Croatia', 'Hungary',
       'Bangladesh', 'Indonesia', 'Denmark', 'Mexico', 'Philippines',
       'Slovakia', 'Argentina', 'Colombia', 'Egypt', 'Australia',
       'New Zealand', 'Nigeria', 'Viet Nam', 'China', 'Sri Lanka',
       'Taiwan'
    )
    ages = (
        'Under 18 years old', '18-24 years old','25-34 years old', '35-44 years old', '45-54 years old',
        '55-64 years old', '65 years or older',

    )

    educations = (
        'Undergraduate', 'Graduate','Masters degree', 'Postgraduate',
        'High School or Below', 'Other'
    )
    developments = (
        'Full-Stack Developer', 'Back-End Developer',
        'Front-End Developer', 'Mobile Developer',
        'Desktop/Enterprise Application Developer', 'AI Developer','Other', 'Engineer',
    )
    employments=(
        'Full-time', 'Part-time'
    )
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)  # Adds 30px of space

    # Create columns for a structured layout
    col1, col2 = st.columns(2)

    with col1:
        country = st.selectbox(
            "Country",
            countries,
            help="Choose your country from the dropdown."
        )
        age = st.selectbox(
            "Your Age Group ",
            ages,
            help="Choose your age range from the dropdown."
        )
        education = st.selectbox(
            "Your Education Level:",
            educations,
            help="Pick your highest educational qualification."
        )

    with col2:
        development = st.selectbox(
            "Your Development Type:",
            developments,
            help="What type of developer are you? Choose from the list."
        )
        employment = st.selectbox(
            "Employment Type:",
            employments,
            help="Are you working full-time or part-time?"
        )
        expericence = st.slider(
            "Years of Professional Experience:",
            0, 50, 3,
            help="Use the slider to indicate how many years of experience you have."
        )
    st.markdown(
        """
        <style>
            div.stButton > button:first-child {
                background-color: #4CAF50;
                color: white;
                border: None;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                margin-top: 20px;
                cursor: pointer;
            }
            div.stButton > button:first-child:hover {
                background-color: #45a049;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    ok = st.button("Calculate Salary")
    if ok:
        # Recheck if all fields are filled
        if country == "Select" or age == "Select" or education == "Select" or development == "Select" or employment == "Select" or expericence is None:
            st.error("Please fill out all the required fields before calculating the salary.")
        else:
            X = np.array([[country, age,education,expericence,development,employment ]])
            X[:, 0] = le_country.transform(X[:, 0])
            X[:, 1] = le_age.transform(X[:, 1])
            X[:, 2] = le_education.transform(X[:, 2])
            X[:, 4] = le_dev.transform(X[:, 4])
            X[:, 5] = le_employment.transform(X[:, 5])
            X = X.astype(float)
            salary = regressor.predict(X)
            st.markdown(
                f"""
                   <div style='margin-top: 20px; padding: 20px; border-radius: 10px; 
                    background-color: #d4edda; color: #155724; font-family: Arial, sans-serif; 
                    font-size: 18px; font-weight: bold; text-align: center;'>
                    The estimated salary is : ${salary[0]:,.2f}
                    </div>
                """,
             unsafe_allow_html=True
            )



