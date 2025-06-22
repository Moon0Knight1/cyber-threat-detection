import streamlit as st
import numpy as np
import pandas as pd
import pickle

# ----------------------------
# Load saved model and tools
# ----------------------------
with open(r"C:\Users\SAMI ULLAH\Desktop\cyber-threat-detection-ml\notebooks\save_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load scaler (optional)
try:
    with open(r"C:\Users\SAMI ULLAH\Desktop\cyber-threat-detection-ml\notebooks\scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    scaler_used = True
except:
    scaler_used = False

# Load label encoder (optional)
try:
    with open(r"C:\Users\SAMI ULLAH\Desktop\cyber-threat-detection-ml\notebooks\label_encoder.pkl", "rb") as f:
        le = pickle.load(f)
    label_encoder_used = True
except:
    label_encoder_used = False
    class_map = {0: 'attack', 1: 'normal'}

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("🚨 Cyber Threat Detection (ML Model)")
st.markdown("Upload a CSV file **or** enter a single sample below to check if it's an `attack` or `normal`.")

# ----------------------------
# CSV Upload Section
# ----------------------------
uploaded_file = st.file_uploader("📂 Upload CSV for Batch Prediction", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### 🧾 Uploaded Data Preview", df.head())

    input_data = df.values

    if scaler_used:
        input_data = scaler.transform(input_data)

    preds = model.predict(input_data)

    if label_encoder_used:
        decoded_preds = le.inverse_transform(preds)
    else:
        decoded_preds = [class_map.get(p, "Unknown") for p in preds]

    df['Prediction'] = decoded_preds
    st.write("### ✅ Prediction Results", df)
    st.download_button("Download Results as CSV", df.to_csv(index=False), file_name="prediction_results.csv")

# ----------------------------
# Manual Input Section
# ----------------------------
st.markdown("---")
st.subheader("🧪 Or Manually Enter Feature Values")

with st.form("manual_form"):
    input_text = st.text_input("Enter 15 numeric values (comma-separated)", "0,1,40,0,0,0,0,0,1,0,0,0,0,0,0")
    submitted = st.form_submit_button("Predict")

    if submitted:
        try:
            manual_values = [float(x.strip()) for x in input_text.split(",")]
            if len(manual_values) != 15:
                st.error("❌ Please enter exactly 15 numeric values.")
            else:
                input_array = np.array(manual_values).reshape(1, -1)

                if scaler_used:
                    input_array = scaler.transform(input_array)

                pred = model.predict(input_array)

                if label_encoder_used:
                    label = le.inverse_transform(pred)[0]
                else:
                    label = class_map.get(pred[0], "Unknown")

                st.success(f"✅ Prediction: **{label.upper()}**")
        except Exception as e:
            st.error(f"❌ Error: {e}")
