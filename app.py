import streamlit as st
import pickle
st.title('Health Insurance Premium Prediction')
age = st.number_input('Age:')
bmi = st.number_input('BMI:')
childer = st.number_input('Number of Children:')
gender = st.selectbox('Select gender:',('NA','male','female'))

smoker = st.radio('Smoker (yes/no):',('yes','no'))
model = pickle.load(open('model.pkl', 'rb'))

if st.button('Predict'):
    gender = 0 if gender.upper() == 'MALE' else 1
    smoker = 0 if smoker.upper() == 'NO' else 1
    X_test = [[age, gender, bmi,childer, smoker]]
    yp=str(round(model.predict(X_test)[0],2))
    st.write('Your Premium is'+yp)