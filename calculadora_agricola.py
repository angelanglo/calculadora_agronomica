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
    lado_conocido = st.radio(
        "¿Qué medida conoces del terreno?",
        ("Largo (metros)", "Ancho (metros)"),
    )
    if lado_conocido == "Largo (metros)":
      largo = st.number_input(
          "Introduce el Largo (metros)", min_value=1.0, value=100.0, step=1.0
      )
      ancho = area_total / largo
      st.info(
          f"📏 Ancho calculado automáticamente: **{ancho:,.2f} metros** para"
          f" completar el área."
      )
    else:
      ancho = st.number_input(
          "Introduce el Ancho (metros)", min_value=1.0, value=220.0, step=1.0
      )
      largo = area_total / ancho
      st.info(
          f"📏 Largo calculado automáticamente: **{largo:,.2f} metros** para"
          f" completar el área."
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

  if unidad_dist == "Centímetros (cm)":
    dist_surcos = dist_surcos_input / 100.0
    dist_plantas = dist_plantas_input / 100.0
  else:
    dist_surcos = dist_surcos_input
    dist_plantas = dist_plantas_input

  if st.button(f"Calcular {nombre_cultivo}"):
    if dist_surcos > 0 and dist_plantas > 0:
      num_surcos = ancho / dist_surcos
      num_surcos_completos = int(num_surcos)
      plantas_por_surco = largo / dist_plantas
      plantas_por_surco_completas = int(plantas_por_surco)
      plantas_totales = num_surcos_completos * plantas_por_surco_completas
      densidad_ha = 10000 / (dist_surcos * dist_plantas)

      st.success("¡Cálculo realizado con éxito!")
      st.markdown(
          f"""
            * **Área total:** {area_total:,.2f} m²
            * **1. N° de surcos:** {ancho:.2f} m $\div$ {dist_surcos} m = {num_surcos:.2f} $\rightarrow$ **{num_surcos_completos}** surcos completos
            * **2. Plantas por surco:** {largo:.2f} m $\div$ {dist_plantas} m = {plantas_por_surco:.2f} $\rightarrow$ **{plantas_por_surco_completas}** plantas por surco
            * **3. Plantas totales:** {num_surcos_completos} $\times$ {plantas_por_surco_completas} = **{plantas_totales:,.0f}** plantas de {nombre_cultivo}
            
            ### **RESPUESTA:** Densidad poblacional = {plantas_totales:,.0f} plantas de {nombre_cultivo} (Estimada aprox. {densidad_ha:,.2f} plantas/ha)
            """
      )
    else:
      st.error("⚠️ Las distancias deben ser mayores a cero.")


# --- EJERCICIO 2 ---
elif opcion == "2. Densidad Poblacional (Área Total)":
  st.markdown("## 📐 2. Densidad Poblacional por Área Total")
  st.markdown(
      "Calcula la densidad de plantas por hectárea conociendo el área total del"
      " terreno y el número de plantas establecidas."
  )

  area_total_m2 = st.number_input(
      "Área total del terreno (m²)", min_value=1.0, value=5000.0, step=100.0
  )
  num_plantas = st.number_input(
      "Número total de plantas sembradas", min_value=1.0, value=12500.0, step=50.0
  )

  if st.button("Calcular Densidad por Área Total"):
    if area_total_m2 > 0:
      hectareas = area_total_m2 / 10000
      densidad = num_plantas / hectareas
      st.success("¡Cálculo realizado con éxito!")
      st.markdown(
          f"""
            * **Área total en hectáreas:** {area_total_m2:,.2f} m² $\div$ 10,000 = **{hectareas:,.4f} ha**
            * **Plantas sembradas:** {num_plantas:,.0f} plantas
            
            ### **RESPUESTA:** Densidad poblacional = **{densidad:,.2f}** plantas por hectárea
            """
      )
    else:
      st.error("⚠️ El área debe ser mayor a cero.")


# --- EJERCICIO 3 ---
elif opcion == "3. Conversión de Unidades de Superficie":
  st.markdown("## 🔄 3. Conversión de Unidades de Superficie")
  st.markdown(
      "Convierte rápidamente entre hectáreas (ha) y metros cuadrados (m²)."
  )

  tipo_conversion = st.radio(
      "Selecciona la dirección de la conversión:",
      ("Hectáreas a Metros Cuadrados (m²)", "Metros Cuadrados (m²) a Hectáreas"),
  )

  if tipo_conversion == "Hectáreas a Metros Cuadrados (m²)":
    val_ha = st.number_input(
        "Introduce las Hectáreas (ha)", min_value=0.0, value=1.0, step=0.1
    )
    if st.button("Convertir a m²"):
      resultado_m2 = val_ha * 10000
      st.success("¡Conversión realizada con éxito!")
      st.markdown(
          f"""
            * **Fórmula:** {val_ha} ha $\times$ 10,000
            
            ### **RESPUESTA:** Equivalente a **{resultado_m2:,.2f} m²**
            """
      )
  else:
    val_m2 = st.number_input(
        "Introduce los Metros Cuadrados (m²)",
        min_value=0.0,
        value=10000.0,
        step=500.0,
    )
    if st.button("Convertir a Hectáreas"):
      resultado_ha = val_m2 / 10000
      st.success("¡Conversión realizada con éxito!")
      st.markdown(
          f"""
            * **Fórmula:** {val_m2:,.2f} m² $\div$ 10,000
            
            ### **RESPUESTA:** Equivalente a **{resultado_ha:,.4f} ha**
            """
      )


# --- EJERCICIO 4 ---
elif opcion == "4. Requerimiento de Semillas / Insumos":
  st.markdown("## 📦 4. Requerimiento de Semillas y Plántulas")
  st.markdown(
      "Calcula el total exacto de semillas o plántulas a comprar considerando"
      " el porcentaje estimado de marras o pérdidas."
  )

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

  if st.button("Calcular Requerimiento Total"):
    plantas_netas = area_ha * densidad_ha
    total_con_perdida = plantas_netas * (1 + (porcentaje_perdida / 100))

    st.success("¡Cálculo realizado con éxito!")
    st.markdown(
        f"""
          * **Área a sembrar:** {area_ha:,.2f} ha
          * **Densidad por hectárea:** {densidad_ha:,.2f} plantas/ha
          * **Plantas netas requeridas:** {area_ha} $\times$ {densidad_ha} = **{plantas_netas:,.0f}** plantas
          * **Margen de pérdida estimado:** {porcentaje_perdida}%
          
          ### **RESPUESTA:** Total de semillas/plántulas a comprar = **{total_con_perdida:,.0f}** unidades
          """
    )
