import streamlit as st
import numpy as np

csfont = {'fontname':'Times New Roman'}

#--------------------Pilot Part-------------------#

dominios=st.sidebar.radio("Proyecto 1 - Hidraulica",("Caudal","Perdidas",),key=1) 
if dominios=="Caudal":
    listaFunc=[" ","función (1)", "función (2)", "función (3)", "función (4)", "función (5)"]
    Deltas=0.01
    funcion=st.sidebar.selectbox("Menú",listaFunc, key=5)
    if funcion==" ":
        st.title("Bienvenido!")
        st.write("En esta sección se realizaran los calculos correspondientes a un caudal ")
 
elif dominios=="Perdidas":
    listaFunc=[" ","Señal (1)", "Señal (2)", "Señal (3)"]
    listaFunc1=[" ","Portadora (1)", "Portadora (2)", "Portadora (3)"]
    Deltas=0.01
    funcion=st.sidebar.selectbox("Menú",listaFunc, key=6)
    if funcion==" ":
        st.title("Bienvenido!")
        st.write("En esta sección se realizaron los calculos de perdidas")
    elif funcion=="Señal (1)" or funcion=="Señal (2)" or funcion=="Señal (3)":
        funcionp1=st.sidebar.selectbox("Menú",listaFunc1, key=40)
        if funcion==" ":
            st.title("Bienvenido!")
            st.write("Por favor seleccione un par de funciones del menú para comenzar con la representacion de señales con series de Fourier")


