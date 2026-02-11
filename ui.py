import streamlit as st
import pickle
import numpy as np

# Load model
def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

st.title("Laptop Price Prediction")

st.write("Fill in the laptop specifications below to predict the price in euros.")

# Input fields
ram = st.number_input("RAM (GB)", min_value=2, max_value=64, step=2)
weight = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0, step=0.1)

company = st.selectbox("Company", ['acer','apple','asus','dell','hp','lenovo','msi','other','toshiba'])
typename = st.selectbox("Type Name", ['2in1convertible','gaming','netbook','notebook','ultrabook','workstation'])
opsys = st.selectbox("Operating System", ['linux','mac','other','windows'])
cpu = st.selectbox("CPU", ['amd','intelcorei3','intelcorei5','intelcorei7','other'])
gpu = st.selectbox("GPU", ['amd','intel','nvidia'])

touchscreen = st.checkbox("Touchscreen")
ips = st.checkbox("IPS Display")

# Predict button
if st.button("Predict Price"):
    feature_list = []
    feature_list.append(int(ram))
    feature_list.append(float(weight))
    feature_list.append(1 if touchscreen else 0)
    feature_list.append(1 if ips else 0)

    company_list = ['acer','apple','asus','dell','hp','lenovo','msi','other','toshiba']
    typename_list = ['2in1convertible','gaming','netbook','notebook','ultrabook','workstation']
    opsys_list = ['linux','mac','other','windows']
    cpu_list = ['amd','intelcorei3','intelcorei5','intelcorei7','other']
    gpu_list = ['amd','intel','nvidia']

    def traverse_list(lst, value):
        for item in lst:
            if item == value:
                feature_list.append(1)
            else:
                feature_list.append(0)

    traverse_list(company_list, company)
    traverse_list(typename_list, typename)
    traverse_list(opsys_list, opsys)
    traverse_list(cpu_list, cpu)
    traverse_list(gpu_list, gpu)

    pred_value = prediction(feature_list)
    pred_value = np.round(pred_value[0], 2) * 221

    st.success(f"Estimated Laptop Price: {pred_value:.2f}")
