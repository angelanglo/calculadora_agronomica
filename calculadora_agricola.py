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
        # CORRECCIÓN: Usar filas_aguacate x filas_aguacate como indica tu guía (17 x 17 = 289)
        plantas_aguacate_ha = filas_aguacate * filas_aguacate
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
            f"- **3. Plantas / Ha:** {filas_aguacate} × {filas_aguacate} = **{plantas_aguacate_ha} plantas**"
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
