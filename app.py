import streamlit as st
st.markdown("""
<style>

.main {
    background-color: #FFFFFF;
}

h1 {
    color: #13362F;
}

h2, h3 {
    color: #2B5D54;
}

.stButton>button {
    background-color: #13362F;
    color: white;
    border-radius: 10px;
    border: none;
}

.stMetric {
    background-color: #F4F7F3;
    padding: 15px;
    border-radius: 10px;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

</style>
""", unsafe_allow_html=True)

import pandas as pd
import plotly.express as px
from io import BytesIO

st.set_page_config(
    page_title="EcoHincha World Cup",
    page_icon="⚽",
    layout="wide"
)

st.markdown("""
<h1 style='text-align:center;'>
🌎 ECOHINCHA WORLD CUP™
</h1>
""", unsafe_allow_html=True)
st.markdown("""
<h3 style='text-align:center;color:#2B5D54'>
EGS | Estudio de Gestión de Sistemas
</h3>
""", unsafe_allow_html=True)
st.markdown("""
<div style="
background-color:#13362F;
padding:20px;
border-radius:12px;
color:white;
text-align:center;
">

<h2>Herramienta de Evaluación Ambiental para Eventos Deportivos</h2>

<p>
Calcula la huella de carbono asociada a tu experiencia como hincha
durante la Copa Mundial y descubre tu EcoScore Mundial™.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
### Herramienta de Evaluación Ambiental para Eventos Deportivos

Esta plataforma permite evaluar el impacto ambiental asociado a la experiencia de visualización de un partido del Mundial.

Se analizarán:

- Movilidad
- Energía
- Alimentación y consumo
- Gestión de residuos
- Comportamiento ambiental

Al finalizar obtendrás:

- Huella de carbono estimada
- EcoScore Mundial
- Perfil Ambiental
- Recomendaciones para el próximo partido
""")

st.info("Comenzaremos con el módulo de movilidad.")
st.header("📍 DATOS DE LA MEDICIÓN")

nombre_usuario = st.text_input("Nombre o identificación")

ciudad = st.text_input("Ciudad")

provincia = st.text_input("Provincia / Estado")

pais = st.text_input("País")

st.subheader("⚽ Partido evaluado")

equipos_mundial = [
    "Seleccionar equipo",
    "Argentina",
    "Alemania",
    "Arabia Saudita",
    "Argelia",
    "Australia",
    "Austria",
    "Bélgica",
    "Bosnia y Herzegovina",
    "Brasil",
    "Canadá",
    "Cabo Verde",
    "Colombia",
    "Corea del Sur",
    "Costa de Marfil",
    "Croacia",
    "Curazao",
    "Ecuador",
    "Egipto",
    "Escocia",
    "España",
    "Estados Unidos",
    "Francia",
    "Ghana",
    "Haití",
    "Inglaterra",
    "Irak",
    "Irán",
    "Japón",
    "Jordania",
    "Marruecos",
    "México",
    "Noruega",
    "Nueva Zelanda",
    "Países Bajos",
    "Panamá",
    "Paraguay",
    "Portugal",
    "Qatar",
    "RD Congo",
    "República Checa",
    "Senegal",
    "Sudáfrica",
    "Suecia",
    "Suiza",
    "Túnez",
    "Turquía",
    "Uruguay",
    "Uzbekistán"
]

equipo_1 = st.selectbox(
    "Equipo 1",
    equipos_mundial
)

equipo_2 = st.selectbox(
    "Equipo 2",
    equipos_mundial
)

if (
    equipo_1 != "Seleccionar equipo"
    and equipo_2 != "Seleccionar equipo"
    and equipo_1 != equipo_2
):
    partido = f"{equipo_1} vs {equipo_2}"
else:
    partido = ""

st.header("🚗 MÓDULO 1 | MOVILIDAD DEL HINCHA")

