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

# Menú lateral para elegir el sistema de siembra
sistema = st.sidebar.selectbox(
    "Selecciona el Sistema de Siembra",
    [
        "Densidad por Surcos",
        "Sistema Triangular",
        "Sistema Quincunce (Asocio)",
    ],
)

if sistema == "Densidad por Surcos":
    st.header("📏 Densidad Poblacional por Surcos")
    
    # Nombre personalizado para este ejercicio
    nombre_cultivo = st.text_input(
        "📝 Nombre del Cultivo", value="Papa", key="surcos_nombre"
    )

    tipo_entrada = st.radio(
        "¿Cómo conoces las medidas de tu terreno?",
        ["Largo y Ancho directo", "Área Total y uno de los lados"],
        key="surcos_tipo",
    )

    if tipo_entrada == "Área Total y uno de los lados":
        area_total = st.number_input(
            "Área total del terreno (m²)",
            min_value=1.0,
            value=125000.0,
            key="surcos_area",
        )
        lado_conocido = st.number_input(
            "Valor de uno de los lados (en metros)",
            min_value=1.0,
            value=250.0,
            key="surcos_lado",
        )
        lado_calculado = area_total / lado_conocido
        st.info(
            f"💡 El otro lado calculado es de: **{lado_calculado:.2f} metros**"
        )

        cual_es = st.selectbox(
            "El valor que ingresaste arriba corresponde a:",
            ["Ancho", "Largo"],
            key="surcos_cual",
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
            value=500.0,
            key="surcos_largo",
        )
        area_ancho = st.number_input(
            "Ancho del terreno (metros)",
            min_value=1.0,
            value=250.0,
            key="surcos_ancho",
        )
        area_total = area_largo * area_ancho

    st.write("---")
    st.subheader("Distancias y Datos Adicionales")
    unidad_medida = st.radio(
        "Unidad de medida para distancias",
        ["Centímetros (cm)", "Metros (m)"],
        key="surcos_unidad",
    )

    d_surcos_input = st.number_input(
        "Distancia entre surcos (D/S)",
        min_value=0.1,
        value=80.0,
        key="surcos_ds",
    )
    d_plantas_input = st.number_input(
        "Distancia entre plantas en el surco (D/P)",
        min_value=0.1,
        value=50.0,
        key="surcos_dp",
    )

    peso_unidad_g = st.number_input(
        "Peso por unidad cosechada (gramos) [Opcional para costos]",
        min_value=0.0,
        value=32.0,
        key="surcos_peso",
    )
    costo_kg = st.number_input(
        "Costo por kg de cosecha ($) [Opcional para costos]",
        min_value=0.0,
        value=120.0,
        key="surcos_costo",
    )

    if unidad_medida == "Centímetros (cm)":
        distancia_entre_surcos = d_surcos_input / 100.0
        distancia_entre_plantas = d_plantas_input / 100.0
    else:
        distancia_entre_surcos = d_surcos_input
        distancia_entre_plantas = d_plantas_input

    if st.button(f"Calcular {nombre_cultivo}"):
        surcos = area_ancho / distancia_entre_surcos
        surcos_completos = math.floor(surcos)

        plantas_surco = area_largo / distancia_entre_plantas
        total_plantas = surcos_completos * plantas_surco

        st.success("¡Cálculo realizado con éxito!")
        st.write(f"- **Área total:** {area_total:,.2f} m²")
        st.write(
            f"- **1. Número de surcos:** {area_ancho} ÷ {distancia_entre_surcos} = {surcos:.2f} $\\rightarrow$ **{surcos_completos} surcos completos**"
        )
        st.write(
            f"- **2. Plantas por surco:** {area_largo} ÷ {distancia_entre_plantas} = **{int(plantas_surco)} plantas**"
        )
        st.write(
            f"- **3. Plantas totales:** {surcos_completos} × {int(plantas_surco)} = **{int(total_plantas):,} plantas de {nombre_cultivo.lower()}**"
        )

        if peso_unidad_g > 0 and costo_kg > 0:
            peso_kg_total_unidad = peso_unidad_g / 1000.0
            total_kg = total_plantas * peso_kg_total_unidad
            costo_total = total_kg * costo_kg
            st.write(
                f"- **4. Cantidad total (kg):** {int(total_plantas):,} × {peso_kg_total_unidad} kg = **{total_kg:,.3f} kg**"
            )
            st.markdown(
                f"- **5. Costo total:** {total_kg:,.3f} kg × ${costo_kg:,.1f} = **${costo_total:,.2f}**"
            )

