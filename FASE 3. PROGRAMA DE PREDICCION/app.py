import streamlit as st
import pandas as pd
import pickle
from PIL import Image  # Librería para manejar imágenes
import matplotlib.pyplot as plt
import seaborn as sns  # si usas seaborn
import numpy as np

modelo = pickle.load(open("modelo_hospital.pkl", "rb"))

# CArgamos imagen del proyecto
imagen = Image.open("Imagen1.png")

# Mostrar en Streamlit
st.image(imagen)

# CABECERA DEL PROGRAMA
st.title("Predicción de Estancia Hospitalaria")
st.markdown("Esta app predice la duración de la estancia de un paciente usando el modelo entrenado.")

# SECCIÓN 1: INFORMACIÓN DE HOSPITAL
st.header("Información del Hospital")
col1, col2, col3 = st.columns(3)
with col1:
    Hospital_code = st.selectbox('Hospital_code', list(range(1,33)))
    Hospital_type_code = st.selectbox('Hospital_type_code', ["a", "b", "c", "d", "e", "f", "g"])
    City_Code_Hospital = st.selectbox('City_Code_Hospital', [1,2,3,4,5,6,7,9,10,11,13])
    Hospital_region_code = st.selectbox('Hospital_region_code', ["X", "Y", "Z"])
with col2:
    Extra_Rooms = st.number_input('Available Extra Rooms', min_value=1, max_value=24, value=5)
    Department = st.selectbox('Department', ["TB & Chest disease", "anesthesia", "gynecology", "radiotherapy", "surgery"])
    Ward_Facility_Code = st.selectbox('Ward_Facility_Code',  ["A", "B", "C", "D", "E", "F", "G"])
with col3:
    Bed_Grade = st.selectbox('Bed Grade',[1,2,3,4])
    Ward_Type = st.selectbox('Ward Type',["P","Q","R","S","T","U"])

# SECCIÓN 2: INFORMACIÓN DE PACIENTE
st.header("Información del Paciente")
col1, col2 = st.columns(2)
with col1:
    City_Code_Patient = st.selectbox('City_Code_Patient', list(range(1,39)))
    Visitors = st.number_input('Visitors with Patient', min_value=1, max_value=32, value=2)
    Age = st.selectbox('Age', ["0-20", "21-50", "51-70", "71-100"])
with col2:
    Depossit = st.number_input('Admission_Deposit', min_value=15000, max_value=120000, step=5000, value=20000)
    Registros_paciente = st.number_input('Numero_registros_paciente', min_value=1, max_value=100, value=1)
    Severity_of_Illness = st.selectbox("Severity of Illness", ["Minor","Moderate","Extreme"])
    Type_of_Admission = st.selectbox("Type of Admission", ["Emergency","Trauma","Urgent"])

# SECCIÓN PREDICCIÓN
if st.button("Predecir estancia"):

    # Crear DataFrame con todos los inputs
    datos = pd.DataFrame({
        "Hospital_code":[Hospital_code],
        "Hospital_type_code":[Hospital_type_code],
        "City_Code_Hospital":[City_Code_Hospital],
        "Hospital_region_code":[Hospital_region_code],
        "Extra_Rooms":[Extra_Rooms],
        "Department":[Department],
        "Ward_Facility_Code":[Ward_Facility_Code],
        "Bed_Grade":[Bed_Grade],
        "Ward_Type":[Ward_Type],
        "City_Code_Patient":[City_Code_Patient],
        "Visitors":[Visitors],
        "Type_of_Admission":[Type_of_Admission],
        "Severity_of_Illness":[Severity_of_Illness],
        "Age":[Age],
        "Admission_Deposit":[Depossit],
        "Numero_registros_paciente":[Registros_paciente]
    })

    # DUMMIES PARA LAS COLUMNAS CATEGÓRICAS
    datos_dummies = pd.get_dummies(datos)
    modelo_columns = modelo.get_booster().feature_names
    for col in modelo_columns:
        if col not in datos_dummies.columns:
            datos_dummies[col] = 0
    datos_dummies = datos_dummies[modelo_columns]
    
    # PREDICCIÓN
    pred = modelo.predict(datos_dummies)
    
    # Extraemos el primer valor y convertimos a entero
    pred_int = int(pred[0])  # <-- ¡ojo! pred[0] y luego int()
    
    # Diccionario para cambiar la predicción de numérico a texto
    etiquetas = {
        0: "De 0 a 10 días",
        1: "De 11 a 40 días",
        2: "Más de 40 días"
    }
    
    # Lo pasamos a variable
    resultado_texto = etiquetas.get(pred_int, "Valor desconocido")
    
    # Muestra del resultado de la predicción
    st.markdown(
        f"""
        <div style="
            background-color:#F0E199; 
            padding:20px; 
            border-radius:15px; 
            text-align:center;
            font-size:28px;
            font-weight:bold;
            color:#34742E;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.3);
        ">
            🏥 Predicción de Estancia: {resultado_texto}
        </div>
        """, 
        unsafe_allow_html=True
    )