lugar = st.selectbox(
    "¿Dónde viste el partido?",
    [
        "Mi casa",
        "Casa de familiares",
        "Casa de amigos",
        "Bar",
        "Fan Fest",
        "Estadio"
    ]
)

transporte = st.selectbox(
    "¿Cómo te transportaste?",
    [
        "Caminando",
        "Bicicleta",
        "Colectivo",
        "Moto",
        "Auto",
        "Taxi/Uber"
    ]
)

distancia = st.number_input(
    "¿Cuántos kilómetros recorriste?",
    min_value=0.0,
    value=0.0
)

if transporte in ["Caminando", "Bicicleta"]:
    personas = 1
    st.info("Movilidad no motorizada.")
else:
    personas = st.number_input(
        "¿Cuántas personas viajaban en el vehículo?",
        min_value=1,
        value=1
    )
factores_transporte = {
    "Caminando": 0.0,
    "Bicicleta": 0.0,
    "Colectivo": 0.060,
    "Moto": 0.103,
    "Auto": 0.192,
    "Taxi/Uber": 0.192
}

factor = factores_transporte[transporte]

emisiones_movilidad = (distancia * factor) / personas

st.subheader("Resultado preliminar de movilidad")

st.info(f"Huella de carbono por movilidad: {emisiones_movilidad:.2f} kg CO₂e")

if emisiones_movilidad == 0:
    st.success("Tu movilidad no generó emisiones directas de CO₂e.")
elif transporte in ["Auto", "Taxi/Uber"]:
    st.warning("La movilidad motorizada individual es una de las fuentes de mayor impacto del evento.")
elif transporte == "Colectivo":
    st.info("El transporte público reduce la huella por persona frente al uso de auto particular.")
else:
    st.info("Resultado calculado correctamente.")
    st.header("⚡ MÓDULO 2 | ENERGÍA UTILIZADA DURANTE EL PARTIDO")

dispositivo = st.selectbox(
    "¿Qué dispositivo usaron para ver el partido?",
    [
        "Televisor LED",
        "Smart TV grande",
        "Notebook",
        "Proyector",
        "Pantalla gigante"
    ]
)

minutos_tv = st.number_input(
    "¿Cuántos minutos utilizaste este dispositivo durante el partido? (90 minutos = partido completo)",
    min_value=0,
    value=0,
    step=5
)

horas_tv = minutos_tv / 60

uso_aire = st.checkbox("¿Usaron aire acondicionado?")
horas_aire = 0.0

if uso_aire:
    horas_aire = st.number_input(
        "¿Cuántas horas usaron aire acondicionado?",
        min_value=0.0,
        value=2.0,
        step=0.5
    )

uso_calefaccion = st.checkbox("¿Usaron calefacción eléctrica?")
horas_calefaccion = 0.0

if uso_calefaccion:
    horas_calefaccion = st.number_input(
        "¿Cuántas horas usaron calefacción?",
        min_value=0.0,
        value=2.0,
        step=0.5
    )

potencias_dispositivo = {
    "Televisor LED": 0.08,
    "Smart TV grande": 0.12,
    "Notebook": 0.06,
    "Proyector": 0.25,
    "Pantalla gigante": 1.50
}

factor_electricidad = 0.30

energia_dispositivo = potencias_dispositivo[dispositivo] * horas_tv
energia_aire = 1.50 * horas_aire
energia_calefaccion = 2.00 * horas_calefaccion

energia_total_kwh = energia_dispositivo + energia_aire + energia_calefaccion
emisiones_energia = energia_total_kwh * factor_electricidad

st.subheader("Resultado preliminar de energía")

st.info(f"Huella de carbono por energía: {emisiones_energia:.2f} kg CO₂e")

st.write(f"Consumo eléctrico estimado: {energia_total_kwh:.2f} kWh")
st.header("🍔 MÓDULO 3 | ALIMENTACIÓN Y CONSUMO")

