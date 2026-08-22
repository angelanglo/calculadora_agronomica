import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Calculadora Agronómica SENA",
    page_icon="🌱",
    layout="centered",
)

# Título y autor
st.title("🌱 Calculadora Agronómica Personalizada")
st.markdown(
    "Herramienta integral de cálculo para densidad de población y sistemas de"
    " siembra."
)
st.markdown("*🚀 Creado por: Angelo Gonzalo Piedrahita Leon*")
st.write("---")

# Menú lateral para seleccionar el ejercicio
st.sidebar.title("Selecciona el Ejercicio")
opcion = st.sidebar.selectbox(
    "Elige una opción:",
    (
        "1. Densidad Poblacional (Surcos - Típico)",
        "2. Densidad Poblacional (Área Total)",
        "3. Conversión de Unidades de Superficie",
        "4. Requerimiento de Semillas / Insumos",
    ),
)


# --- EJERCICIO 1 ---
if opcion == "1. Densidad Poblacional (Surcos - Típico)":
  # Campo de texto para el cultivo
  nombre_cultivo = st.text_input("Nombre del Cultivo", value="Tomate")


  # Función para cambiar el emoji de manera dinámica según el cultivo
  def obtener_emoji_cultivo(nombre):
    nombre_minus = nombre.lower()
    if "papa" in nombre_minus:
      return "🥔"
    elif "maiz" in nombre_minus or "maíz" in nombre_minus:
      return "🌽"
    elif "frijol" in nombre_minus or "fríjol" in nombre_minus:
      return "🫘"
    elif "arroz" in nombre_minus:
      return "🌾"
    elif "tomate" in nombre_minus:
      return "🍅"
    elif "platano" in nombre_minus or "plátano" in nombre_minus:
      return "🍌"
    else:
      return "🌱"


  emoji_actual = obtener_emoji_cultivo(nombre_cultivo)

  st.markdown(f"## {emoji_actual} 1. Densidad Poblacional por Surcos")

  col1, col2 = st.columns(2)
  with col1:
    dist_surcos = st.number_input(
        "Distancia entre surcos (m)", min_value=0.01, value=1.0, step=0.05
    )
  with col2:
    dist_plantas = st.number_input(
        "Distancia entre plantas (m)", min_value=0.01, value=0.4, step=0.05
    )

  if st.button("Calcular Densidad"):
    if dist_surcos > 0 and dist_plantas > 0:
      area_por_planta = dist_surcos * dist_plantas
      densidad_ha = 10000 / area_por_planta
      st.success(f"🌾 **Cultivo:** {nombre_cultivo}")
      st.info(f"📊 **Densidad estimada:** {densidad_ha:,.2f} plantas/ha")
    else:
      st.error("⚠️ Las distancias deben ser mayores a cero.")


# --- EJERCICIO 2 ---
elif opcion == "2. Densidad Poblacional (Área Total)":
  st.markdown("## 📐 2. Densidad Poblacional por Área Total")

  area_total_m2 = st.number_input(
      "Área total del terreno (m²)", min_value=1.0, value=5000.0, step=100.0
  )
  num_plantas = st.number_input(
      "Número total de plantas sembradas", min_value=1.0, value=12500.0, step=50.0
  )

  if st.button("Calcular Densidad Total"):
    densidad = num_plantas / (area_total_m2 / 10000)
    st.info(
        f"📊 **Densidad poblacional estimada:** {densidad:,.2f} plantas por"
        " hectárea"
    )


# --- EJERCICIO 3 ---
elif opcion == "3. Conversión de Unidades de Superficie":
  st.markdown("## 🔄 3. Conversión de Unidades de Superficie")

  tipo_conversion = st.radio(
      "Selecciona la conversión:",
      ("Hectáreas a Metros Cuadrados (m²)", "Metros Cuadrados (m²) a Hectáreas"),
  )

  if tipo_conversion == "Hectáreas a Metros Cuadrados (m²)":
    val_ha = st.number_input(
        "Introduce las Hectáreas (ha)", min_value=0.0, value=1.0, step=0.1
    )
    if st.button("Convertir a m²"):
      resultado_m2 = val_ha * 10000
      st.success(f"✨ **{val_ha} ha** equivalen a **{resultado_m2:,.2f} m²**")
  else:
    val_m2 = st.number_input(
        "Introduce los Metros Cuadrados (m²)",
        min_value=0.0,
        value=10000.0,
        step=500.0,
    )
    if st.button("Convertir a Hectáreas"):
      resultado_ha = val_m2 / 10000
      st.success(
          f"✨ **{val_m2:,.2f} m²** equivalen a **{resultado_ha:,.4f} ha**"
      )


# --- EJERCICIO 4 ---
elif opcion == "4. Requerimiento de Semillas / Insumos":
  st.markdown("## 📦 4. Requerimiento de Semillas y Plántulas")

  area_ha = st.number_input(
      "Área total a sembrar (en hectáreas)",
      min_value=0.01,
      value=1.0,
      step=0.1,
  )
  densidad_ha = st.number_input(
      "Densidad estimada (plantas por hectárea)",
      min_value=1.0,
      value=25000.0,
      step=500.0,
  )
  porcentaje_perdida = st.number_input(
      "Porcentaje estimado de marras / pérdida (%)",
      min_value=0.0,
      value=5.0,
      step=0.5,
  )

  if st.button("Calcular Insumos"):
    plantas_netas = area_ha * densidad_ha
    total_con_perdida = plantas_netas * (1 + (porcentaje_perdida / 100))

    st.success(f"🌱 **Plantas netas requeridas:** {plantas_netas:,.0f}")
    st.warning(
        f"📦 **Total con margen de pérdida ({porcentaje_perdida}%):**"
        f" **{total_con_perdida:,.0f}** semillas o plántulas a comprar."
    )
