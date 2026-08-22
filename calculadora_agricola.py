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

  # Opciones avanzadas de terreno que tenías antes
  tipo_medida = st.radio(
      "¿Cómo conoces las medidas de tu terreno?",
      ("Largo y Ancho directo", "Área Total y uno de los lados"),
  )

  if tipo_medida == "Largo y Ancho directo":
    col1, col2 = st.columns(2)
    with col1:
      largo = st.number_input(
          "Largo del terreno (metros)", min_value=1.0, value=100.0, step=1.0
      )
    with col2:
      ancho = st.number_input(
          "Ancho del terreno (metros)", min_value=1.0, value=220.0, step=1.0
      )
    area_total = largo * ancho
  else:
    area_total = st.number_input(
        "Área Total del terreno (m²)", min_value=1.0, value=22000.0, step=100.0
    )

  st.markdown("### Distancias de Siembra")
  unidad_dist = st.radio(
      "Unidad de medida para las distancias de siembra",
      ("Centímetros (cm)", "Metros (m)"),
  )

  col3, col4 = st.columns(2)
  with col3:
    dist_surcos_input = st.number_input(
        "Distancia entre surcos (D/S)",
        min_value=1.0,
        value=96.0 if unidad_dist == "Centímetros (cm)" else 0.96,
        step=1.0 if unidad_dist == "Centímetros (cm)" else 0.05,
    )
  with col4:
    dist_plantas_input = st.number_input(
        "Distancia entre plantas en el surco (D/P)",
        min_value=1.0,
        value=40.0 if unidad_dist == "Centímetros (cm)" else 0.40,
        step=1.0 if unidad_dist == "Centímetros (cm)" else 0.05,
    )

  # Convertir a metros si el usuario eligió centímetros
  if unidad_dist == "Centímetros (cm)":
    dist_surcos = dist_surcos_input / 100.0
    dist_plantas = dist_plantas_input / 100.0
  else:
    dist_surcos = dist_surcos_input
    dist_plantas = dist_plantas_input

  if st.button(f"Calcular {nombre_cultivo}"):
    if dist_surcos > 0 and dist_plantas > 0:
      area_por_planta = dist_surcos * dist_plantas
      densidad_ha = 10000 / area_por_planta
      total_plantas_terreno = densidad_ha * (area_total / 10000)

      st.success(f"🌾 **Cultivo:** {nombre_cultivo}")
      st.info(f"📊 **Densidad estimada:** {densidad_ha:,.2f} plantas/ha")
      st.write(
          f"🌱 **Cantidad estimada para tu terreno ({area_total:,.2f} m²):**"
          f" **{total_plantas_terreno:,.0f}** plantas"
      )
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