elif sistema == "Sistema Triangular":
    st.header("🔺 Sistema de Siembra Triangular")
    
    # Nombre personalizado para el sistema triangular
    nombre_cultivo_tri = st.text_input(
        "📝 Nombre del Cultivo (Ej: Palma de Coco, Plátano)", 
        value="Plátano", 
        key="tri_nombre"
    )

    unidad_area = st.radio(
        "¿En qué unidad deseas ingresar la superficie del terreno?",
        ["Hectáreas (Has)", "Metros Cuadrados (m²)"],
        key="tri_u_area",
    )

    if unidad_area == "Hectáreas (Has)":
        superficie_input = st.number_input(
            "Superficie en Hectáreas (Has)",
            min_value=0.01,
            value=28.7,
            key="tri_has",
        )
        superficie_m2 = superficie_input * 10000.0
    else:
        superficie_m2 = st.number_input(
            "Superficie en Metros Cuadrados (m²)",
            min_value=1.0,
            value=287000.0,
            key="tri_m2",
        )

    distancia_tri = st.number_input(
        "Distancia de siembra (d en metros)",
        min_value=0.1,
        value=2.5,
        key="tri_d",
    )

    if st.button(f"Calcular {nombre_cultivo_tri} Triangular"):
        d_cuadrado = distancia_tri**2
        plantas_totales = (superficie_m2 / d_cuadrado) * 1.154

        st.success("¡Cálculo realizado con éxito!")
        if unidad_area == "Hectáreas (Has)":
            st.write(
                f"- **Conversión de Área:** {superficie_input} Has × 10,000 = **{superficie_m2:,.0f} m²**"
            )
        st.write(f"- **Superficie total (S):** {superficie_m2:,.0f} m²")
        st.write(
            f"- **Cálculo ($d^2$):** ({distancia_tri})² = {d_cuadrado:.2f}"
        )
        st.write(
            f"- **Fórmula Triangular (con constante 1.154):** ({superficie_m2:,.0f} ÷ {d_cuadrado}) × 1.154"
        )
        st.write(
            f"- **Densidad Poblacional Total:** **{round(plantas_totales):,} plantas de {nombre_cultivo_tri.lower()}**"
        )

elif sistema == "Sistema Quincunce (Asocio)":
    st.header("🍊 Sistema Quincunce en Asocio")
    
    # Nombres personalizados para ambos cultivos del asocio
    cultivo_principal = st.text_input(
        "📝 Cultivo Principal (Ej: Cacao, Lúcuma)",
        value="Cacao",
        key="quin_princ",
    )
    cultivo_relleno = st.text_input(
        "📝 Cultivo de Relleno (Ej: Plátano, Aguacate)",
        value="Plátano",
        key="quin_rell",
    )

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
        col_calc = 100.0 / distancia_q
        fil_calc = 100.0 / distancia_q

        # Cultivo Principal
        cols_princ = math.floor(col_calc)
        filas_princ = math.floor(fil_calc)
        plantas_princ_ha = cols_princ * filas_princ
        total_princ = plantas_princ_ha * area_has

        # Cultivo de Relleno (Quincunce - Relleno restando 1 en filas)
        cols_relleno = cols_princ
        filas_relleno = filas_princ - 1
        plantas_relleno_ha = filas_relleno * filas_relleno
        total_relleno = plantas_relleno_ha * area_has

        total_general = total_princ + total_relleno

        st.success("¡Cálculo realizado con éxito!")

        st.subheader(f"🌲 {cultivo_principal.upper()} (Cultivo Principal)")
        st.write(
            f"- **1. Columnas:** 100 m ÷ {distancia_q} m = **{cols_princ}**"
        )
        st.write(
            f"- **2. Filas:** 100 m ÷ {distancia_q} m = **{filas_princ}**"
        )
        st.write(
            f"- **3. Plantas / Ha:** {cols_princ} × {filas_princ} = **{plantas_princ_ha} plantas**"
        )
        st.write(
            f"- **4. Plantas totales ({area_has} Has):** {plantas_princ_ha} × {area_has} = **{int(total_princ):,} plantas de {cultivo_principal.lower()}**"
        )

        st.subheader(f"🥑 {cultivo_relleno.upper()} (Cultivo en Quincunce)")
        st.write(
            f"- **1. Columnas:** 100 m ÷ {distancia_q} m = **{cols_relleno}**"
        )
        st.write(
            f"- **2. Filas:** ({filas_princ} - 1) = **{filas_relleno}**"
        )
        st.write(
            f"- **3. Plantas / Ha:** {filas_relleno} × {filas_relleno} = **{plantas_relleno_ha} plantas**"
        )
        st.write(
            f"- **4. Plantas totales ({area_has} Has):** {plantas_relleno_ha} × {area_has} = **{int(total_relleno):,} plantas de {cultivo_relleno.lower()}**"
        )

        st.write("---")
        st.markdown(f"### 📊 RESUMEN TOTAL GENERAL")
        st.write(f"- **{cultivo_principal}:** {int(total_princ):,} plantas")
        st.write(f"- **{cultivo_relleno}:** {int(total_relleno):,} plantas")
        st.markdown(
            f"### **TOTAL GENERAL = {int(total_general):,} plantas**"
        )

st.write("---")
st.caption("Desarrollado con Python y Streamlit por Angelo Gonzalo Piedrahita Leon 🚀")
