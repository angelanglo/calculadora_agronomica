import math
import streamlit as st

st.set_page_config(
    page_title="Calculadora Agronómica SENA", page_icon="🌱", layout="centered"
)

st.title("🌱 Calculadora Agronómica SENA")
st.write(
    "Herramienta integral de cálculo para densidad de población y sistemas de siembra."
)

# Menú lateral para elegir el cultivo o sistema de siembra
cultivo = st.sidebar.selectbox(
    "Selecciona el Cultivo / Sistema",
    ["Tomate", "Papa", "Plátano (Triangular)", "Quincunce (Frutales)"],
)

if cultivo == "Tomate":
    st.header("🍅 Densidad Poblacional: Tomate")

    tipo_entrada = st.radio(
        "¿Cómo conoces las medidas de tu terreno?",
        ["Largo y Ancho directo", "Área Total y uno de los lados"],
    )

    if tipo_entrada == "Área Total y uno de los lados":
        area_total = st.number_input(
            "Área total del terreno (m²)", min_value=1.0, value=22000.0
        )
        lado_conocido = st.number_input(
            "Valor de uno de los lados (en metros)", min_value=1.0, value=220.0
        )
        lado_calculado = area_total / lado_conocido
        st.info(
            f"💡 El otro lado calculado es de: **{lado_calculado:.2f} metros**"
        )

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
        "Unidad de medida para distancias", ["Centímetros (cm)", "Metros (m)"]
    )

    d_surcos_input = st.number_input(
        "Distancia entre surcos (D/S)", min_value=0.1, value=96.0
    )
    d_plantas_input = st.number_input(
        "Distancia entre plantas en el surco (D/P)", min_value=0.1, value=40.0
    )

    if unidad_medida == "Centímetros (cm)":
        distancia_entre_surcos = d_surcos_input / 100.0
        distancia_entre_plantas = d_plantas_input / 100.0
    else:
        distancia_entre_surcos = d_surcos_input
        distancia_entre_plantas = d_plantas_input

    if st.button("Calcular Tomate"):
        numero_de_surcos = area_ancho / distancia_entre_surcos
        plantas_por_surco = area_largo / distancia_entre_plantas
        surcos_completos = math.floor(numero_de_surcos)
        plantas_totales = surcos_completos * plantas_por_surco

        st.success("¡Cálculo realizado con éxito!")
        st.write(f"- **Área total:** {area_total:,.2f} m²")
        st.write(
            f"- **Número de surcos:** {area_ancho} ÷ {distancia_entre_surcos} = **{surcos_completos} surcos**"
        )
        st.write(
            f"- **Plantas por surco:** {area_largo} ÷ {distancia_entre_plantas} = **{int(plantas_por_surco)}**"
        )
        st.write(
            f"- **Plantas totales:** {int(plantas_totales):,} plantas de tomate"
        )

elif cultivo == "Papa":
    st.header("🥔 Densidad Poblacional: Papa")
    area_largo = st.number_input(
        "Largo del terreno (metros)", min_value=1.0, value=50.0
    )
    area_ancho = st.number_input(
        "Ancho del terreno (metros)", min_value=1.0, value=20.0
    )

    d_surcos = st.number_input(
        "Distancia entre surcos (metros)", min_value=0.1, value=0.9
    )
    d_plantas = st.number_input(
        "Distancia entre plantas (metros)", min_value=0.01, value=0.3
    )

    if st.button("Calcular Papa"):
        area_total = area_largo * area_ancho
        surcos = area_ancho / d_surcos
        plantas_surco = area_largo / d_plantas
        total_papas = math.floor(surcos) * plantas_surco

        st.success("¡Cálculo realizado!")
        st.write(f"- **Área total:** {area_total:.2f} m²")
        st.write(f"- **Número de surcos:** {math.floor(surcos)}")
        st.write(f"- **Plantas por surco:** {int(plantas_surco)}")
        st.write(
            f"- **Población total estimada:** {int(total_papas):,} plantas de papa"
        )

elif cultivo == "Plátano (Triangular)":
    st.header("🍌 Sistema de Siembra: Plátano en Triangular")
    st.write(
        "En el arreglo triangular (tres bolillo), la distancia entre surcos se ajusta geométricamente."
    )

    area_largo = st.number_input(
        "Largo del lote (metros)", min_value=1.0, value=100.0
    )
    area_ancho = st.number_input(
        "Ancho del lote (metros)", min_value=1.0, value=50.0
    )
    distancia = st.number_input(
        "Distancia entre plantas (metros)", min_value=0.1, value=3.0
    )

    if st.button("Calcular Triangular"):
        area_total = area_largo * area_ancho
        # Fórmula aproximada para triangular: Área / (0.866 * d * d) o similar basada en triángulo equilátero
        # Área de un triángulo equilátero = (sqrt(3)/4) * d^2 ≈ 0.433 * d^2 por planta, o densidad = 2 / (sqrt(3) * d^2) * Area
        factor_triangular = (math.sqrt(3) / 2) * (distancia**2)
        plantas_totales = area_total / factor_triangular

        st.success("¡Cálculo realizado!")
        st.write(f"- **Área total:** {area_total:,.2f} m²")
        st.write(
            f"- **Plantas totales (Triangular):** {int(plantas_totales):,} plantas"
        )

elif cultivo == "Quincunce (Frutales)":
    st.header("🍊 Sistema de Siembra: Quincunce (Frutales)")
    st.write(
        "Marco real con un árbol adicional (relleno) en el centro de cada rectángulo."
    )

    area_largo = st.number_input(
        "Largo del terreno (metros)", min_value=1.0, value=100.0
    )
    area_ancho = st.number_input(
        "Ancho del terreno (metros)", min_value=1.0, value=100.0
    )
    distancia_a = st.number_input(
        "Distancia entre plantas (Lado A en metros)", min_value=0.1, value=6.0
    )
    distancia_b = st.number_input(
        "Distancia entre surcos (Lado B en metros)", min_value=0.1, value=6.0
    )

    if st.button("Calcular Quincunce"):
        # Plantas en marco real
        col_marcoreal = area_largo / distancia_a
        fil_marcoreal = area_ancho / distancia_b
        plantas_marcoreal = math.ceil(col_marcoreal) * math.ceil(fil_marcoreal)

        # Plantas centrales (quincunce) = (Columnas - 1) * (Filas - 1)
        centrales = (math.ceil(col_marcoreal) - 1) * (
            math.ceil(fil_marcoreal) - 1
        )
        total_quincunce = plantas_marcoreal + centrales

        st.success("¡Cálculo realizado!")
        st.write(f"- **Árboles en marco real:** {plantas_marcoreal}")
        st.write(f"- **Árboles de relleno (centrales):** {centrales}")
        st.write(
            f"- **Población total en Quincunce:** {int(total_quincunce):,} árboles"
        )

st.write("---")
st.caption("Desarrollado para prácticas del SENA 🚜")
