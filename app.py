import streamlit as st
import pandas as pd
import pickle

# Load the preprocessor & model
with open("preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)
with open("rf_salary_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Employee Salary Prediction")
st.write("Predict whether an employee earns >50K or <=50K based on features.")

# --- User Inputs ---
age = st.slider("Age", 17, 90, 30)
workclass = st.selectbox("Workclass", ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked'])
education = st.selectbox("Education", ['Bachelors','Some-college','11th','HS-grad','Prof-school','Assoc-acdm','Assoc-voc','9th','7th-8th','12th','Masters','1st-4th','10th','Doctorate','5th-6th','Preschool'])
educational_num = st.slider("Educational Num", 1, 16, 10)
marital_status = st.selectbox("Marital Status", ['Married-civ-spouse','Divorced','Never-married','Separated','Widowed','Married-spouse-absent','Married-AF-spouse'])
occupation = st.selectbox("Occupation", ['Tech-support','Craft-repair','Other-service','Sales','Exec-managerial','Prof-specialty','Handlers-cleaners','Machine-op-inspct','Adm-clerical','Farming-fishing','Transport-moving','Priv-house-serv','Protective-serv','Armed-Forces'])
relationship = st.selectbox("Relationship", ['Wife','Own-child','Husband','Not-in-family','Other-relative','Unmarried'])
race = st.selectbox("Race", ['White','Asian-Pac-Islander','Amer-Indian-Eskimo','Other','Black'])
gender = st.selectbox("Gender", ['Male','Female'])
hours_per_week = st.slider("Hours Per Week", 1, 99, 40)
native_country = st.selectbox("Native Country", ['United-States','Cambodia','England','Puerto-Rico','Canada','Germany','Outlying-US(Guam-USVI-etc)','India','Japan','Greece','South','China','Cuba','Iran','Honduras','Philippines','Italy','Poland','Jamaica','Vietnam','Mexico','Portugal','Ireland','France','Dominican-Republic','Laos','Ecuador','Taiwan','Haiti','Columbia','Hungary','Guatemala','Nicaragua','Scotland','Thailand','Yugoslavia','El-Salvador','Trinadad&Tobago','Peru','Hong','Holand-Netherlands'])

# Prepare input data
input_data = pd.DataFrame([{
    'age': age,
    'workclass': workclass,
    'education': education,
    'educational_num': educational_num,
    'marital_status': marital_status,
    'occupation': occupation,
    'relationship': relationship,
    'race': race,
    'gender': gender,
    'hours_per_week': hours_per_week,
    'native_country': native_country,
    'capital_gain': 0  # <-- Add dummy value to satisfy preprocessor
}])

# Predict button
if st.button("Predict"):
    input_processed = preprocessor.transform(input_data)
    prediction = model.predict(input_processed)
    result = ">50K" if prediction[0] == 1 else "<=50K"
    st.subheader(f"Predicted Income: {result}")
