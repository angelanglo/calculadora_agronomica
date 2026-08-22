import streamlit as st
import math

st.set_page_config(page_title="Calculadora Agrícola SENA", page_icon="🌱")
st.title("🌱 Calculadora de Densidad y Costos Agrícolas")

# CREACIÓN DE LAS PESTAÑAS (¡Esto era lo que faltaba!)
tab1, tab2, tab3, tab4 = st.tabs(["Tomate", "Papa", "Plátano (Triangular)", "Quincunce"])

def calcular_largo(area, ancho):
    return area / ancho if ancho > 0 else 0.0

# --- PESTAÑA 1: TOMATE (Inteligente con unidades) ---
with tab1:
    st.header("🍅 Cálculo para Tomate")
    area_t = st.number_input("Área Total (m²)", value=22000.0, key="t_area")
    ancho_t_fijo = st.number_input("Ancho fijo (m)", value=50.0, key="t_ancho_fijo")
    largo_t_calc = calcular_largo(area_t, ancho_t_fijo)
    st.info(f"Largo calculado: {largo_t_calc:,.2f} m")
    
    unidad_ds = st.radio("Unidad para Distancia entre surcos:", ["Metros (m)", "Centímetros (cm)"], key="u_ds")
    ds_t = st.number_input("Valor surcos:", value=96.0, key="t_ds")
    
    unidad_dp = st.radio("Unidad para Distancia entre plantas:", ["Metros (m)", "Centímetros (cm)"], key="u_dp")
    dp_t = st.number_input("Valor plantas:", value=40.0, key="t_dp")
    
    if st.button("Calcular Tomate"):
        ds_final = ds_t / 100 if unidad_ds == "Centímetros (cm)" else ds_t
        dp_final = dp_t / 100 if unidad_dp == "Centímetros (cm)" else dp_t
        
        surcos = int(ancho_t_fijo / ds_final)
        plantas_s = int(largo_t_calc / dp_final)
        st.success(f"N° de surcos: {surcos} | Plantas Totales: {surcos * plantas_s:,}")

# --- PESTAÑA 2: PAPA (Inteligente con unidades) ---
with tab2:
    st.header("🥔 Cálculo para Papa")
    area_p = st.number_input("Área Total (m²)", value=500.0, key="p_area")
    ancho_p_fijo = st.number_input("Ancho fijo (m)", value=50.0, key="p_ancho_fijo")
    largo_p_calc = calcular_largo(area_p, ancho_p_fijo)
    st.info(f"Largo calculado: {largo_p_calc:,.2f} m")
    
    unidad_ds_p = st.radio("Unidad surcos:", ["Metros (m)", "Centímetros (cm)"], key="u_ds_p")
    ds_p = st.number_input("Valor surcos:", value=0.85, key="p_ds")
    
    unidad_dp_p = st.radio("Unidad plantas:", ["Metros (m)", "Centímetros (cm)"], key="u_dp_p")
    dp_p = st.number_input("Valor plantas:", value=5.0, key="p_dp")
    
    peso_p = st.number_input("Peso por papa (g)", value=32.0, key="p_peso")
    costo_p = st.number_input("Costo por kg ($)", value=120.0, key="p_costo")
    
    if st.button("Calcular Papa"):
        ds_p_final = ds_p / 100 if unidad_ds_p == "Centímetros (cm)" else ds_p
        dp_p_final = dp_p / 100 if unidad_dp_p == "Centímetros (cm)" else dp_p
        
        surcos = int(ancho_p_fijo / ds_p_final)
        plantas_s = int(largo_p_calc / dp_p_final)
        total_p = surcos * plantas_s
        st.metric("Plantas Totales", f"{total_p:,}")
        st.metric("Cantidad de Papa", f"{(total_p * peso_p)/1000:,.2f} kg")
        st.metric("Costo Total", f"${((total_p * peso_p)/1000) * costo_p:,.2f}")

# --- PESTAÑA 3: PLÁTANO ---
with tab3:
    st.header("🍌 Cálculo para Plátano (Triangular)")
    area_has = st.number_input("Área en Has", value=28.7, key="pl_area")
    dist_pl = st.number_input("Distancia (m)", value=2.5, key="pl_dist")
    
    if st.button("Calcular Plátano"):
        superficie_m2 = area_has * 10000
        dist_cuadrado = dist_pl ** 2
        paso_division = superficie_m2 / dist_cuadrado
        plantas_totales = paso_division * 1.154
        
        st.markdown("### 📋 Resultados del Procedimiento")
        st.metric("1. Superficie (m²)", f"{superficie_m2:,.0f}")
        st.metric("2. Distancia al cuadrado (d²)", f"{dist_cuadrado:,.2f}")
        st.info(f"🔹 **Cálculo intermedio (S / d²):** {paso_division:,.3f}")
        st.info(f"🔹 **Aplicando constante:** {paso_division:,.3f} × 1,154")
        st.metric("3. Plantas Totales (Aprox)", f"{round(plantas_totales):,}")
        
        st.markdown("### 🔄 Tabla de Conversión")
        st.info("• 1 Hectárea (Has) equivale a: **10.000 m²**")
        st.info(f"• Conversión automática: {area_has} Has * 10.000 = **{superficie_m2:,.0f} m²**")

# --- PESTAÑA 4: QUINCUNCE ---
with tab4:
    st.header("🌳 Cálculo para Quincunce")
    area_q = st.number_input("Área en Has", value=20.0, key="q_area")
    dist_q = st.number_input("Distancia (m)", value=5.5, key="q_dist")
    
    if st.button("Cálculo de Quincuncio"):
        columnas = math.floor(100 / dist_q)
        filas_lucuma = columnas
        plantas_lucuma_ha = columnas * filas_lucuma
        plantas_totales_lucuma = plantas_lucuma_ha * area_q
        
        filas_aguacate = columnas - 1
        plantas_aguacate_ha = filas_aguacate * filas_aguacate
        plantas_totales_aguacate = plantas_aguacate_ha * area_q
        
        total_general = plantas_totales_lucuma + plantas_totales_aguacate
        
        st.markdown("### 📋 Procedimiento Detallado (Frutales)")
        st.metric("1. Columnas (100 / Distancia)", f"{columnas}")
        st.metric("2. Filas Lúcuma", f"{filas_lucuma}")
        st.metric("3. Plantas Lúcuma / Ha", f"{plantas_lucuma_ha}")
        st.metric("4. Plantas Totales Lúcuma", f"{plantas_totales_lucuma:,.0f}")
        
        st.divider()
        
        st.metric("5. Columnas Aguacate", f"{columnas}")
        st.metric("6. Filas Aguacate (Filas - 1)", f"{filas_aguacate}")
        st.metric("7. Plantas Aguacate / Ha", f"{plantas_aguacate_ha}")
        st.metric("8. Plantas Totales Aguacate", f"{plantas_totales_aguacate:,.0f}")
        
        st.markdown("---")
        st.success(f"### 9. TOTAL GENERAL: {total_general:,.0f} plantas")