import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

st.title("📈 Graphical Calculator")

st.write("Enter a mathematical function in terms of **x** to generate its graph.")
st.write("Examples: `sin(x)`, `cos(x)`, `x**2`, `log(x)`, `exp(x)`, `sqrt(x)`")

# Input for function
func = st.text_input("Function f(x):", value="sin(x)")

# Range inputs
x_min = st.number_input("X-axis minimum:", value=-10.0)
x_max = st.number_input("X-axis maximum:", value=10.0)

# Allowed math functions
allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
allowed["np"] = np

# Generate graph
if st.button("Plot"):
    try:
        x = np.linspace(x_min, x_max, 500)

        # Safe evaluation
        y = eval(func, {"__builtins__": {}}, {**allowed, "x": x})

        # Plotting
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title(f"f(x) = {func}")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.grid(True)

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")