tipo_comida = st.selectbox(
    "¿Qué consumieron principalmente durante el partido?",
    [
        "No consumimos comida",
        "Snacks",
        "Comida casera",
        "Delivery",
        "Asado",
        "Picada",
        "Otro"
    ]
)
detalle_comida = ""

if tipo_comida == "Otro":
    detalle_comida = st.text_input(
        "Especificá qué consumieron"
    )
if tipo_comida == "No consumimos comida":
    personas_comida = 0
    st.info("No se registró consumo de alimentos.")
else:
    personas_comida = st.number_input(
        "¿Cuántas personas consumieron comida?",
        min_value=1,
        value=1
    )

bebidas = st.selectbox(
    "¿Qué bebidas consumieron principalmente?",
    [
        "No consumimos bebidas",
        "Agua de red / botella reutilizable",
        "Gaseosas en botella plástica",
        "Latas",
        "Botellas de vidrio"
    ]
)

cantidad_bebidas = st.number_input(
    "Cantidad aproximada de bebidas/envases utilizados",
    min_value=0,
    value=0
)

factores_comida = {
    "No consumimos comida": 0.0,
    "Snacks": 0.60,
    "Comida casera": 1.20,
    "Delivery": 1.80,
    "Asado": 4.50,
    "Picada": 2.20,
    "Otro": 1.20
}

factores_bebidas = {
    "No consumimos bebidas": 0.0,
    "Agua de red / botella reutilizable": 0.02,
    "Gaseosas en botella plástica": 0.25,
    "Latas": 0.18,
    "Botellas de vidrio": 0.30
}

emisiones_comida = factores_comida[tipo_comida] * personas_comida
emisiones_bebidas = factores_bebidas[bebidas] * cantidad_bebidas

emisiones_alimentacion = emisiones_comida + emisiones_bebidas

st.subheader("Resultado preliminar de alimentación y consumo")

st.info(f"Huella de carbono por alimentación y consumo: {emisiones_alimentacion:.2f} kg CO₂e")

st.write(f"Emisiones por comida: {emisiones_comida:.2f} kg CO₂e")
st.write(f"Emisiones por bebidas/envases: {emisiones_bebidas:.2f} kg CO₂e")

if tipo_comida == "Asado":
    st.warning("El consumo de asado representa una fuente relevante de emisiones dentro del evento.")
elif tipo_comida == "Delivery":
    st.warning("El delivery puede aumentar el impacto por envases, traslado y residuos asociados.")
elif tipo_comida == "Comida casera":
    st.info("La comida casera tiende a permitir mayor control sobre residuos y desperdicio.")
st.header("♻️ MÓDULO 4 | GESTIÓN DE RESIDUOS")

plasticos = st.number_input(
    "Cantidad de envases plásticos generados",
    min_value=0,
    value=0
)

latas = st.number_input(
    "Cantidad de latas generadas",
    min_value=0,
    value=0
)

vidrio = st.number_input(
    "Cantidad de envases de vidrio",
    min_value=0,
    value=0
)

carton = st.number_input(
    "Cantidad de envases de cartón",
    min_value=0,
    value=0
)

organicos = st.number_input(
    "Cantidad estimada de residuos orgánicos",
    min_value=0,
    value=0
)

separacion = st.selectbox(
    "¿Separaste los residuos?",
    ["Seleccionar", "Sí", "No"]
)

reciclaje = st.selectbox(
    "¿Los materiales reciclables fueron enviados a reciclaje?",
    ["Seleccionar", "Sí", "No"]
)

compostaje = st.selectbox(
    "¿Los residuos orgánicos fueron compostados?",
    ["Seleccionar", "Sí", "No"]
)

factor_plastico = 0.08
factor_lata = 0.05
factor_vidrio = 0.04
factor_carton = 0.03
factor_organico = 0.06

emisiones_residuos = (
    plasticos * factor_plastico +
    latas * factor_lata +
    vidrio * factor_vidrio +
    carton * factor_carton +
    organicos * factor_organico
)

