import math
import streamlit as st

st.set_page_config(
    page_title="Calculadora Agronómica SENA",
    page_icon="🌱",
    layout="centered",
)

st.title("🌱 Calculadora Agronómica Personalizada")
st.write(
    "Herramienta integral de cálculo para densidad de población y sistemas de"
    " siembra."
)
st.caption("🚀 Creado por: Angelo Gonzalo Piedrahita Leon")


def obtener_emoji(nombre_cultivo):
  n = nombre_cultivo.lower()
  if "tomate" in n:
    return "🍅"
  elif "papa" in n:
    return "🥔"
  elif "platano" in n or "plátano" in n:
    return "🍌"
  elif "aguacate" in n:
    return "🥑"
  elif "piña" in n:
    return "🍍"
  elif "maiz" in n or "maíz" in n:
    return "🌽"
  elif "frijol" in n or "fríjol" in n:
    return "🫘"
  elif "arroz" in n:
    return "🌾"
  elif "cafe" in n or "café" in n:
    return "☕"
  elif "citrico" in n or "naranja" in n or "limon" in n or "limón" in n:
    return "🍊"
  else:
    return "🌱"


ejercicio = st.sidebar.selectbox(
    "Selecciona el Ejercicio",
    [
        "1. Densidad Poblacional (Surcos - Tipo 1)",
        "2. Densidad Poblacional (Surcos con Costos - Tipo 2)",
        "3. Densidad Poblacional (Sistema Triangular)",
        "4. Sistema Quincunce (Asocio de Cultivos)",
    ],
)

if ejercicio == "1. Densidad Poblacional (Surcos - Tipo 1)":
  cultivo_1 = st.text_input("Nombre del Cultivo", value="Tomate")
  emoji_1 = obtener_emoji(cultivo_1)

  st.header(f"{emoji_1} 1. Densidad Poblacional por Surcos")

  tipo_entrada_t = st.radio(
      "¿Cómo conoces las medidas de tu terreno?",
      ["Largo y Ancho directo", "Área Total y uno de los lados"],
      key="t_tipo",
  )

  if tipo_entrada_t == "Área Total y uno de los lados":
    area_total_t = st.number_input(
        "Área total del terreno (m²)", min_value=1.0, value=22000.0, key="t_area"
    )
    lado_conocido_t = st.number_input(
        "Valor de uno de los lados (en metros)",
        min_value=1.0,
        value=220.0,
        key="t_lado",
    )
    lado_calculado_t = area_total_t / lado_conocido_t
    st.info(f"💡 El otro lado calculado es de: **{lado_calculado_t:.2f} metros**")

    cual_es_t = st.selectbox(
        "El valor que ingresaste arriba corresponde a:",
        ["Ancho", "Largo"],
        key="t_cual",
    )
    if cual_es_t == "Ancho":
      area_ancho_t = lado_conocido_t
      area_largo_t = lado_calculado_t
    else:
      area_largo_t = lado_conocido_t
      area_ancho_t = lado_calculado_t
  else:
    area_largo_t = st.number_input(
        "Largo del terreno (metros)", min_value=1.0, value=100.0, key="t_largo"
    )
    area_ancho_t = st.number_input(
        "Ancho del terreno (metros)", min_value=1.0, value=220.0, key="t_ancho"
    )
    area_total_t = area_largo_t * area_ancho_t

  st.write("---")
  st.subheader("Distancias de Siembra")

  unidad_medida_t = st.radio(
      "Unidad de medida para las distancias de siembra",
      ["Centímetros (cm)", "Metros (m)"],
      key="t_unidad",
  )

  d_surcos_t = st.number_input(
      "Distancia entre surcos (D/S)", min_value=0.1, value=96.0, key="t_ds"
  )
  d_plantas_t = st.number_input(
      "Distancia entre plantas en el surco (D/P)",
      min_value=0.1,
      value=40.0,
      key="t_dp",
  )

  if unidad_medida_t == "Centímetros (cm)":
    ds_m = d_surcos_t / 100.0
    dp_m = d_plantas_t / 100.0
  else:
    ds_m = d_surcos_t
    dp_m = d_plantas_t

  if st.button(f"Calcular {cultivo_1}"):
    num_surcos = area_ancho_t / ds_m
    surcos_completos = math.floor(num_surcos)
    plantas_surco = area_largo_t / dp_m
    plantas_totales = surcos_completos * plantas_surco

    st.success("¡Cálculo realizado con éxito!")
    st.write(f"- **Área total:** {area_total_t:,.2f} m²")
    st.write(
        f"- **1. N° de surcos:** {area_ancho_t} m ÷ {ds_m} m ="
        f" {num_surcos:.2f} $\\rightarrow$ **{surcos_completos} surcos"
        " completos**"
    )
    st.write(
        f"- **2. Plantas por surco:** {area_largo_t} m ÷ {dp_m} m ="
        f" **{int(plantas_surco)} plantas por surco**"
    )
    st.write(
        f"- **3. Plantas totales:** {surcos_completos} ×"
        f" {int(plantas_surco)} = **{int(plantas_totales):,} plantas de"
        f" {cultivo_1}**"
    )
    st.markdown(
        f"### **RESPUESTA: Densidad poblacional = {int(plantas_totales):,}"
        f" plantas de {cultivo_1}**"
    )

