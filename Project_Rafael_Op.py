import streamlit as st
import numpy as np

def validate_input(label, min_value=1e-8, max_value=1e8, value=1.00000, step=0.00001, format="%.10f"):
    return st.number_input(f"Digite el valor de {label} (m):\n", min_value=min_value, max_value=max_value, value=value, step=step, format=format)

def calculate_friction_factor(Q, L, D, ks, u, fi):
    A = np.pi * (D**2) / 4
    V = Q / A
    Re = (V * D) / u

    def f(fi):
        return 1 / (-2 * np.log10((ks / (3.7 * D) + 2.51 / (Re * np.sqrt(fi)))) )**2

    fi1 = f(fi)
    DE = float('inf')

    # Iteratively calculate friction factor until convergence or maximum iterations
    for i in range(1000):
        if DE < E:
            break
        temp = fi1
        fi = temp
        fi1 = f(temp)
        DE = abs(fi - fi1)

    return fi1

def calculate_friction_losses(Q, L, D, ks, u, fi):
    Hf = (fi * L * (Q / ((np.pi * D**2) / 4))**2) / (2 * D * 9.81)
    return Hf

def calculate_flow_rate(l, d, ks, u, E, km, rho, z2, H):
    v = u / rho
    hf = H
    epsilon = ks / d
    A = np.pi * (d**2) / 4

    # Iteratively solve for velocity until convergence or maximum iterations
    for i in range(1000):
        Vi = (-2 * np.sqrt(2 * 9.81 * d * hf / l))