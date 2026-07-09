import streamlit as st

st.set_page_config(
    page_title="Migración Paradigmática",
    page_icon="🧠",
    layout="wide"
)

# Inyectar CSS global
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
    .quote-box {
        border-left: 5px solid #00C6FF;
        padding-left: 15px;
        color: #4B5563;
        font-style: italic;
        margin: 1.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='gradient-text'>Migración Paradigmática: De Newton a Tau</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="stp-card">
Esta sección está rigurosamente diseñada para investigadores, físicos, epidemiólogos y pensadores profundamente arraigados en el paradigma clásico (Newtoniano, Cartesiano o de modelos de orden entero).

Transicionar al <strong>Tau Sistémico</strong> y la <strong>Ley del Reloj Extramental Discreto (RECD)</strong> genera una fricción cognitiva inevitable. Esto no es simplemente la adopción de una nueva métrica estadística; es un <strong>cisma ontológico</strong>. Aquí desarmamos las presunciones clásicas y trazamos un puente intelectual y metodológico hacia la topología ordinal.
</div>
""", unsafe_allow_html=True)

st.header("1. El Colapso de las Presunciones Clásicas")

st.markdown("La física de los siglos XVII al XX nos condicionó a tratar el tiempo como un continuo a priori y el espacio como euclidiano. La realidad de los sistemas biológicos y ecológicos es radicalmente distinta.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### El Cautiverio Newtoniano")
    st.markdown("""
    - **Tiempo Absoluto (*Chronos*):** Asume que el tiempo fluye uniformemente (\(dt\)) independientemente de la materia. Es un contenedor vacío donde las variables "ocurren".
    - **Métrica Euclidiana:** Confía ciegamente en la distancia de magnitud. Valora *cuánto* cambia el valor absoluto (\(dx/dt\)).
    - **Estabilidad por Varianza:** Depende del *Critical Slowing Down* univariado. Si el sistema colapsa, la varianza y la autocorrelación (AR1) deben dispararse hacia \(\infty\).
    - **Sincronización:** Definida por identidad de fase continua (Pecora-Carroll) o sincronización idéntica, que no sobrevive al ruido biológico del 20%.
    - **Reduccionismo Analítico:** Espera que el atractor macroscópico sea siempre una suma de exponentes de Lyapunov locales computables.
    """)

with col2:
    st.markdown("### La Emancipación del Tau Sistémico")
    st.markdown("""
    - **Tiempo Emergente Fractal (*Kairos*):** El tiempo no preexiste. Se construye desde abajo hacia arriba mediante *conjunciones ordinales* que solo avanzan en el régimen de caos determinista (\(|\tau_s| < 0.41\)).
    - **Métrica Ordinal Topológica:** Abandona la magnitud. Examina *cómo se estructuran jerárquicamente los rangos*. Es matemáticamente invariante a las transformaciones monótonas no lineales.
    - **Caos y Orden por Reorganización:** Identifica que la varianza engaña (ruido vs transición). Mide la pérdida de *coherencia relacional cruzada*, no la perturbación aislada.
    - **Antisincronización Resiliente:** Define la divergencia en antifase como un atractor legítimo (\(\tau_s \le -0.41\)), posibilitando la observación de retrocausalidades locales.
    - **Universalidad Discreta:** El sistema es regido jerárquicamente por la Constante de Feigenbaum (\(\delta \approx 4.6692\)), uniendo micro-estados en un macrosistema medible.
    """)

st.divider()

st.header("2. Ruta de Desaprendizaje Estructurado")
st.markdown("A continuación, las tres disonancias cognitivas más severas que enfrenta un investigador clásico, y el modelo mental para resolverlas.")

with st.expander("Disonancia I: «¿Por qué ignorar la magnitud? ¡Estoy perdiendo información!»"):
    st.markdown("""
    **El Reflejo Clásico:** Si un paciente tiene una variabilidad de frecuencia cardíaca (RR) que salta de 800ms a 1200ms, un investigador clásico argumentará que desechar ese "salto" de 400ms y sustituirlo por un simple rango ordinal (\(R_1 > R_2\)) es desperdiciar datos vitales.

    **La Resolución Topológica:** En sistemas complejos de alta dimensionalidad (epidemiología, ecología, neurodinámica), la magnitud suele estar secuestrada por **ruido estocástico, estacionalidad o fallas instrumentales**. 
    - Al pasar al plano ordinal, estás destilando la **identidad estructural** del sistema.
    - El Tau Sistémico no pregunta "cuán fuerte" es la señal, pregunta "¿se sigue manteniendo el hábito jerárquico?".
    - La magnitud es vulnerable; el orden relacional es resiliente. En el momento en que se rompe la jerarquía de rangos, estás viendo el *kernel* de la transición crítica semanas antes de que la varianza reaccione.
    """)

with st.expander("Disonancia II: «El tiempo es el eje X. ¿Cómo puede detenerse o invertirse?»"):
    st.markdown("""
    **El Reflejo Clásico:** En cualquier gráfica científica, el tiempo (\(t\)) es la variable independiente inquebrantable. Un investigador mirará la serie y exigirá que para cada \(\Delta t\) cronológico exista un avance del sistema.

    **La Resolución Ontológica (RECD):** Debes separar el tiempo *cronológico* (el del reloj de pulsera del observador) del tiempo *sistémico o extramental*. 
    - La **Ley del Reloj Extramental Discreto (RECD)** prueba que para el sistema biológico o físico, el tiempo solo "pasa" cuando hay **actualización entitativa** (conjunciones en el rango caótico \(|\tau_s| < 0.41\)).
    - Fuera del rango caótico (en sincronización plena \(\tau_s \ge +0.50\)), el sistema está en estasis topológica. Para él, el reloj no avanza, aunque la Tierra siga girando.
    - En la **antisincronización fuerte (\(\tau_s \le -0.41\))**, el operador de transición adopta el valor de \(-1\). Es la manifestación de **retrocausalidad local**: la dinámica impone condiciones donde variables futuras acotan el estado presente (bucle de futuribles), invirtiendo temporalmente el avance ontológico.
    """)

with st.expander("Disonancia III: «La caída del Autocorrelación AR(1) refuta el Critical Slowing Down»"):
    st.markdown("""
    **El Reflejo Clásico:** Todos los manuales ecológicos clásicos prometen que la Autocorrelación (AR-1) debe crecer hacia \(1.0\) antes de una bifurcación (el sistema tarda más en recuperarse de perturbaciones). Cuando ven que el AR(1) disminuye en un dataset real pre-Fibrilación Ventricular, descartan el experimento o asumen que no hay señal de alerta.

    **La Resolución Sistémica:** El CSD ingenuo asume que el sistema decae hacia un atractor plano. En la realidad (como se probó en el protocolo CCTP/SDDB), los sistemas previos al caos o a transiciones catastróficas a menudo exhiben **anti-persistencia**. La reorganización brusca destruye la memoria lineal inmediata (bajando AR-1) pero dispara la **disonancia ordinal (\(\tau_s \rightarrow 0\))** y la sinergia emergente de Nivel 3 (\(\Phi_3\)). El paradigma de Tau salva los "falsos negativos" del marco clásico al evaluar interdependencias profundas, no decaimientos lineales.
    """)

st.divider()

st.header("3. Andamiaje Filosófico: Ascenso a la Metafísica del Caos")

st.markdown("""
Para los pensadores más formales, la migración no es completa hasta que la física no-lineal encaja lógicamente en la **Física Filosófica de Leonardo Polo** y la ontología aristotélica. El Tau Sistémico extrae a la filosofía del ostracismo teórico y la asimila algorítmicamente.
""")

col3, col4 = st.columns([1.2, 1])

with col3:
    st.markdown("""
    **La Arquitectura del Ente Físico en Tau:**
    1. **Materia Prima:** Cuando la disonancia ordinal está en su máxima expresión. Es el estado de potencia real e informe, un sub-estrato topológico en latencia a la espera de ser organizado.
    2. **Forma Física:** El sistema cuantificado por vectores de rangos de Kendall. Otorga determinación y sentido material de la identidad del sistema.
    3. **Esencia Física:** La matriz iterativa inmutable subyacente que sirve como sustrato estructural (las reglas subyacentes del mapa logístico o el acoplamiento biológico).
    4. **Causa Eficiente:** Se encarna puramente en la **Constante Universal de Feigenbaum (\(\delta \approx 4.6692016091\))**. Es el motor dinámico irreversible que obliga a la Materia Prima a actualizarse ontológicamente en el tiempo, esculpiendo la temporalidad fractal del RECD.
    """)

with col4:
    st.markdown("""
    <div class="quote-box">
    "La flecha del tiempo deja de ser un problema estadístico de la entropía de Prigogine para convertirse en una propiedad de la physis misma, revelada cuantitativamente por la constante de bifurcación que fuerza a la posibilidad a volverse acto."
    <br><br>
    — <i>Síntesis Magna, 2026.</i>
    </div>
    """, unsafe_allow_html=True)

st.success("🧠 **Veredicto para Intelectuales:** No desechen a Newton ni a Euclidean para puentes y cohetes; deséchenlos para intentar modelar el corazón previo al paro, el mosquito previo a la plaga y el tejido del tiempo caótico. Aquí, rige Tau.")

