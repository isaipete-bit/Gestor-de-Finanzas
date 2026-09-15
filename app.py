import streamlit as st
import pandas as pd

st.title("Tracker de Finanzas Personales")
st.write("Lleva el control de tus gastos e ingresos de manera simple y visual")
st.caption("Version 1.0.0")

categorias=["Alimentacion","Transporte","Entretenimiento","Salud","Educacion","Otros"]

if "transacciones" not in st.session_state:
    st.session_state.transacciones = []

with st.form("Nueva transaccion"):
    descripcion=st.text_input("Descripcion del gasto o ingreso",placeholder="Escribe la descripcion de la operacion")
    monto=st.number_input("Monto",step=1.0,min_value=0.0,format="%0.2f")
    fecha=st.date_input("Fecha")
    categoria=st.selectbox("Categoria",categorias)
    tipo=st.radio("Tipo de operacion",["Gasto","Ingreso"],horizontal=True)
    enviado=st.form_submit_button("Enviar")

if enviado:
    st.session_state.transacciones.append({"descripcion":descripcion,
                                                    "monto":monto,
                                                    "fecha":fecha,
                                                    "categoria":categoria,
                                                    "tipo":tipo})
    st.success("Transaccion agregada correctamente")

st.subheader("Transacciones registradas:")

if st.session_state.transacciones:
    df=pd.DataFrame(st.session_state.transacciones)
    st.dataframe(df)

else:
    st.info("No hay transacciones registradas")