if separacion == "Sí":
    emisiones_residuos *= 0.90

if reciclaje == "Sí":
    emisiones_residuos *= 0.80

if compostaje == "Sí":
    emisiones_residuos *= 0.90

residuos_totales = plasticos + latas + vidrio + carton + organicos

st.subheader("Resultado preliminar de residuos")

st.info(f"Huella de carbono por energía: {emisiones_energia:.2f} kg CO₂e")

st.write(f"Residuos generados: {residuos_totales} unidades aproximadas")
st.header("🌎 RESULTADO FINAL | HUELLA AMBIENTAL DEL PARTIDO")

emisiones_totales = (
    emisiones_movilidad +
    emisiones_energia +
    emisiones_alimentacion +
    emisiones_residuos
)

personas_totales = max(personas_comida, personas)

emisiones_por_persona = emisiones_totales / personas_totales
# Equivalencias ambientales orientativas
km_auto_equivalente = emisiones_totales / 0.192 if emisiones_totales > 0 else 0
arboles_estimados = emisiones_totales / 22 if emisiones_totales > 0 else 0
kwh_equivalentes = emisiones_totales / 0.43 if emisiones_totales > 0 else 0

if emisiones_por_persona <= 2:
    categoria_ecohincha = "EcoHincha A+"
elif emisiones_por_persona <= 5:
    categoria_ecohincha = "EcoHincha A"
elif emisiones_por_persona <= 8:
    categoria_ecohincha = "EcoHincha B"
elif emisiones_por_persona <= 12:
    categoria_ecohincha = "EcoHincha C"
else:
    categoria_ecohincha = "EcoHincha D"
# EcoScore Mundial

eco_score = max(
    0,
    round(
        100 - (emisiones_por_persona * 8)
    )
)

st.info(f"Huella de carbono por energía: {emisiones_energia:.2f} kg CO₂e")

st.info(f"Huella de carbono por energía: {emisiones_energia:.2f} kg CO₂e")
st.markdown(f"""
<div style="
background-color:#D8E7B8;
padding:22px;
border-radius:14px;
color:#13362F;
margin-top:20px;
">
<h3>Interpretación del resultado</h3>
<p><b>EcoScore Mundial:</b> {eco_score}/100</p>
<p><b>Categoría EcoHincha:</b> {categoria_ecohincha}</p>
<p><b>Equivalencia en automóvil:</b> {km_auto_equivalente:.1f} km recorridos.</p>
<p><b>Compensación estimada:</b> {arboles_estimados:.2f} árboles durante un año.</p>
<p><b>Energía equivalente:</b> {kwh_equivalentes:.1f} kWh.</p>

</div>
""", unsafe_allow_html=True)
st.markdown(f"""
<div style="
background-color:#13362F;
padding:26px;
border-radius:18px;
color:white;
margin-top:22px;
text-align:center;
">

<h3 style="color:#D8E7B8;">EcoScore Mundial™</h3>

<h1 style="color:#D8E7B8;font-size:58px;">
{eco_score}/100
</h1>

<div style="
background-color:white;
border-radius:20px;
height:22px;
width:100%;
margin-top:10px;
">
<div style="
background-color:#D8E7B8;
height:22px;
border-radius:20px;
width:{eco_score}%;
">
</div>
</div>

<p style="font-size:20px;margin-top:18px;">
Nivel alcanzado: <b>{categoria_ecohincha}</b>
</p>

</div>
""", unsafe_allow_html=True)
st.subheader("📋 Desglose técnico de emisiones")

st.markdown(f"""
<div style="
background-color:#FFFFFF;
border:2px solid #2B5D54;
padding:22px;
border-radius:14px;
color:#13362F;
margin-top:20px;
">

<p><b>Movilidad:</b> {emisiones_movilidad:.2f} kg CO₂e</p>
<p><b>Energía:</b> {emisiones_energia:.2f} kg CO₂e</p>
<p><b>Alimentación y consumo:</b> {emisiones_alimentacion:.2f} kg CO₂e</p>
<p><b>Residuos:</b> {emisiones_residuos:.2f} kg CO₂e</p>

</div>
""", unsafe_allow_html=True)

