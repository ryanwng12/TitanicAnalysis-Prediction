#!/usr/bin/env python
# coding: utf-8



import pickle
import streamlit as st 

pickle_in = open("linear_svc.pkl","rb")
classifier=pickle.load(pickle_in)

def predict_survival(Pclass,sex,SibSp,Parch,Embarked,Age_band,Fare_band):
    
    prediction=classifier.predict([[Pclass,sex,SibSp,Parch,Embarked,Age_band,Fare_band]])
    print(prediction)
    return prediction


def main():
    st.title("Titanic Survival Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Titanic Survival Predictor ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    #Passenger Classes
    Pclass = st.selectbox("Which Passenger Class are you?",
                          ('First Class','Second Class','Third Class'))

    if Pclass == 'First Class':
        Pclass = 1
    elif Pclass == 'Second Class':
        Pclass = 2
    elif Pclass == 'Third Class':
        Pclass = 3

    #Gender of the passenger
    sex = st.radio("What's your gender?",('Male', 'Female'))

    if sex == 'Male':
         sex = 1
    else:
         sex = 0

    #Sibling or spouse present on board
    Ss = st.radio("Do you have siblings/spouse on board?",('No', 'Yes'))

    if Ss == 'Yes':
         SibSp = st.text_input("How many siblings/spouse?","Type Here")
    else:
         SibSp = 0
    
    #Parents or children present on board
    PC = st.radio("Do you have parents/children on board?",('No', 'Yes'))

    if PC == 'Yes':
         Parch = st.text_input("How many parents/children?","Type Here")
    else:
         Parch = 0
    
    #Boarding location of passenger
    Location = st.selectbox("Where did you depart?",
                          ('Cherbourg, France','Queenstown, Ireland','Southampton, England'))

    if Location == 'Cherbourg, France':
        Embarked = 0
    elif Location == 'Queenstown, Ireland':
        Embarked = 1
    elif Location == 'Southampton, England':
        Embarked = 2

    #Age of passenger
    Age = st.slider('How old are you?', 0, 100, 25)

    if Age <= 19:
        Age_band = 0
    elif Age > 19 & Age < 60:
        Age_band = 1
    elif Age >= 60:
        Age_band = 2

    #ticket fare of passenger
    tfare = st.number_input("Enter ticket fare, starting from £7", min_value = 7, step = 0.5)

    if tfare <= 13:
        Fare_band = 0
    elif Age > 13 & Age < 30:
        Fare_band = 1
    elif Age >= 30:
        Fare_band = 2

    #prediction output    
    result=""
    if st.button("Predict"):
        result=predict_survival(Pclass,sex,SibSp,Parch,Embarked,Age_band,Fare_band)
    st.success('The output is {}'.format(result))

    #Fun fact
    if st.button("Fun Fact"):
        st.write("""A third class ticket cost around £7 in 1912 which is nearly £800 in today's money.
                    A second class ticket cost around £13 or nearly £1500 today and a first class ticket
                    would have set you back a minimum of £30 or more than £3300 today.""")

    #Hiding hamburger menu
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}

            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    #footer {visibility: hidden;}

    #Customizing footer
    footer="""
    <div class='footer'>
    <p>Contact me!<a style='display:block;text-align:center;' 
    href='mailto:rwong696@gmail.com' target='_blank'>rwong696@gmail.com</a></p>
    </div>"""

    st.markdown(footer, unsafe_allow_html=True)

if __name__=='__main__':
    main()




