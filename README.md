# 💖 Heart Stroke Prediction App

A **Machine Learning-powered web application** that predicts the **risk of heart disease** based on user health data.  
Built with **Python**, **Streamlit**, and **Scikit-learn**, this app helps users understand their heart health risk instantly.

---

## 🚀 Live Demo  
🎯 **Try it here:** [Heart Stroke Prediction App](https://gg4vqgqmqcqj75b2xl33wn.streamlit.app/)

---

## 🧠 About the Project

Heart disease is one of the leading causes of death globally.  
This project uses **Machine Learning models** to predict whether a person is at **high risk** or **low risk** of heart disease based on medical parameters such as:

- Age  
- Sex  
- Chest Pain Type  
- Blood Pressure  
- Cholesterol  
- Fasting Blood Sugar  
- Maximum Heart Rate  
- ST Depression (Oldpeak)  
- Exercise-induced Angina  
- ECG and Slope results  

The app provides **real-time predictions** using an interactive **Streamlit** interface.

---

## ⚙️ Machine Learning Workflow

1. **Data Preprocessing**  
   - Cleaned and encoded categorical data.  
   - Scaled numerical features using `StandardScaler`.

2. **Model Training**  
   Trained multiple ML algorithms for comparison:
   - Logistic Regression  
   - K-Nearest Neighbors (KNN)  
   - Naive Bayes  
   - Decision Tree  
   - Support Vector Machine (SVM)

3. **Model Evaluation**  
   | Model | Accuracy | F1 Score |
   |:------|:---------:|:--------:|
   | Logistic Regression | 0.8696 | 0.8857 |
   | **KNN (Selected Model)** | **0.8641** | **0.8815** |
   | Naive Bayes | 0.8533 | 0.8683 |
   | Decision Tree | 0.7772 | 0.8000 |
   | SVM | 0.8478 | 0.8679 |

   ✅ **KNN was selected as the best-performing model** based on accuracy and F1 score.

4. **Model Saving**  
   - Trained model: `KNN_heart.pkl`  
   - Scaler: `scaler.pkl`  
   - Feature columns: `columns.pkl`

---

## 🌐 Tech Stack

| Category | Tools Used |
|-----------|-------------|
| **Frontend** | Streamlit 🎈 |
| **Backend** | Python 🐍 |
| **Machine Learning** | Scikit-learn 🤖 |
| **Data Handling** | Pandas, NumPy |
| **Model Persistence** | Joblib |

---

## 💡 Features

- 🧩 Interactive UI built using **Streamlit**  
- 📊 Real-time heart stroke prediction  
- ⚡ Fast & accurate model inference  
- 🔒 Secure — no data stored anywhere  
- 🎨 Clean design with animations and emoji indicators  

---

## 🧩 How It Works

1. User inputs medical details via sliders and dropdowns.  
2. The model processes the inputs and scales them.  
3. The KNN model predicts the heart stroke risk.  
4. The result is displayed with an intuitive message:
   - 💚 **Low Risk**  
   - ⚠️ **High Risk**



