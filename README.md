🔒 Cyber Threat Detection Using Machine Learning (XGBoost + Streamlit)

🚀 Project Overview

This project applies Machine Learning to detect cyber attacks in network traffic using the NSL-KDD dataset. The model classifies whether a given network activity is normal or an attack. The entire pipeline is built using:

XGBoost Classifier for modeling

Streamlit for a real-time interactive web app

🧠 Key Features

End-to-end ML pipeline: from data preprocessing to model evaluation

Outlier handling and feature scaling

Label encoding of attack types

Hyperparameter tuning using GridSearchCV

Real-time predictions using a trained model

Streamlit-based UI for manual and file-based input testing

📊 Dataset Used

Dataset: NSL-KDD (KDDTest+.arff)

Source: Kaggle

Target Variable: attack

Label was simplified to two classes: normal and attack

🛠️ Steps Performed

Data Loading & Cleaning

Missing Value & Duplicate Handling

Outlier Detection (Z-score method)

Label Encoding for Categorical Fields

Attack Label Simplification (normal or attack)

Exploratory Data Analysis (EDA)

Feature Selection (Correlation)

Train-Test Split

Scaling with StandardScaler

Model Training using XGBoost

Hyperparameter Tuning

Evaluation (98% Accuracy)

Model Serialization (pickle)

Deployment via Streamlit

💻 Local Setup Instructions

Clone the repo:

git clone https://github.com/Moon0Knight1/cyber-threat-detection.git
cd cyber-threat-detection

Install requirements:

pip install -r requirements.txt

Run the app:

streamlit run app.py(on cmd)

📂 Repository Structure
cyber-threat-detection/
├── data/
│   ├── KDDTest+.csv
│   └── sample_attack_normal_data.csv
├── notebooks/
│   └── eda_modeling.ipynb
|   |── save_model.pkl
|   ├── scaler.pkl
|   ├── label_encoder.pkl
├── app/
│   └── app.py
├── results/
│   └── confusion_matrix.png
│   └── roc_curve.png
├── requirements.txt
└── README.md


📌 Author

Name: Azlan Qureshi

Role: Developer, Data Scientist

📫 Feel free to connect on LinkedIn(https://www.linkedin.com/in/onlyazlan/)