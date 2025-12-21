import streamlit as st 
import pickle
import pandas as pd

st.title("Check If You Have Heart Disease 😳 Or Not 🤗 ??") 

st.header("Please Enter following details") 

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ",age," years old") 

gender = st.selectbox(
    "Please Enter Your Gender - Male(1) , Female(0)",
    (1, 0),
)
st.write("You Gender:", 'Male' if gender==1 else 'Female')

cp = st.selectbox(
    "Enter Chest Pain Value",
    (0,1,2,3)
)
st.write("Chest Pain: ",cp) 

trestbp = st.slider("Enter Your Resting Blood Pressure", 90, 200, 120)
st.write("Resting Blood Pressure: ",trestbp) 

chol = st.slider("Enter Your Serum Cholesterol", 126, 564, 196)
st.write("Serum Cholesterol: ",chol) 

fbs = st.selectbox(
    "Please Enter Your Fasting Blood Sugar",
    (1, 0),
)
st.write("Fasting Blood Sugar: ", fbs) 

RestECG = st.selectbox(
    "Enter RestECG Value",
    (0,1,2)
)
st.write("RestECG: ",RestECG) 

thalach = st.slider("Enter Maximum Heart Rate Achieved", 71, 202, 100)
st.write("Maximum Heart Rate Achieved: ",thalach) 

exang = st.selectbox(
    "Whether you experiences chest pain during exercise ?? 0 - No , 1 - Yes",
    (1, 0),
)
st.write("Whether you experiences chest pain during exercise: ",'Yes' if exang==1 else "No") 


Oldpeak = st.number_input(
    "Whether Depression Induced by Exercise Relative to Rest", value=0, placeholder="Type a number..."
)
st.write("Rate of Depression Induced by Exercise Relative to Rest", Oldpeak)

slope = st.selectbox(
    "the shape (slope) of the ST segment during peak exercise in an ECG ?? 0 - upsloping , 1 - flat , 2 - downsloping",
    (0,1,2)
)
st.write("Slope: ",slope) 

ca = st.selectbox(
    "Number of Major Vessels Colored by Fluoroscopy",
    (0,1,2,3,4)
)
st.write("Number of Major Vessels Colored by Fluoroscopy : ",ca) 

thal = st.selectbox(
    "Blood flow status of the heart based on a thallium stress test",
    (0,1,2,3)
)
st.write("blood flow status of the heart based on a thallium stress test : ",thal) 

button = st.button("Predict",type='primary')

sample = pd.DataFrame({
    'age': [age],
    'sex': [gender],
    'cp': [cp],
    'trestbps': [trestbp],
    'chol': [chol],
    'fbs': [fbs],
    'restecg': [RestECG],
    'thalach': [thalach],
    'exang': [exang],
    'oldpeak': [Oldpeak],
    'slope': [slope],
    'ca': [ca],
    'thal': [thal]
})

@st.cache_resource
def load_model():
    return pickle.load(open('model.pkl','rb')) 

model = load_model()

if button:
    prediction = model.predict(sample) 

    # st.write(":rainbow[Prediction] : ", "You May Have Heart Disease" if prediction[0] == 1 else "You Don't Have Heart Disease")

    if prediction[0] == 1:
        st.error("⚠️ You May Have Heart Disease") 
    else:
        st.success("✅ You Don't Have Heart Disease")

    # st.write("Prediction : ",prediction)