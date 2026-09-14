import streamlit as st

st.title("Tracker de Finanzas Personales")
st.write("Lleva el control de tus gastos e in gresos de manera simple y visual")
st.caption("Version 1.0.0")

categorias=["Alimentacion","Transporte","Entretenimiento","Salud","Educacion","Otros"]

descripcion=st.text_input("Descripcion del gasto o ingreso",placeholder="Escribe la descripcion de la operacion")
monto=st.number_input("Monto",step=1.0,min_value=0.0,format="%0.2f")
fecha=st.date_input("Fecha")
categoria=st.selectbox("Categoria",categorias)