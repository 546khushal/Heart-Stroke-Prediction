import streamlit as st
import pandas as pd
import joblib

# Load your trained model and preprocessing files
model = joblib.load('KNN_heart.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

# ---------- PAGE SETUP ----------
st.set_page_config(page_title="Heart Stroke Prediction", page_icon="💓", layout="centered")

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
    body {
        background-color: #f8f9fa;
        color: #2d3436;
    }
    .title {
        text-align: center;
        color: #e63946;
        font-size: 40px;
        font-weight: bold;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { color: #e63946; }
        50% { color: #ff758f; }
        100% { color: #e63946; }
    }
    .sub {
        text-align: center;
        font-size: 18px;
        color: #495057;
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #e63946;
        color: white;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 600;
        width: 100%;
        height: 50px;
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #ff5c8d;
        transform: scale(1.05);
    }
    .result-success {
        background-color: #d8f3dc;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 22px;
        color: #2b9348;
        animation: fadeIn 1s ease-in;
    }
    .result-error {
        background-color: #ffe5ec;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 22px;
        color: #e63946;
        animation: shake 0.5s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes shake {
        0% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        50% { transform: translateX(5px); }
        75% { transform: translateX(-5px); }
        100% { transform: translateX(0); }
    }
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">💖 Heart Stroke Prediction by Khushal 😊</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Please provide the following health details to predict your heart disease risk.</div>', unsafe_allow_html=True)

# ---------- INPUT FORM ----------
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 100, 40)
    sex = st.selectbox("Sex", ['M', 'F'])
    chest_pain = st.selectbox("Chest Pain Type", ['ATA', 'NAP', 'TA', 'ASY'])
    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)

with col2:
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
    max_hr = st.slider("Max Heart Rate", 60, 220, 150)
    exercise_angina = st.selectbox("Exercise Induced Angina", ["Y", "N"])
    oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

# ---------- PREDICTION ----------
if st.button("🔍 Predict"):
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    # Fill missing columns
    input_df = pd.DataFrame([raw_input])
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    # ---------- DISPLAY RESULT ----------
    if prediction == 1:
        st.markdown('<div class="result-error">⚠️ High Risk of Heart Disease</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-success">💚 Low Risk of Heart Disease</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("<br><hr><p style='text-align:center; color:gray;'>Made with ❤️ by Khushal Kumar</p>", unsafe_allow_html=True)
