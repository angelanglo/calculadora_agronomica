import math
import streamlit as st

st.set_page_config(
    page_title="Calculadora Agronómica", page_icon="🌱", layout="centered"
)

st.title("🌱 Calculadora Agronómica Personal")
st.write(
    "Herramienta integral de cálculo para densidad de población y sistemas de siembra."
)
st.caption("🚀 Creado por: Angelo Gonzalo Piedrahita Leon")

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
        key="tomate_tipo",
    )

    if tipo_entrada == "Área Total y uno de los lados":
        area_total = st.number_input(
            "Área total del terreno (m²)",
            min_value=1.0,
            value=22000.0,
            key="tomate_area",
        )
        lado_conocido = st.number_input(
            "Valor de uno de los lados (en metros)",
            min_value=1.0,
            value=220.0,
            key="tomate_lado",
        )
        lado_calculado = area_total / lado_conocido
        st.info(
            f"💡 El otro lado calculado es de: **{lado_calculado:.2f} metros**"
        )

        cual_es = st.selectbox(
            "El valor que ingresaste arriba corresponde a:",
            ["Ancho", "Largo"],
            key="tomate_cual",
        )
        if cual_es == "Ancho":
            area_ancho = lado_conocido
            area_largo = lado_calculado
        else:
            area_largo = lado_conocido
            area_ancho = lado_calculado
    else:
        area_largo = st.number_input(
            "Largo del terreno (metros)",
            min_value=1.0,
            value=100.0,
            key="tomate_largo",
        )
        area_ancho = st.number_input(
            "Ancho del terreno (metros)",
            min_value=1.0,
            value=220.0,
            key="tomate_ancho",
        )
        area_total = area_largo * area_ancho

    st.write("---")
    st.subheader("Distancias de Siembra")
    unidad_medida = st.radio(
        "Unidad de medida para distancias",
        ["Centímetros (cm)", "Metros (m)"],
        key="tomate_unidad",
    )

    d_surcos_input = st.number_input(
        "Distancia entre surcos (D/S)",
        min_value=0.1,
        value=96.0,
        key="tomate_ds",
    )
    d_plantas_input = st.number_input(
        "Distancia entre plantas en el surco (D/P)",
        min_value=0.1,
        value=40.0,
        key="tomate_dp",
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

    tipo_entrada_papa = st.radio(
        "¿Cómo conoces las medidas de tu terreno?",
        ["Largo y Ancho directo", "Área Total y uno de los lados"],
        key="papa_tipo",
    )

    if tipo_entrada_papa == "Área Total y uno de los lados":
        area_total_p = st.number_input(
            "Área total del terreno (m²)",
            min_value=1.0,
            value=1000.0,
            key="papa_area",
        )
        lado_conocido_p = st.number_input(
            "Valor de uno de los lados (en metros)",
            min_value=1.0,
            value=50.0,
            key="papa_lado",
        )
        lado_calculado_p = area_total_p / lado_conocido_p
        st.info(
            f"💡 El otro lado calculado es de: **{lado_calculado_p:.2f} metros**"
        )

        cual_es_p = st.selectbox(
            "El valor que ingresaste arriba corresponde a:",
            ["Ancho", "Largo"],
            key="papa_cual",
        )
        if cual_es_p == "Ancho":
            area_ancho_p = lado_conocido_p
            area_largo_p = lado_calculado_p
        else:
            area_largo_p = lado_conocido_p
            area_ancho_p = lado_calculado_p
    else:
        area_largo_p = st.number_input(
            "Largo del terreno (metros)",
            min_value=1.0,
            value=50.0,
            key="papa_largo",
        )
        area_ancho_p = st.number_input(
            "Ancho del terreno (metros)",
            min_value=1.0,
            value=20.0,
            key="papa_ancho",
        )
        area_total_p = area_largo_p * area_ancho_p

    st.write("---")
    st.subheader("Distancias de Siembra")
    unidad_medida_p = st.radio(
        "Unidad de medida para distancias",
        ["Centímetros (cm)", "Metros (m)"],
        key="papa_unidad",
    )

    d_surcos_input_p = st.number_input(
        "Distancia entre surcos (D/S)",
        min_value=0.1,
        value=90.0,
        key="papa_ds",
    )
    d_plantas_input_p = st.number_input(
        "Distancia entre plantas en el surco (D/P)",
        min_value=0.1,
        value=30.0,
        key="papa_dp",
    )

    if unidad_medida_p == "Centímetros (cm)":
        distancia_entre_surcos_p = d_surcos_input_p / 100.0
        distancia_entre_plantas_p = d_plantas_input_p / 100.0
    else:
        distancia_entre_surcos_p = d_surcos_input_p
        distancia_entre_plantas_p = d_plantas_input_p

    if st.button("Calcular Papa"):
        surcos_p = area_ancho_p / distancia_entre_surcos_p
        plantas_surco_p = area_largo_p / distancia_entre_plantas_p
        surcos_completos_p = math.floor(surcos_p)
        total_papas = surcos_completos_p * plantas_surco_p

        st.success("¡Cálculo realizado con éxito!")
        st.write(f"- **Área total:** {area_total_p:,.2f} m²")
        st.write(
            f"- **Número de surcos:** {area_ancho_p} ÷ {distancia_entre_surcos_p} = **{surcos_completos_p} surcos**"
        )
        st.write(
            f"- **Plantas por surco:** {area_largo_p} ÷ {distancia_entre_plantas_p} = **{int(plantas_surco_p)}**"
        )
        st.write(
            f"- **Población total estimada:** {int(total_papas):,} plantas de papa"
        )

elif cultivo == "Plátano (Triangular)":
    st.header("🍌 Sistema de Siembra: Plátano en Triangular")

    unidad_area = st.radio(
        "¿En qué unidad deseas ingresar la superficie del terreno?",
        ["Hectáreas (Has)", "Metros Cuadrados (m²)"],
        key="plat_u_area",
    )

    if unidad_area == "Hectáreas (Has)":
        superficie_input = st.number_input(
            "Superficie en Hectáreas (Has)",
            min_value=0.01,
            value=28.7,
            key="plat_has",
        )
        superficie_m2 = superficie_input * 10000.0
    else:
        superficie_m2 = st.number_input(
            "Superficie en Metros Cuadrados (m²)",
            min_value=1.0,
            value=287000.0,
            key="plat_m2",
        )

    distancia_platano = st.number_input(
        "Distancia de siembra (d en metros)",
        min_value=0.1,
        value=2.5,
        key="plat_d",
    )

    if st.button("Calcular Plátano Triangular"):
        d_cuadrado = distancia_platano**2
        plantas_totales = (superficie_m2 / d_cuadrado) * 1.154

        st.success("¡Cálculo realizado con éxito!")
        if unidad_area == "Hectáreas (Has)":
            st.write(
                f"- **Conversión de Área:** {superficie_input} Has × 10,000 = **{superficie_m2:,.0f} m²**"
            )
        st.write(f"- **Superficie total (S):** {superficie_m2:,.0f} m²")
        st.write(
            f"- **Cálculo ($d^2$):** ({distancia_platano})² = {d_cuadrado:.2f}"
        )
        st.write(
            f"- **Fórmula Triangular (con constante 1.154):** ({superficie_m2:,.0f} ÷ {d_cuadrado}) × 1.154"
        )
        st.write(
            f"- **Densidad Poblacional Total:** **{round(plantas_totales):,} plantas de plátano**"
        )

elif cultivo == "Quincunce (Frutales)":
    st.header("🍊 Sistema Quincunce en Asocio (Lúcuma y Aguacate)")

    area_has = st.number_input(
        "Área total del terreno (Hectáreas)",
        min_value=0.1,
        value=20.0,
        key="quin_has",
    )
    distancia_q = st.number_input(
        "Distancia de siembra (metros)", min_value=0.1, value=5.5, key="quin_dq"
    )

    if st.button("Calcular Quincunce en Asocio"):
        # Cálculos base por hectárea (tomando 100m por lado)
        col_calc = 100.0 / distancia_q
        fil_calc = 100.0 / distancia_q

        # Lúcuma (Cultivo Principal)
        cols_lucuma = math.floor(col_calc)
        filas_lucuma = math.floor(fil_calc)
        plantas_lucuma_ha = cols_lucuma * filas_lucuma
        total_lucuma = plantas_lucuma_ha * area_has

        # Aguacate (Cultivo en Quincunce - Relleno restando 1 en filas)
        cols_aguacate = cols_lucuma
        filas_aguacate = filas_lucuma - 1
        plantas_aguacate_ha = cols_aguacate * filas_aguacate
        total_aguacate = plantas_aguacate_ha * area_has

        total_general = total_lucuma + total_aguacate

        st.success("¡Cálculo realizado con éxito!")

        st.subheader("🌲 LÚCUMA (Cultivo Principal)")
        st.write(
            f"- **1. Columnas:** 100 m ÷ {distancia_q} m = **{cols_lucuma}**"
        )
        st.write(
            f"- **2. Filas:** 100 m ÷ {distancia_q} m = **{filas_lucuma}**"
        )
        st.write(
            f"- **3. Plantas / Ha:** {cols_lucuma} × {filas_lucuma} = **{plantas_lucuma_ha} plantas**"
        )
        st.write(
            f"- **4. Plantas totales ({area_has} Has):** {plantas_lucuma_ha} × {area_has} = **{int(total_lucuma):,} plantas de lúcuma**"
        )

        st.subheader("🥑 AGUACATE (Cultivo en Quincunce)")
        st.write(
            f"- **1. Columnas:** 100 m ÷ {distancia_q} m = **{cols_aguacate}**"
        )
        st.write(
            f"- **2. Filas:** ({filas_lucuma} - 1) = **{filas_aguacate}**"
        )
        st.write(
            f"- **3. Plantas / Ha:** {cols_aguacate} × {filas_aguacate} = **{plantas_aguacate_ha} plantas**"
        )
        st.write(
            f"- **4. Plantas totales ({area_has} Has):** {plantas_aguacate_ha} × {area_has} = **{int(total_aguacate):,} plantas de aguacate**"
        )

        st.write("---")
        st.markdown(f"### 📊 RESUMEN TOTAL GENERAL")
        st.write(f"- **Lúcuma:** {int(total_lucuma):,} plantas")
        st.write(f"- **Aguacate:** {int(total_aguacate):,} plantas")
        st.markdown(
            f"### **TOTAL GENERAL = {int(total_general):,} plantas**"
        )

st.write("---")
st.caption("Desarrollado con Python y Streamlit por Angelo Gonzalo Piedrahita Leon 🚜")