elif ejercicio == "2. Densidad Poblacional (Surcos con Costos - Tipo 2)":
  cultivo_2 = st.text_input("Nombre del Cultivo", value="Papa")
  emoji_2 = obtener_emoji(cultivo_2)

  st.header(f"{emoji_2} 2. Densidad Poblacional con Costos y Pesos")

  tipo_entrada_p = st.radio(
      "¿Cómo conoces las medidas de tu terreno?",
      ["Largo y Ancho directo", "Área Total y uno de los lados"],
      key="p_tipo",
  )

  if tipo_entrada_p == "Área Total y uno de los lados":
    area_total_p = st.number_input(
        "Área total del terreno (m²)", min_value=1.0, value=125000.0, key="p_area"
    )
    lado_conocido_p = st.number_input(
        "Valor de uno de los lados (en metros)",
        min_value=1.0,
        value=250.0,
        key="p_lado",
    )
    lado_calculado_p = area_total_p / lado_conocido_p
    st.info(f"💡 El otro lado calculado es de: **{lado_calculado_p:.2f} metros**")

    cual_es_p = st.selectbox(
        "El valor que ingresaste arriba corresponde a:",
        ["Ancho", "Largo"],
        key="p_cual",
    )
    if cual_es_p == "Ancho":
      area_ancho_p = lado_conocido_p
      area_largo_p = lado_calculado_p
    else:
      area_largo_p = lado_conocido_p
      area_ancho_p = lado_calculado_p
  else:
    area_largo_p = st.number_input(
        "Largo del terreno (metros)", min_value=1.0, value=500.0, key="p_largo"
    )
    area_ancho_p = st.number_input(
        "Ancho del terreno (metros)", min_value=1.0, value=250.0, key="p_ancho"
    )
    area_total_p = area_largo_p * area_ancho_p

  st.write("---")
  st.subheader("Distancias, Pesos y Costos")

  unidad_medida_p = st.radio(
      "Unidad de medida para las distancias de siembra",
      ["Metros (m)", "Centímetros (cm)"],
      key="p_unidad",
  )

  d_surcos_p_in = st.number_input(
      "Distancia entre surcos (D/S)", min_value=0.01, value=0.80, key="p_ds"
  )
  d_plantas_p_in = st.number_input(
      "Distancia entre plantas en el surco (D/P)",
      min_value=0.01,
      value=0.50,
      key="p_dp",
  )

  if unidad_medida_p == "Centímetros (cm)":
    d_surcos_p = d_surcos_p_in / 100.0
    d_plantas_p = d_plantas_p_in / 100.0
  else:
    d_surcos_p = d_surcos_p_in
    d_plantas_p = d_plantas_p_in

  peso_g = st.number_input(
      f"Peso por unidad de {cultivo_2} (gramos)",
      min_value=0.1,
      value=32.0,
      key="p_peso",
  )
  costo_kg = st.number_input(
      "Costo por kg ($)", min_value=0.1, value=120.0, key="p_costo"
  )

  if st.button(f"Calcular {cultivo_2}"):
    num_surcos_p = area_ancho_p / d_surcos_p
    surcos_completos_p = math.floor(num_surcos_p)
    plantas_surco_p = area_largo_p / d_plantas_p
    total_unidades = surcos_completos_p * plantas_surco_p

    kg_total = (peso_g / 1000.0) * total_unidades
    costo_total = kg_total * costo_kg

    st.success("¡Cálculo realizado con éxito!")
    st.write(f"- **Área total:** {area_total_p:,.2f} m²")
    st.write(
        f"- **1. N° de surcos:** {area_ancho_p} m ÷ {d_surcos_p} m ="
        f" {num_surcos_p:.2f} $\\rightarrow$ **{surcos_completos_p} surcos"
        " completos**"
    )
    st.write(
        f"- **2. Plantas por surco:** {area_largo_p} m ÷ {d_plantas_p} m ="
        f" **{int(plantas_surco_p)} plantas por surco**"
    )
    st.write(
        f"- **3. Plantas totales:** {surcos_completos_p} ×"
        f" {int(plantas_surco_p)} = **{int(total_unidades):,} plantas de"
        f" {cultivo_2}**"
    )
    st.write(
        f"- **4. Cantidad total (kg):** {total_unidades:,.0f} ×"
        f" {(peso_g/1000)} kg = **{kg_total:,.3f} kg**"
    )
    st.markdown(
        f"- **5. Costo total:** {kg_total:,.3f} kg × ${costo_kg:,.1f} ="
        f" **${costo_total:,.3f}**"
    )
    st.markdown(f"### **RESPUESTAS:**")
    st.write(
        f"Densidad = {int(total_unidades):,} plantas | Cantidad necesaria ="
        f" {kg_total:,.3f} kg | Costo total = ${costo_total:,.3f}"
    )

