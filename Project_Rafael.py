import streamlit as st
import numpy as np

csfont = {'fontname':'Times New Roman'}

#--------------------Pilot Part-------------------#

def Perdidas():
    Q=st.number_input("Digite el valor del caudal (m^3/s):\n", min_value=1e-8, max_value=1e8, value=1.00000, step=0.00001, format="%.10f")
    L=st.number_input("Digite el valor de la longitud (m):\n", min_value=1e-8, max_value=1e8, value=1.00000, step=0.00001, format="%.10f")
    D=st.number_input("Digite el valor del diametro (m):\n", min_value=1e-8, max_value=1e8, value=1.00000, step=0.00001, format="%.10f")
    ks=st.number_input("Digite el valor de la rugosidad de la tuberia(m):\n", min_value=1e-8, max_value=1e8, value=1.00000, step=0.00001, format="%.10f")
    u=st.number_input("Digite el valor de la viscosidad cinematica (m^2/s):\n", min_value=1e-8, max_value=1e8, value=1.00000, step=0.00001, format="%.10f")
    E=st.number_input("Digite el valor del Error:\n", min_value=1e-8, max_value=1e8, value=1.00000, step=0.00001, format="%.10f")
    A=np.pi*(D**2)/4
    V=Q/A
    Re=(V*D)/u
    fi=st.number_input("Digite el valor de fi:\n", min_value=1e-8, max_value=1e8, value=1.00000, step=0.00001, format="%.10f")
    def i(fi):
        fi1=(1/(-2*np.log10((ks/(3.7*D)+2.51/(Re*np.sqrt(fi))))))**2
        return fi1
    fi1=i(fi)
    DE=abs(fi-fi1)
    while E<DE:
        temp=fi1
        fi=temp
        fi1=i(temp)
        DE=abs(fi-fi1)
    Hf=(fi1*L*(V**2))/(2*D*9.81)
    st.write("El valor del coeficiente de fricción f es: ",fi1)
    st.write("El valor de la perdida de cabeza por friccion es:",Hf)
    
    
def Caudal():
    l = st.number_input("Digite el valor de la longitud (m):\n", value=1.0000000, format="%.10f")
    d = st.number_input("Digite el valor del diametro (m):\n", value=1.00000, format="%.10f")
    ks = st.number_input("Digite el valor de la rugosidad de la tuberia (m):\n", value=1.00000, format="%.10f")
    v = st.number_input("Digite el valor de la viscosidad cinematica (m^2/s):\n", value=1.00000, format="%.10f")
    E = st.number_input("Digite el valor del Error:\n",value=1.00000, step=0.00001, format="%.10f")
    km = st.number_input("Digite el valor de las perdidas menores (m):\n", value=0.0000000000, format="%.10f")
    z2 = st.number_input("Digite el valor de z2 (m):\n", value=0.0000000000, format="%.10f")
    H = st.number_input("Digite el valor de la altura total (m):\n", value=1.000000, format="%.10f")
    hf = H
    A = np.pi*(d**2)/4
    Vi = (-2*np.sqrt(2*9.81*d*hf/l))*np.log10((ks/(3.7*d))+((2.51*v*np.sqrt(l))/(d*np.sqrt(2*9.81*d*hf))))    
    hfi = H-z2-km*(Vi**2)/(2*9.81)
    def i(hf):
        Vi1 = (-2 * np.sqrt(2 * 9.81 * d * hf / l)) * np.log10((ks / (3.7 * d)) + ((2.51 * v * np.sqrt(l)) / (d * np.sqrt(2 * 9.81 * d * hf))))
        hf1 = H - z2 - km * (Vi1 ** 2) / (2 * 9.81)
        return hf1, Vi1
    DE = abs(hf - hfi)
    while E < DE:
        temp1 = hfi
        iteracion = i(temp1)
        hfi1 = iteracion[0]
        Vi = iteracion[1]
        DE = abs(hfi- hfi1)
        hfi=hfi1
    Q = Vi * A    
    st.write("El valor del caudal es:",Q)
    
    