categorias = {
    "Movilidad": emisiones_movilidad,
    "Energía": emisiones_energia,
    "Alimentación y consumo": emisiones_alimentacion,
    "Residuos": emisiones_residuos
}

categoria_principal = max(categorias, key=categorias.get)
valor_principal = categorias[categoria_principal]
df_emisiones = pd.DataFrame({
    "Categoría": [
        "Movilidad",
        "Energía",
        "Alimentación",
        "Residuos"
    ],
    "Emisiones": [
        emisiones_movilidad,
        emisiones_energia,
        emisiones_alimentacion,
        emisiones_residuos
    ]
})

fig = px.pie(
    df_emisiones,
    values="Emisiones",
    names="Categoría",
    title="Distribución de la Huella Ambiental",
    hole=0.45
)

fig.update_layout(
    paper_bgcolor="white",
    font_color="#13362F"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Principal fuente de emisión detectada")
st.warning(f"{categoria_principal}: {valor_principal:.2f} kg CO₂e")

st.subheader("Recomendaciones prioritarias para el próximo partido")

recomendaciones = []

recomendaciones = []

if transporte in ["Auto", "Moto", "Taxi/Uber"]:
    recomendaciones.append("Reducir el uso de vehículos individuales o compartir el viaje.")

if uso_aire:
    recomendaciones.append("Optimizar el uso del aire acondicionado para disminuir el consumo energético.")

if tipo_comida == "Asado":
    recomendaciones.append("Reducir el consumo de carne vacuna para disminuir la huella alimentaria.")

if tipo_comida == "Delivery":
    recomendaciones.append("Reducir pedidos con envases descartables y traslados asociados.")

if separacion == "No":
    recomendaciones.append("Implementar separación de residuos en origen.")

if reciclaje == "No":
    recomendaciones.append("Enviar materiales reciclables a sistemas de recuperación.")

if compostaje == "No":
    recomendaciones.append("Compostar residuos orgánicos para reducir residuos enviados a disposición final.")

if recomendaciones:
    st.subheader("Recomendaciones prioritarias para el próximo partido")
    for rec in recomendaciones:
        st.write(f"✅ {rec}")
st.subheader("Distribución de la huella por categoría")

datos_grafico = pd.DataFrame({
    "Categoría": [
        "Movilidad",
        "Energía",
        "Alimentación y consumo",
        "Residuos"
    ],
    "kg CO₂e": [
        emisiones_movilidad,
        emisiones_energia,
        emisiones_alimentacion,
        emisiones_residuos
    ]
})

fig = px.pie(
    datos_grafico,
    names="Categoría",
    values="kg CO₂e",
    title="Participación porcentual de cada fuente de emisión"
)

st.plotly_chart(fig, use_container_width=True)
st.subheader("Participación de cada categoría")

movilidad_pct = (emisiones_movilidad / emisiones_totales * 100) if emisiones_totales > 0 else 0
energia_pct = (emisiones_energia / emisiones_totales * 100) if emisiones_totales > 0 else 0
alimentacion_pct = (emisiones_alimentacion / emisiones_totales * 100) if emisiones_totales > 0 else 0
residuos_pct = (emisiones_residuos / emisiones_totales * 100) if emisiones_totales > 0 else 0

st.info(f"Movilidad: {movilidad_pct:.1f}%")
st.info(f"Energía: {energia_pct:.1f}%")
st.info(f"Alimentación: {alimentacion_pct:.1f}%")
st.info(f"Residuos: {residuos_pct:.1f}%")
st.subheader("📊 Comparación EcoHincha")

recomendaciones = []

if transporte in ["Auto", "Moto", "Taxi/Uber"]:
    recomendaciones.append("Reducir el uso de movilidad motorizada individual o compartir el viaje con otras personas.")
elif transporte == "Colectivo":
    recomendaciones.append("El uso de transporte público reduce la huella por persona frente al vehículo particular.")
else:
    recomendaciones.append("La movilidad activa no generó emisiones directas. Mantener este hábito cuando sea posible.")

if energia_pct > 30:
    recomendaciones.append("Reducir el tiempo de uso de dispositivos o priorizar equipos de menor consumo energético.")

if uso_aire:
    recomendaciones.append("Optimizar el uso del aire acondicionado durante el partido para disminuir el consumo eléctrico.")

if tipo_comida == "Asado":
    recomendaciones.append("El consumo de asado representa una fuente relevante de emisiones. Alternar con opciones de menor impacto.")
elif tipo_comida == "Delivery":
    recomendaciones.append("Reducir envases y traslados asociados al delivery puede disminuir la huella del evento.")

if separacion == "No":
    recomendaciones.append("Separar los residuos generados permite mejorar su recuperación y reducir impactos.")
if reciclaje == "No":
    recomendaciones.append("Enviar materiales reciclables a reciclaje mejora el desempeño ambiental del evento.")
if compostaje == "No":
    recomendaciones.append("Compostar residuos orgánicos reduce la cantidad enviada a disposición final.")

if categoria_ecohincha == "EcoHincha A+":
    comparacion_texto = "Tu nivel EcoHincha indica un desempeño ambiental muy alto. Según tus respuestas, la experiencia evaluada registró una huella muy baja o nula."

elif categoria_ecohincha == "EcoHincha A":
    comparacion_texto = "Tu nivel EcoHincha indica un buen desempeño ambiental. La huella registrada se mantiene en un rango bajo para este tipo de experiencia."

elif categoria_ecohincha == "EcoHincha B":
    comparacion_texto = "Tu nivel EcoHincha indica un desempeño ambiental intermedio. Se identifican algunos aspectos con oportunidad de mejora."

elif categoria_ecohincha == "EcoHincha C":
    comparacion_texto = "Tu nivel EcoHincha indica una huella ambiental significativa. Se recomienda revisar las principales fuentes de emisión registradas."

else:
    comparacion_texto = "Tu nivel EcoHincha indica una huella ambiental alta. Las decisiones de movilidad, consumo energético, alimentación o residuos aumentaron el impacto total del evento."
st.markdown(f"""
<div style="
background-color:#13362F;
padding:24px;
border-radius:16px;
color:white;
margin-top:20px;
">

<h3 style="color:#D8E7B8;">Tu nivel EcoHincha</h3>

<h1 style="color:#D8E7B8;">{categoria_ecohincha}</h1>

<p style="font-size:17px;">
{comparacion_texto}
</p>

</div>
""", unsafe_allow_html=True)

fig_barra = px.bar(
    datos_grafico,
    x="Categoría",
    y="kg CO₂e",
    title="Comparación de emisiones por categoría",
    text="kg CO₂e"
)

st.plotly_chart(fig_barra, use_container_width=True)
st.markdown("---")

st.markdown("""
<div style="
background-color:#13362F;
padding:30px;
border-radius:18px;
color:white;
text-align:center;
margin-top:20px;
">

<h2 style="color:#D8E7B8;">RESULTADO EJECUTIVO</h2>

<p style="font-size:18px;">Huella ambiental estimada del partido</p>

<h1 style="color:#D8E7B8;font-size:60px;">
{:.2f} kg CO₂e
</h1>

<p style="font-size:20px;">
{:.2f} kg CO₂e por persona
</p>

</div>
""".format(emisiones_totales, emisiones_por_persona), unsafe_allow_html=True)
st.markdown("""
<div style="
background-color:#D8E7B8;
padding:20px;
border-radius:14px;
color:#13362F;
margin-top:20px;
">

<h3>Fuente principal de emisión detectada</h3>
<h2>{}</h2>
<p>{:.2f} kg CO₂e</p>

</div>
""".format(categoria_principal, valor_principal), unsafe_allow_html=True)
st.subheader("🏅 Certificación Ambiental")
st.subheader("🔎 Calidad de la medición")



st.success(
    f"""
Certificado generado exitosamente

Categoría obtenida: {categoria_ecohincha}

EcoScore Mundial: {eco_score}/100

Huella total estimada:
{emisiones_totales:.2f} kg CO₂e

Huella por persona:
{emisiones_por_persona:.2f} kg CO₂e/persona
"""
)

st.markdown("""
<div style="
background-color:#FFFFFF;
border:2px solid #2B5D54;
padding:22px;
border-radius:14px;
margin-top:20px;
">

<h3 style="color:#13362F;">Recomendaciones prioritarias para el próximo partido</h3>

</div>
""", unsafe_allow_html=True)

for i, rec in enumerate(recomendaciones, start=1):
    st.markdown(f"""
    <div style="
    background-color:#F6F8F2;
    border-left:6px solid #2B5D54;
    padding:14px;
    border-radius:8px;
    margin-bottom:10px;
    color:#13362F;
    ">
    <b>Recomendación {i}:</b> {rec}
    </div>
    """, unsafe_allow_html=True)
    st.header("🏆 ECOSCORE MUNDIAL™")

puntaje = 100

if emisiones_totales > 5:
    puntaje -= 15
if emisiones_totales > 15:
    puntaje -= 20
if emisiones_totales > 30:
    puntaje -= 25

if separacion == "No":
    puntaje -= 10
if reciclaje == "No":
    puntaje -= 10
if compostaje == "No":
    puntaje -= 5

if transporte in ["Auto", "Taxi/Uber"]:
    puntaje -= 10

puntaje = max(0, puntaje)

if puntaje <= 20:
    perfil = "Hincha de Alto Impacto"
elif puntaje <= 40:
    perfil = "Hincha en Transición"
elif puntaje <= 60:
    perfil = "Hincha Responsable"
elif puntaje <= 80:
    perfil = "Hincha Sustentable"
else:
    perfil = "EcoHincha Mundial™"

st.info(f"Huella de carbono por energía: {emisiones_energia:.2f} kg CO₂e")

st.markdown(f"""
<div style="
background-color:#2B5D54;
padding:22px;
border-radius:14px;
color:white;
margin-top:10px;
">

<h2 style="color:#D8E7B8;">{perfil}</h2>

<p>
Este perfil sintetiza el desempeño ambiental del usuario durante la experiencia de visualización del partido.
La huella de carbono estricta continúa siendo el resultado principal de la medición.
</p>

</div>
""", unsafe_allow_html=True)
st.header("📄 DESCARGA DE RESULTADOS")

resultados = pd.DataFrame({
    "Categoría": [
        "Movilidad",
        "Energía",
        "Alimentación y consumo",
        "Residuos",
        "Total",
        "Por persona",
        "Fuente principal",
        "EcoScore",
        "Perfil"
    ],
    "Resultado": [
        round(emisiones_movilidad, 2),
        round(emisiones_energia, 2),
        round(emisiones_alimentacion, 2),
        round(emisiones_residuos, 2),
        round(emisiones_totales, 2),
        round(emisiones_por_persona, 2),
        categoria_principal,
        puntaje,
        perfil
    ],
    "Unidad": [
        "kg CO₂e",
        "kg CO₂e",
        "kg CO₂e",
        "kg CO₂e",
        "kg CO₂e",
        "kg CO₂e/persona",
        "-",
        "puntos",
        "-"
    ]
})

buffer = BytesIO()

with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
    resultados.to_excel(writer, index=False, sheet_name="Resultado EcoHincha")

st.download_button(
    label="Descargar resultado en Excel",
    data=buffer.getvalue(),
    file_name="resultado_ecohincha_worldcup.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
st.header("📘 INFORME TÉCNICO RESUMIDO")

st.markdown(f"""
<div style="
background-color:#FFFFFF;
border:2px solid #13362F;
padding:24px;
border-radius:14px;
color:#13362F;
">

<h3>EcoHincha World Cup™</h3>
<p><b>Entidad:</b> EGS | Estudio de Gestión de Sistemas</p>
<p><b>Objeto de evaluación:</b> experiencia de visualización de un partido del Mundial.</p>

<p><b>Huella total estimada:</b> {emisiones_totales:.2f} kg CO₂e.</p>
<p><b>Huella por persona:</b> {emisiones_por_persona:.2f} kg CO₂e/persona.</p>
<p><b>Fuente principal de emisión:</b> {categoria_principal}.</p>
<p><b>EcoScore Mundial™:</b> {puntaje}/100.</p>
<p><b>Perfil ambiental:</b> {perfil}.</p>

<h4>Lectura técnica</h4>
<p>
El resultado permite identificar las principales fuentes de emisión asociadas al evento,
considerando movilidad, energía, alimentación, consumo y gestión de residuos.
La medición es de carácter estimativo y orientada a educación ambiental, comunicación climática
y mejora de hábitos sostenibles en eventos deportivos.
</p>

<h4>Recomendaciones prioritarias</h4>
<ul>
{''.join([f'<li>{rec}</li>' for rec in recomendaciones])}
</ul>

</div>
""", unsafe_allow_html=True)
st.header("🗂️ REGISTRO HISTÓRICO DE MEDICIÓN")

nombre_usuario = st.text_input("Nombre o identificación de la medición")

guardar = st.button("Guardar medición")

if guardar:
    nueva_medicion = pd.DataFrame({
        "nombre": [nombre_usuario],
"ciudad": [ciudad],
"provincia": [provincia],
"pais": [pais],
"partido": [partido],

        "huella_total_kg_co2e": [round(emisiones_totales, 2)],
        "huella_por_persona": [round(emisiones_por_persona, 2)],
        "movilidad": [round(emisiones_movilidad, 2)],
        "energia": [round(emisiones_energia, 2)],
        "alimentacion": [round(emisiones_alimentacion, 2)],
        "residuos": [round(emisiones_residuos, 2)],
        "fuente_principal": [categoria_principal],
        "ecoscore": [puntaje],
        "perfil": [perfil]
    })

    try:
        historico = pd.read_csv("registro_ecohincha.csv")
        historico = pd.concat([historico, nueva_medicion], ignore_index=True)
    except FileNotFoundError:
        historico = nueva_medicion

    historico.to_csv("registro_ecohincha.csv", index=False)

    st.success("Medición guardada correctamente.")
    st.header("🌎 OBSERVATORIO ECOHINCHA")

try:
    observatorio = pd.read_csv("registro_ecohincha.csv")

    st.write(f"Mediciones registradas: {len(observatorio)}")

    st.dataframe(
        observatorio[
            [
                "nombre",
                "ciudad",
                "provincia",
                "pais",
                "partido",
                "huella_total_kg_co2e",
                "ecoscore"
            ]
        ]
    )

except:
    st.info("Todavía no existen mediciones registradas.")

st.markdown("---")

st.markdown("""
<div style="
background-color:#13362F;
padding:18px;
border-radius:12px;
color:#D8E7B8;
text-align:center;
">

<h3>EcoHincha World Cup™ | EGS</h3>
<p>
Herramienta educativa de estimación de huella ambiental para eventos deportivos.
</p>

</div>
""", unsafe_allow_html=True)

if st.button("Iniciar nueva medición"):
    st.rerun()

st.header("🌎 RESULTADO FINAL | HUELLA AMBIENTAL DEL PARTIDO")
