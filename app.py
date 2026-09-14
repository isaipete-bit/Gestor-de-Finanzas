import streamlit as st

st.title("Tracker de Finanzas Personales")
st.write("Lleva el control de tus gastos e in gresos de manera simple y visual")
st.markdown("Version 1.0.0")

descripcion=st.text_input("Descripcion del gasto o ingreso",placeholder="Escribe la descripcion de la operacion")
st.write("Escribiste: ", descripcion)