elif ejercicio == "3. Densidad Poblacional (Sistema Triangular)":
  cultivo_3 = st.text_input("Nombre del Cultivo", value="Plátano")
  emoji_3 = obtener_emoji(cultivo_3)

  st.header(f"{emoji_3} 3. Densidad Poblacional (Sistema Triangular)")

  area_has = st.number_input(
      "Área del terreno (Hectáreas)", min_value=0.01, value=28.7, key="pl_has"
  )
  distancia_pl = st.number_input(
      "Distancia de siembra (d en metros)", min_value=0.1, value=2.5, key="pl_d"
  )

  if st.button(f"Calcular {cultivo_3} Triangular"):
    area_m2 = area_has * 10000.0
    d_cuadrado = distancia_pl**2
    plantas_totales = (area_m2 / d_cuadrado) * 1.154

    st.success("¡Cálculo realizado con éxito!")
    st.write(
        f"- **Conversión de Área:** {area_has} Has × 10.000 ="
        f" **{area_m2:,.0f} m²**"
    )
    st.info(
        f"📍 **Referencia de Superficie:** Los `{area_m2:,.0f} m²` calculados"
        f" representan la **superficie total del terreno** disponible para el"
        f" establecimiento del cultivo de {cultivo_3}."
    )
    st.write(f"- **Cálculo ($d^2$):** ({distancia_pl})² = {d_cuadrado:.2f}")
    st.write(f"- **Fórmula:** ({area_m2:,.0f} ÷ {d_cuadrado}) × 1,154")
    st.markdown(
        f"### **RESPUESTA: Densidad poblacional = {round(plantas_totales):,}"
        f" plantas de {cultivo_3}**"
    )

elif ejercicio == "4. Sistema Quincunce (Asocio de Cultivos)":
  st.header("🍊 4. Sistema Quincunce (Asocio de Dos Cultivos)")

  cultivo_principal = st.text_input(
      "Nombre Cultivo Principal (Temporal / Relleno)", value="Lúcuma"
  )
  cultivo_secundario = st.text_input(
      "Nombre Cultivo Secundario (Permanente / Quincunce)", value="Aguacate"
  )

  area_q_has = st.number_input(
      "Área total del terreno (Hectáreas)", min_value=0.1, value=20.0, key="q_has"
  )
  distancia_q = st.number_input(
      "Distancia de siembra (metros)", min_value=0.1, value=5.5, key="q_d"
  )

  if st.button("Calcular Sistema Quincunce"):
    col = 100.0 / distancia_q
    fil = 100.0 / distancia_q

    col_p = math.floor(col)
    fil_p = math.floor(fil)
    princ_ha = col_p * fil_p
    total_princ = princ_ha * area_q_has

    fil_s = fil_p - 1
    sec_ha = fil_s * fil_s
    total_sec = sec_ha * area_q_has

    total_general = total_princ + total_sec

    st.success("¡Cálculo realizado con éxito!")
    st.subheader(f"🌲 {cultivo_principal.upper()}:")
    st.write(f"- Columnas: 100 m ÷ {distancia_q} m = {col_p}")
    st.write(f"- Filas: 100 m ÷ {distancia_q} m = {fil_p}")
    st.write(f"- Plantas / Ha: {col_p} × {fil_p} = {princ_ha}")
    st.write(
        f"- **Plantas totales:** {princ_ha} × {area_q_has} Has ="
        f" **{int(total_princ):,} plantas**"
    )

    st.subheader(f"🥑 {cultivo_secundario.upper()} (QUINCUNCE):")
    st.write(f"- Columnas: {col_p}")
    st.write(f"- Filas: ({fil_p} - 1) = {fil_s}")
    st.write(f"- Plantas / Ha: {fil_s} × {fil_s} = {sec_ha}")
    st.write(
        f"- **Plantas totales:** {sec_ha} × {area_q_has} Has ="
        f" **{int(total_sec):,} plantas**"
    )

    st.write("---")
    st.markdown("### 📊 RESUMEN TOTAL GENERAL")
    st.write(f"- **{cultivo_principal}:** {int(total_princ):,} plantas")
    st.write(f"- **{cultivo_secundario}:** {int(total_sec):,} plantas")
    st.markdown(f"### **TOTAL GENERAL = {int(total_general):,} plantas**")

st.write("---")
st.caption(
    "Desarrollado con Python y Streamlit por Angelo Gonzalo Piedrahita Leon 🚀"
)
