import math
import streamlit as st

st.set_page_config(
    page_title="Calculadora Agronómica", page_icon="🌱", layout="centered"
)

st.title("🌱 Calculadora Agronómica SENA")
st.write(
    "Herramienta de cálculo para densidad de población y distribución de cultivos."
)

# Menú lateral para elegir el cultivo
cultivo = st.sidebar.selectbox(
    "Selecciona el cultivo", ["Tomate", "Maíz", "Frijol", "Otro"]
)

if cultivo == "Tomate":
    st.header("🍅 Cálculo para Cultivo de Tomate")

    # Entradas de datos
    area_largo = st.number_input(
        "Largo del terreno (metros)", min_value=1.0, value=50.0
    )
    area_ancho = st.number_input(
        "Ancho del terreno (metros)", min_value=1.0, value=20.0
    )

    st.write("---")
    distancia_entre_surcos = st.number_input(
        "Distancia entre surcos (metros)", min_value=0.1, value=1.5
    )
    distancia_entre_plantas = st.number_input(
        "Distancia entre plantas en el surco (metros)", min_value=0.1, value=0.4
    )

    if st.button("Calcular Tomate"):
        # Cálculos
        area_total = area_largo * area_ancho
        numero_de_surcos = area_ancho / distancia_entre_surcos
        plantas_por_surco = area_largo / distancia_entre_plantas
        plantas_totales = numero_de_surcos * plantas_por_surco

        st.success("¡Cálculo realizado con éxito!")

        # Mostrar resultados detallados
        st.write(f"- **Área total del terreno:** {area_total:.2f} m²")
        st.write(f"- **Número de surcos:** {math.ceil(numero_de_surcos)}")
        st.write(f"- **Plantas por surco:** {int(plantas_por_surco)} plantas")
        st.write(
            f"- **Plantas totales estimadas:** {int(plantas_totales)} plantas"
        )

elif cultivo == "Maíz":
    st.header("🌽 Cálculo para Cultivo de Maíz")
    st.write(
        "Próximamente más configuraciones específicas para maíz y otros cultivos."
    )

else:
    st.header("🌾 Configuración General")
    st.write("Selecciona un cultivo válido en el menú lateral.")

st.write("---")
st.caption("Desarrollado para prácticas del SENA 🚜")
