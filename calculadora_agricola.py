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

    # Opción de unidades para las distancias entre plantas/surcos
    unidad_medida = st.radio(
        "¿En qué unidad deseas ingresar las distancias de plantación?",
        ["Metros (m)", "Centímetros (cm)"],
    )

    st.write("---")
    st.subheader("Dimensiones del Terreno")
    area_largo = st.number_input(
        "Largo del terreno (metros)", min_value=1.0, value=50.0
    )
    area_ancho = st.number_input(
        "Ancho del terreno (metros)", min_value=1.0, value=20.0
    )

    st.subheader("Distancias de Siembra")
    d_surcos_input = st.number_input(
        "Distancia entre surcos", min_value=0.1, value=1.5
    )
    d_plantas_input = st.number_input(
        "Distancia entre plantas en el surco", min_value=0.1, value=40.0
    )

    # Conversión automática si el usuario eligió centímetros
    if unidad_medida == "Centímetros (cm)":
        distancia_entre_surcos = d_surcos_input / 100.0
        distancia_entre_plantas = d_plantas_input / 100.0
    else:
        distancia_entre_surcos = d_surcos_input
        distancia_entre_plantas = d_plantas_input

    # Sección de cálculo inverso / estimación de dimensiones si se requiere
    st.write("---")
    st.subheader("Herramienta de Dimensiones (Opcional)")
    modo_calculo = st.checkbox(
        "¿Deseas calcular el área estimando a partir de número de surcos deseados?"
    )

    if modo_calculo:
        surcos_deseados = st.number_input(
            "Número de surcos que deseas sembrar", min_value=1, value=10
        )
        ancho_calculado = surcos_deseados * distancia_entre_surcos
        st.info(
            f"💡 Para tener {surcos_deseados} surcos, necesitarías un ancho de terreno de aproximadamente **{ancho_calculado:.2f} metros**."
        )

    if st.button("Calcular Tomate"):
        # Cálculos principales
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
