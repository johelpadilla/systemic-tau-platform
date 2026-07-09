import streamlit as st

st.set_page_config(
    page_title="Migración Paradigmática",
    page_icon="🧠",
    layout="wide"
)

# Inyectar CSS global (simplificado para mantener consistencia)
st.markdown("""
<style>
    .stp-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 0, 0, 0.05);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .gradient-text {
        background: linear-gradient(90deg, #1E3A8A, #00C6FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='gradient-text'>Migración Paradigmática: De Newton a Tau</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="stp-card">
Bienvenidos. Esta sección está diseñada específicamente para intelectuales, físicos, matemáticos y científicos profundamente arraigados en el paradigma clásico (Newtoniano, Cartesiano, o de sistemas continuos). 

Sabemos que adoptar el paradigma del **Tau Sistémico** y la **Ley del Reloj Extramental Discreto (RECD)** puede generar fricción cognitiva inicial. Esto ocurre porque el paradigma no es solo un cambio de fórmula matemática, sino un **salto ontológico**. Aquí te guiamos paso a paso para realizar esta transición mental de forma estructurada.
</div>
""", unsafe_allow_html=True)

st.header("1. El Choque de Paradigmas")

st.markdown("La principal barrera de entrada no es la matemática, sino las premisas ocultas que hemos naturalizado durante siglos sobre cómo funciona la realidad y el tiempo.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Física Newtoniana Clásica")
    st.markdown("""
    - **El Tiempo absoluto (*Chronos*):** Un contenedor infinito, continuo e independiente de la materia. Los eventos ocurren *dentro* del tiempo.
    - **Métrica Euclidiana:** Distancias y derivadas asumen espacios métricos suaves.
    - **Señales de Alerta Clásicas (CSD):** Se espera que la *varianza* aumente (la amplitud crece) al acercarse a un punto crítico.
    - **Sincronización:** Medida en fase (física) o amplitudes (Pecora-Carroll).
    """)

with col2:
    st.subheader("Física del Tau Sistémico")
    st.markdown("""
    - **Tiempo Emergente Discreto (*Kairos*):** El tiempo no preexiste. Se construye desde abajo hacia arriba por *micro-conjunciones ordinales* dictadas por Feigenbaum (\(\delta\)).
    - **Métrica Ordinal Topológica:** No importa *cuánto* cambia el valor, sino *cómo se alinean los rangos* jerárquicamente.
    - **Tau Sistémico (\(\tau_s\)):** La inestabilidad se detecta por volatilidad ordinal (\(|\tau_s| < 0.41\)), la cual a menudo ocurre cuando la varianza clásica es engañosa.
    - **Antisincronización:** Divergencias robustas detectadas topológicamente (\(\tau_s \le -0.41\)), permitiendo retrocausalidad local.
    """)

st.divider()

st.header("2. Ruta de Desaprendizaje: Soltando las amarras clásicas")

with st.expander("Paso 1: Soltar la Varianza y abrazar el Orden"):
    st.markdown("""
    **El instinto clásico:** *"Para ver si un sistema se desestabiliza, miro si sus oscilaciones se hacen más violentas (varianza / desviación estándar)."*
    
    **El ajuste paradigmático:** En sistemas complejos ruidosos (epidemiología, cardiología, neurociencia), la varianza a menudo sube por estacionalidad o ruido irrelevante. En su lugar, debes mirar **la coherencia del orden**. Piensa en una orquesta: el caos no ocurre cuando tocan más fuerte, sino cuando dejan de leer la misma partitura. El Tau Sistémico (\(\tau_s\)) mide exactamente eso: la pérdida de coherencia ordinal.
    """)

with st.expander("Paso 2: Aceptar el Tiempo como Propiedad Emergente, no como Contenedor"):
    st.markdown("""
    **El instinto clásico:** *"Tengo datos muestreados cada 1 milisegundo o cada semana. Ese es mi eje X."*
    
    **El ajuste paradigmático:** Ese es el tiempo del observador (tu reloj). El **Reloj Extramental Discreto (RECD)** postula que el sistema tiene su propio reloj interno. Sus "tics" solo avanzan cuando ocurren eventos de conjunción estructural genuinos (en el rango caótico \(|\tau_s| < 0.41\)). Si no hay conjunción, para el sistema, el tiempo ontológico no ha avanzado. Esto es lo que significa que el tiempo se *contrae* de forma fractal gobernado por la constante universal de Feigenbaum (\(\delta \approx 4.6692\)).
    """)

with st.expander("Paso 3: Digerir la Retrocausalidad Local y la Antisincronización"):
    st.markdown("""
    **El instinto clásico:** *"El tiempo siempre fluye hacia adelante, y los sistemas divergen de forma asimétrica."*
    
    **El ajuste paradigmático:** En regímenes de **antisincronización fuerte (\(\tau_s \le -0.41\))**, la compuerta universal del tiempo adopta un valor negativo (\(g(\tau_s) = -1\)). Esto no es un error matemático, es una anti-cronología local donde el reloj sistémico retrocede momentáneamente, permitiendo bucles de *futuribles*. Esto ha sido probado empíricamente tanto en atractores de Lorenz como en la dinámica *Aedes aegypti* (Caño Martín Peña) bajo fumigaciones forzadas.
    """)

st.divider()

st.header("3. La Analogía Intelectual: Aristóteles, Polo y la Física No Lineal")

st.markdown("""
Para cerrar la brecha, es altamente útil conectar este marco con la filosofía clásica y el realismo trascendental de **Leonardo Polo**. 
- Los intelectuales clásicos sufren porque intentan encajar el Tau Sistémico en la **Física de Newton**. 
- El paradigma de Padilla-Villanueva (2025-2026) encaja perfectamente en la **Física Filosófica**:

1. **Materia Prima:** La pura potencia latente de la red, donde la disonancia ordinal es alta.
2. **Forma Física:** La vectorización de los rangos ordinales que capturan la identidad transitoria del sistema.
3. **Causa Eficiente:** La **constante de Feigenbaum (\(\delta\))**. Actúa como el motor ontológico puro, inyectando dinamismo irreversible que actualiza la temporalidad fractal del sistema.

> *"La flecha del tiempo no es un epifenómeno estadístico termodinámico. Es una propiedad ontológica primaria, esculpida directamente por las bifurcaciones caóticas."* 
""")

st.success("💡 **Consejo Pedagógico Final:** No intentes forzar tus datos a un modelo predictivo continuo. Convierte tus variables multivariadas a rangos (rankings), cálcula las concordancias de Kendall en ventanas temporales, y deja que los umbrales topológicos (+0.50, 0.41, -0.41) revelen el atractor subyacente. La matemática del caos ordinal hará el resto.")