def Diametro():
    Qd=st.number_input("Digite el valor del caudal de diseño (m^3/s):\n", value=1.00000, format="%.10f")
    l=st.number_input("Digite el valor de la longitud de la tuberia (m):\n", value=1.00000, format="%.10f")
    ks=st.number_input("Digite el valor de la rugosidad de la tuberia (m):\n", value=1.00000, format="%.10f")
    v=st.number_input("Digite el valor de la viscosidad cinematica (m^2/s):\n", value=1.00000, format="%.10f")
    km=st.number_input("Digite el valor de las perdidas menores (m):\n", value=0.00000, format="%.10f")
    z2=st.number_input("Digite el valor de z2 (m):\n", value=0.00000, format="%.10f")
    H=st.number_input("Digite el valor de la altura total (m):\n", value=0.00000, format="%.10f")
    hf=H-z2
    E=0.01
    Ev=0.01
    Δd=0.005
    Δh=0.05
    di=0.005
    A=np.pi*(di**2)/4
    Vi=(-2*np.sqrt(2*9.81*di*hf/l))*np.log10((ks/(3.7*di))+((2.51*v*np.sqrt(l))/(di*np.sqrt(2*9.81*di*hf))))
    
    Q=Vi*A
    hfi=H-z2-km*(Vi**2)/(2*9.81)
    
    def i(hf):
        Vi1=(-2*np.sqrt(2*9.81*di*hf/l))*np.log10((ks/(3.7*di))+((2.51*v*np.sqrt(l))/(di*np.sqrt(2*9.81*di*hf))))
        hf1=H-z2-km*(Vi1**2)/(2*9.81)
        return hf1,Vi1

    DE=abs(hf-hfi)
    while E<DE:
        temp1=hfi
        iteracion=i(temp1)    
        hfi=iteracion[0]
        Q=iteracion[1]*A
        DE=abs(hf-hfi)
    Cdl=Q
    st.write("El valor del caudal es:", Cdl)
    
def Potencia():
    l=st.number_input("Digite el valor de la longitud (m):\n", min_value=1e-8, max_value=1e3, value=1.00000, step=0.00001, format="%.10f")
    d=st.number_input("Digite el valor del diametro (m):\n", min_value=1e-8, max_value=1e3, value=1.00000, step=0.00001, format="%.10f")
    ks=st.number_input("Digite el valor de la rugosidad del material (m):\n", min_value=1e-8, max_value=1e3, value=1.00000, step=0.00001, format="%.10f")
    μ=st.number_input("Digite el valor de la viscosidad (pa*s):\n", min_value=1e-8, max_value=1e3, value=1.00000, step=0.00001, format="%.10f")
    E=st.number_input("Digite el valor del Error:\n", min_value=1e-8, max_value=1e3, value=1.00000, step=0.00001, format="%.10f")
    km=st.number_input("Digite el valor de las perdidas menores (m):\n", min_value=1e-8, max_value=1e3, value=1.00000, step=0.00001, format="%.10f")
    ρ=st.number_input("Digite el valor de la densidad del material (kg/m^3):\n", min_value=1e-8, max_value=1e8, value=1.00000, step=0.00001, format="%.10f")
    z2=st.number_input("Digite el valor de z2 (m):\n", min_value=1e-8, max_value=1e3, value=1.00000, step=0.00001, format="%.10f")
    H=st.number_input("Digite el valor de la altura total (m):\n", min_value=1e-8, max_value=1e3, value=1.00000, step=0.00001, format="%.10f")

    v=μ/ρ #viscosidad
    hf=H
    ε=ks/d
    A=np.pi*(d**2)/4

    Vi=(-2*np.sqrt(2*9.81*d*hf/l))*np.log10((ks/(3.7*d))+((2.51*v*np.sqrt(l))/(d*np.sqrt(2*9.81*d*hf))))
    hfi=H-z2-km*(Vi**2)/(2*9.81)
    
    def i(hf):
        Vi1=(-2*np.sqrt(2*9.81*d*hf/l))*np.log10((ks/(3.7*d))+((2.51*v*np.sqrt(l))/(d*np.sqrt(2*9.81*d*hf))))
        hf1=H-z2-km*(Vi1**2)/(2*9.81)
        return (hf1,Vi1)

    DE=abs(hf-hfi)
    while E<DE:
        temp1=hfi
        iteracion=i(temp1)    
        hfi=iteracion[0]
        Q=iteracion[1]*A
        DE=abs(hf-hfi)
    Cdl=Q
    st.write("El valor del caudal es:",Cdl)

dominios=st.sidebar.radio("Proyecto 1 - Hidraulica",("Perdidas","Caudal","Diametro","Potencia",),key=1) 
if dominios=="Perdidas":
    Perdidas()

elif dominios=="Caudal":
    Caudal()
    
elif dominios=="Diametro":
    Diametro()

elif dominios=="Potencia":
    Potencia()

