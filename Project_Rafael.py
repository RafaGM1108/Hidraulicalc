import streamlit as st
import numpy as np

csfont = {'fontname':'Times New Roman'}

#--------------------Pilot Part-------------------#

def Perdidas():
    Q=st.number_input("Digite el valor del caudal (m^3/s):\n",step=0.0000001)
    L=st.number_input("Digite el valor de la longitud (m):\n")
    D=st.number_input("Digite el valor del diametro (m):\n")
    ks=st.number_input("Digite el valor de la rugosidad del material (m):\n")
    u=st.number_input("Digite el valor de la viscosidad (m^2/s):\n")
    E=st.number_input(input("Digite el valor del Error:\n"))
    A=np.pi*(D**2)/4
    V=Q/A
    Re=(V*D)/u
    fi=float(input("Digite el valor de fi:\n"))
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
    print(DE)
    Hf=(fi1*L*(V**2))/(2*D*9.81)
    st.write("El valor del coeficiente de fricción f es: ",fi1)
    st.write("El valor de la perdida de cabeza por friccion es:",Hf)
    
def Caudal():
    l=float(input("Digite el valor de la longitud (m):\n"))
    d=float(input("Digite el valor del diametro (m):\n"))
    ks=float(input("Digite el valor de la rugosidad del material (m):\n"))
    μ=float(input("Digite el valor de la viscosidad (pa*s):\n"))
    E=float(input("Digite el valor del Error:\n"))
    km=float(input("Digite el valor de las perdidas menores (m):\n"))
    ρ=float(input("Digite el valor de la densidad del material (kg/m^3):\n"))
    z2=float(input("Digite el valor de z2 (m):\n"))
    H=float(input("Digite el valor de la altura total (m):\n"))

    v=μ/ρ #viscosidad
    hf=H
    ε=ks/d

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
        DE=abs(hf-hfi)


dominios=st.sidebar.radio("Proyecto 1 - Hidraulica",("Perdidas","Caudal",),key=1) 
if dominios=="Perdidas":
    Perdidas()

elif dominios=="Caudal":
    Caudal()


