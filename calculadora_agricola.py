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

    # 1. Opción de ingresar por Área Total o por Dimensiones Directas
    tipo_entrada = st.radio(
        "¿Cómo conoces las medidas de tu terreno?",
        ["Largo y Ancho directo", "Área Total y uno de los lados"],
    )

    if tipo_entrada == "Área Total y uno de los lados":
        area_total = st.number_input(
            "Área total del terreno (m²)", min_value=1.0, value=22000.0
        )
        lado_conocido = st.number_input(
            "Valor de uno de los lados (Ancho o Largo en metros)",
            min_value=1.0,
            value=220.0,
        )

        # Despejamos el otro lado automáticamente (Área / Lado)
        lado_calculado = area_total / lado_conocido
        st.info(
            f"💡 Según tu área de {area_total} m², el otro lado calculado es de: **{lado_calculado:.2f} metros**"
        )

        # Preguntamos si el lado conocido es el Ancho o el Largo
        cual_es = st.selectbox(
            "El valor que ingresaste arriba corresponde a:", ["Ancho", "Largo"]
        )
        if cual_es == "Ancho":
            area_ancho = lado_conocido
            area_largo = lado_calculado
        else:
            area_largo = lado_conocido
            area_ancho = lado_calculado
    else:
        area_largo = st.number_input(
            "Largo del terreno (metros)", min_value=1.0, value=100.0
        )
        area_ancho = st.number_input(
            "Ancho del terreno (metros)", min_value=1.0, value=220.0
        )
        area_total = area_largo * area_ancho

    st.write("---")
    st.subheader("Distancias de Siembra")
    unidad_medida = st.radio(
        "¿En qué unidad deseas ingresar las distancias?",
        ["Centímetros (cm)", "Metros (m)"],
    )

    d_surcos_input = st.number_input(
        "Distancia entre surcos (D/S)", min_value=0.1, value=96.0
    )
    d_plantas_input = st.number_input(
        "Distancia entre plantas en el surco (D/P)", min_value=0.1, value=40.0
    )

    # Conversión automática de cm a metros si aplica
    if unidad_medida == "Centímetros (cm)":
        distancia_entre_surcos = d_surcos_input / 100.0
        distancia_entre_plantas = d_plantas_input / 100.0
    else:
        distancia_entre_surcos = d_surcos_input
        distancia_entre_plantas = d_plantas_input

    st.write("---")
    if st.button("Calcular Densidad Poblacional"):
        # Fórmulas idénticas a tu guía del SENA
        numero_de_surcos = area_ancho / distancia_entre_surcos
        plantas_por_surco = area_largo / distancia_entre_plantas

        # Usamos surcos completos para el cálculo final o exactos según prefieras
        surcos_completos = math.floor(numero_de_surcos)
        plantas_totales = surcos_completos * plantas_por_surco

        st.success("¡Cálculo realizado con éxito!")

        st.write(f"- **Área total del terreno:** {area_total:,.2f} m²")
        st.write(
            f"- **1. Número de surcos:** {area_ancho} m ÷ {distancia_entre_surcos} m = **{numero_de_surcos:.2f}** $\\rightarrow$ **{surcos_completos} surcos** (completos)"
        )
        st.write(
            f"- **2. Plantas por surco:** {area_largo} m ÷ {distancia_entre_plantas} m = **{int(plantas_por_surco)} plantas por surco**"
        )
        st.write(
            f"- **3. Plantas totales (Densidad Poblacional):** {surcos_completos} × {int(plantas_por_surco)} = **{int(plantas_totales):,} plantas de tomate**"
        )

elif cultivo == "Maíz":
    st.header("🌽 Cálculo para Cultivo de Maíz")
    st.write("Próximamente más configuraciones específicas.")

else:
    st.header("🌾 Configuración General")
    st.write("Selecciona un cultivo válido en el menú lateral.")

st.write("---")
st.caption("Desarrollado para prácticas del SENA 🚜")
