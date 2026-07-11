import os

# Define the domains and their tailored narratives in ES, EN, and FR.
# The tone must be strictly formal, elegant, and professional.

CONTENT = {
    "es": {
        "cardiologia": """# Dominio Científico: Cardiología Computacional y Dinámica Cardíaca

## 1. Contexto Científico y Desafío Clínico
La predicción de la **muerte súbita cardíaca** inducida por **fibrilación ventricular (FV)** constituye uno de los mayores desafíos en la electrofisiología moderna. A pesar de la abundancia de datos en registros Holter continuos, los biomarcadores tradicionales extraídos del electrocardiograma (ECG) de superficie frecuentemente fracasan en anticipar la transición hacia la arritmia fatal.

## 2. El Comportamiento de Tau Sistémica
En la dinámica cardiovascular, **Tau Sistémica (τ_s)** no rastrea la simple fluctuación de la frecuencia cardíaca, sino que cuantifica la **reorganización relacional ordinal** entre el intervalo RR y su tasa de variación. 

Previo a un evento crítico (FV), el corazón no experimenta un simple "enlentecimiento crítico" (*critical slowing down*). En su lugar, el sistema entra en un régimen de **desacoplamiento topológico**. τ_s detecta cómo la estructura simbólica de la variabilidad latido a latido colapsa, capturando el agotamiento de la sinergia fisiológica (medido a través de **excess3**).

## 3. Limitaciones de las Métricas Convencionales
- **Varianza (SDNN/RMSSD):** Tiende a aumentar de forma errática (firma tipo CSD), pero presenta alta susceptibilidad a artefactos y extrasístoles.
- **Autocorrelación (AR1):** Contraintuitivamente, suele exhibir *anti-persistencia* antes de la FV, contradiciendo los modelos clásicos de EWS.
- **Tau Sistémica (τ_s):** Exhibe una robustez excepcional frente al ruido sináptico y *pacing* intermitente, ofreciendo una ventana de alerta temprana significativamente mayor y una tasa de falsos positivos drásticamente reducida.

## 4. Evidencia Empírica (Cohorte CCTP)
Las investigaciones sobre la base de datos *Sudden Cardiac Death Holter Database* (SDDB) demuestran que el reloj extramental cardíaco experimenta una emergencia medible, manifestando una dimensión fractal intrínseca y estable previo a la pérdida de homeostasis.""",

        "epidemiologia": """# Dominio Científico: Epidemiología Dinámica y Salud Pública

## 1. Contexto Científico y Desafío Epidemiológico
La transición de estados endémicos a **brotes epidémicos severos** (e.g., Dengue, enfermedades infecciosas emergentes) obedece a dinámicas no lineales complejas. Anticipar el punto de bifurcación epidemiológica basándose puramente en la tasa de incidencia histórica genera alertas tardías, comprometiendo la respuesta de salud pública.

## 2. El Comportamiento de Tau Sistémica
En el ecosistema epidemiológico, **Tau Sistémica (τ_s)** evalúa la sincronización y la estructura relacional entre múltiples vectores (por ejemplo, clima, densidad poblacional, y tasas de infección por estratos). 

Conforme el sistema se acerca a un brote epidémico, τ_s detecta una **pérdida de complejidad relacional**. Las variables epidemiológicas comienzan a alinearse en patrones ordinales altamente predecibles antes de que ocurra la explosión en la varianza de casos. Tau Sistémica actúa como un sismógrafo de la estructura de la red de contagio.

## 3. Limitaciones de las Métricas Convencionales
- **Modelos SIR Estándar:** Asumen homogeneidad de mezcla y tasas de contacto constantes, fallando ante transiciones críticas abruptas.
- **Varianza Espacial:** El aumento de la varianza en los reportes de casos ocurre simultáneamente con el brote, perdiendo su utilidad predictiva.
- **Tau Sistémica (τ_s):** Captura el acoplamiento silente entre los factores ambientales y los hospederos (cuantificado vía **excess3**), emitiendo señales de alerta fundamentadas en la topología de la infección antes del crecimiento exponencial.

## 4. Aplicación Práctica
La integración de τ_s en plataformas de vigilancia epidemiológica permite a los gestores de salud pública estratificar el riesgo sistémico de manera proactiva, diferenciando fluctuaciones estacionales benignas de verdaderas transiciones críticas hacia el estado epidémico.""",

        "neurociencia": """# Dominio Científico: Neurociencia Computacional y Dinámica Cerebral

## 1. Contexto Científico y Desafío Clínico
El cerebro humano opera en un estado de criticidad autoorganizada. Transiciones patológicas abruptas, tales como las **crisis epilépticas**, requieren de la identificación de estados *pre-ictales* en señales de electroencefalografía (EEG). Sin embargo, la detección temprana se ve obstaculizada por la abrumadora dimensionalidad y el ruido inherente de la actividad cortical.

## 2. El Comportamiento de Tau Sistémica
En la red neuronal, **Tau Sistémica (τ_s)** cuantifica la topología de la conectividad funcional en el dominio del tiempo. En lugar de medir amplitudes, evalúa la **coherencia ordinal** entre múltiples canales de EEG.

Al aproximarse a una crisis epiléptica, la neurodinámica experimenta una transición hacia la hiper-sincronización. τ_s captura este fenómeno observando cómo la diversidad de microestados relacionales colapsa drásticamente. El **RECD** revela que las estructuras sinérgicas de alto orden (medidas por **excess3**) se disuelven, forzando al sistema a converger hacia un atractor patológico de baja dimensionalidad.

## 3. Limitaciones de las Métricas Convencionales
- **Análisis Espectral (FFT):** Identifica cambios en las bandas de frecuencia, pero es incapaz de medir la interacción n-dimensional no lineal entre áreas corticales.
- **Exponente de Lyapunov:** Computacionalmente prohibitivo para el monitoreo clínico en tiempo real y altamente susceptible al ruido instrumental.
- **Tau Sistémica (τ_s):** Al basarse en la permutación simbólica (Bandt-Pompe), ignora el ruido de amplitud y filtra los artefactos musculares, aislando exclusivamente la arquitectura causal de la inminente transición ictogénica.

## 4. Relevancia Clínica
El paradigma Tau Sistémica ofrece a la neurofisiología una herramienta rigurosa para trazar la "huella digital" topológica de la corteza cerebral, viabilizando el desarrollo de sistemas neuro-moduladores de lazo cerrado (closed-loop) más anticipatorios.""",

        "ecologia": """# Dominio Científico: Ecología de Sistemas y Dinámica de Poblaciones

## 1. Contexto Científico y Desafío Ecológico
Los ecosistemas naturales experimentan **cambios de régimen catastróficos** (e.g., eutrofización de lagos, desertificación, colapso de pesquerías) desencadenados por estresores estocásticos e interacciones tróficas no lineales. Predecir estos colapsos antes de que el ecosistema cruce un punto de no retorno (histéresis) es fundamental para la conservación ambiental.

## 2. El Comportamiento de Tau Sistémica
En la ecología matemática, **Tau Sistémica (τ_s)** actúa como un sensor de la resiliencia estructural. No analiza la densidad poblacional aislada, sino la red de **interdependencias ordinales** entre especies (ej. fito/zooplancton) y factores abióticos (ej. temperatura, fósforo).

Antes de un colapso ecológico, los ecosistemas sufren un declive en su "conectividad sinérgica". τ_s percibe cómo los microestados de la red trófica pierden su heterogeneidad estructural. El parámetro **excess3** documenta matemáticamente la erosión de la resiliencia del ecosistema, señalando el momento en que las interacciones estabilizadoras son superadas por retroalimentaciones positivas desestabilizadoras.

## 3. Limitaciones de las Métricas Convencionales
- **Varianza y Autocorrelación Espacial (EWS clásicos):** A menudo generan falsos positivos inducidos por el ruido ambiental (clima) y dependen críticamente del modelado *Critical Slowing Down* (CSD), el cual no siempre aplica en redes ecológicas complejas.
- **Biomasa Agregada:** Una métrica rezagada que solo muestra alteración una vez que el colapso trófico es irreversible.
- **Tau Sistémica (τ_s):** Al ser invariante a transformaciones monótonas (inmune a ciertas fluctuaciones abióticas), aísla exclusivamente la desintegración de la lógica relacional del ecosistema.

## 4. Impacto en la Conservación
La integración del marco RECD permite a los ecólogos computacionales establecer umbrales de intervención temprana (early-warning signals) altamente calibrados, protegiendo ecosistemas frágiles con fundamentos topológicos rigurosos.""",

        "finanzas": """# Dominio Científico: Econofísica y Mercados Financieros

## 1. Contexto Científico y Desafío Económico
Los mercados financieros globales exhiben comportamientos de sistemas complejos fuertemente acoplados. Las crisis de liquidez y los *flash crashes* representan transiciones de fase impulsadas por dinámicas especulativas y algoritmos de alta frecuencia. Anticipar estas disrupciones exige ir más allá del paradigma clásico de la varianza estocástica.

## 2. El Comportamiento de Tau Sistémica
En la econofísica, **Tau Sistémica (τ_s)** mide la **rigidez topológica** del flujo de capitales. En lugar de evaluar retornos aislados, examina la co-evolución ordinal entre múltiples activos o índices financieros (e.g., S&P 500, VIX, bonos del tesoro).

Antes de un colapso sistémico en el mercado, se observa una "cristalización" de las dependencias inter-activos. τ_s detecta cómo el sistema financiero entra en un estado de hipersincronización ordinal. La pérdida repentina de grados de libertad y la disolución de la sinergia diversificadora (observada a través de la contracción de **excess3**) fungen como el precursor matemático del crash financiero.

## 3. Limitaciones de las Métricas Convencionales
- **Volatilidad (VIX / GARCH):** Mide la dispersión del retorno, pero históricamente actúa como un indicador coincidente o reactivo, no anticipatorio.
- **Correlación de Pearson:** Captura únicamente relaciones lineales y colapsa ante la estructura fractal y las colas pesadas (*fat tails*) de las distribuciones de retornos.
- **Tau Sistémica (τ_s):** Libre de supuestos distribucionales. Al operar en el espacio simbólico de Bandt-Pompe, es resistente a *outliers* y capaz de detectar la arquitectura causal subyacente que orquesta el pánico del mercado.

## 4. Relevancia Financiera
La implementación del marco RECD dota a los analistas cuantitativos e investigadores financieros de un instrumental de última generación para auditar el riesgo sistémico, ofreciendo señales de alerta temprana fundamentadas en la termodinámica de sistemas lejos del equilibrio."""
    },
    "en": {
        "cardiologia": """# Scientific Domain: Computational Cardiology and Cardiac Dynamics

## 1. Scientific Context and Clinical Challenge
The anticipation of **sudden cardiac death** induced by **ventricular fibrillation (VF)** remains one of the preeminent challenges in modern electrophysiology. Despite the abundance of continuous Holter monitoring data, traditional biomarkers extracted from the surface electrocardiogram (ECG) consistently fail to reliably forecast the transition into fatal arrhythmias.

## 2. The Behavior of Systemic Tau
Within cardiovascular dynamics, **Systemic Tau (τ_s)** does not merely track heart rate fluctuations; rather, it quantifies the **ordinal relational reorganization** between the RR interval and its rate of change.

Prior to a critical event (VF), the heart does not undergo simple "critical slowing down" (CSD). Instead, the system enters a regime of **topological decoupling**. τ_s detects the collapse of the symbolic structure within beat-to-beat variability, capturing the depletion of physiological synergy (measured through the **excess3** parameter).

## 3. Limitations of Conventional Metrics
- **Variance (SDNN/RMSSD):** Tends to increase erratically (a CSD-like signature), but suffers from high susceptibility to artifacts and ectopic beats.
- **Autocorrelation (AR1):** Counterintuitively, it often exhibits *anti-persistence* prior to VF, contradicting classical Early Warning Signal (EWS) models.
- **Systemic Tau (τ_s):** Demonstrates exceptional robustness against synaptic noise and intermittent pacing, offering a significantly wider early warning window and a drastically reduced false-positive rate.

## 4. Empirical Evidence (CCTP Cohort)
Research utilizing the *Sudden Cardiac Death Holter Database* (SDDB) demonstrates that the cardiac extramental clock undergoes a measurable emergence, establishing a stable, intrinsic fractal dimension prior to the critical loss of homeostasis.""",

        "epidemiologia": """# Scientific Domain: Dynamic Epidemiology and Public Health

## 1. Scientific Context and Epidemiological Challenge
The transition from endemic states to **severe epidemic outbreaks** (e.g., Dengue, emerging infectious diseases) is governed by complex, non-linear dynamics. Attempting to anticipate the epidemiological bifurcation point based purely on historical incidence rates yields delayed warnings, thereby compromising public health response efficacy.

## 2. The Behavior of Systemic Tau
In the epidemiological ecosystem, **Systemic Tau (τ_s)** evaluates the synchronization and relational structure across multiple vectors (e.g., climatic variables, population density, and stratified infection rates).

As the system approaches an epidemic outbreak, τ_s detects a profound **loss of relational complexity**. Epidemiological variables begin to align into highly predictable ordinal patterns long before the variance in reported cases explodes. Systemic Tau acts as a seismograph for the topological structure of the contagion network.

## 3. Limitations of Conventional Metrics
- **Standard SIR Models:** Rely on assumptions of homogeneous mixing and constant contact rates, which fail abruptly during critical systemic transitions.
- **Spatial Variance:** The surge in variance of case reports occurs simultaneously with the outbreak, stripping it of any predictive utility.
- **Systemic Tau (τ_s):** Captures the silent coupling between environmental drivers and hosts (quantified via **excess3**), emitting rigorous early warning signals based on infection topology prior to exponential growth.

## 4. Practical Application
The integration of τ_s into epidemiological surveillance platforms enables public health administrators to proactively stratify systemic risk, effectively distinguishing benign seasonal fluctuations from genuine critical transitions toward an epidemic state.""",

        "neurociencia": """# Scientific Domain: Computational Neuroscience and Brain Dynamics

## 1. Scientific Context and Clinical Challenge
The human brain operates in a state of self-organized criticality. Abrupt pathological transitions, such as **epileptic seizures**, necessitate the precise identification of *pre-ictal* states in electroencephalographic (EEG) signals. However, early detection is heavily impeded by the overwhelming dimensionality and inherent background noise of cortical activity.

## 2. The Behavior of Systemic Tau
Within neural networks, **Systemic Tau (τ_s)** quantifies the topology of functional connectivity in the temporal domain. Rather than measuring signal amplitudes, it evaluates the **ordinal coherence** across multiple EEG channels.

As the brain approaches an epileptic crisis, neurodynamics undergo a transition toward hyper-synchronization. τ_s captures this phenomenon by observing how the diversity of relational microstates collapses drastically. The **RECD** framework reveals that high-order synergistic structures (measured by **excess3**) dissolve, forcing the system to converge into a low-dimensional pathological attractor.

## 3. Limitations of Conventional Metrics
- **Spectral Analysis (FFT):** Identifies shifts in frequency bands but remains incapable of measuring non-linear, n-dimensional interactions across cortical areas.
- **Lyapunov Exponent:** Computationally prohibitive for real-time clinical monitoring and highly susceptible to instrumental noise.
- **Systemic Tau (τ_s):** By utilizing symbolic permutation (Bandt-Pompe), it fundamentally ignores amplitude noise and filters muscular artifacts, exclusively isolating the causal architecture of the impending ictogenic transition.

## 4. Clinical Relevance
The Systemic Tau paradigm provides neurophysiology with a rigorous mathematical instrument to trace the topological "fingerprint" of the cerebral cortex, paving the way for the development of highly anticipatory, closed-loop neuromodulation systems.""",

        "ecologia": """# Scientific Domain: Systems Ecology and Population Dynamics

## 1. Scientific Context and Ecological Challenge
Natural ecosystems undergo **catastrophic regime shifts** (e.g., lake eutrophication, desertification, fishery collapse) triggered by stochastic stressors and non-linear trophic interactions. Predicting these collapses before the ecosystem crosses a tipping point of no return (hysteresis) is paramount for environmental conservation.

## 2. The Behavior of Systemic Tau
Within mathematical ecology, **Systemic Tau (τ_s)** serves as a precise sensor of structural resilience. It does not analyze isolated population densities; rather, it scrutinizes the network of **ordinal interdependencies** between species (e.g., phyto/zooplankton) and abiotic drivers (e.g., temperature, phosphorus).

Prior to an ecological collapse, ecosystems suffer a severe decline in "synergistic connectivity." τ_s perceives how the microstates of the trophic web lose their structural heterogeneity. The **excess3** parameter mathematically documents the erosion of ecosystem resilience, pinpointing the critical threshold where stabilizing interactions are overwhelmed by destabilizing positive feedbacks.

## 3. Limitations of Conventional Metrics
- **Spatial Variance and Autocorrelation (Classical EWS):** Frequently generate false positives induced by environmental (climatic) noise and rely critically on the *Critical Slowing Down* (CSD) assumption, which may not hold in complex ecological networks.
- **Aggregate Biomass:** A lagging indicator that only reflects alteration once trophic collapse has become irreversible.
- **Systemic Tau (τ_s):** Being invariant to monotonic transformations (immune to certain abiotic fluctuations), it exclusively isolates the disintegration of the ecosystem's underlying relational logic.

## 4. Conservation Impact
The integration of the RECD framework empowers computational ecologists to establish highly calibrated early-warning signals, safeguarding fragile ecosystems through rigorous topological foundations.""",

        "finanzas": """# Scientific Domain: Econophysics and Financial Markets

## 1. Scientific Context and Economic Challenge
Global financial markets exhibit the hallmark behaviors of strongly coupled complex systems. Liquidity crises and *flash crashes* represent phase transitions driven by speculative dynamics and high-frequency algorithmic trading. Anticipating these disruptions demands transcending the classical paradigm of stochastic variance.

## 2. The Behavior of Systemic Tau
Within econophysics, **Systemic Tau (τ_s)** measures the **topological rigidity** of capital flows. Rather than evaluating isolated returns, it examines the ordinal co-evolution across multiple assets or financial indices (e.g., S&P 500, VIX, treasury bonds).

Prior to a systemic market collapse, a "crystallization" of inter-asset dependencies occurs. τ_s detects how the financial system enters a state of ordinal hyper-synchronization. The abrupt loss of degrees of freedom and the dissolution of diversifying synergy (observed via the contraction of **excess3**) serve as the mathematical precursor to the financial crash.

## 3. Limitations of Conventional Metrics
- **Volatility (VIX / GARCH):** Measures return dispersion, but historically acts as a coincident or reactive indicator, lacking true anticipatory power.
- **Pearson Correlation:** Captures only linear relationships and completely collapses when confronted with the fractal structure and fat tails of asset return distributions.
- **Systemic Tau (τ_s):** Entirely free of distributional assumptions. By operating within the symbolic space of Bandt-Pompe, it is robust to *outliers* and capable of detecting the causal architecture orchestrating market panic.

## 4. Financial Relevance
The implementation of the RECD framework equips quantitative analysts and financial researchers with next-generation instrumentation to audit systemic risk, offering early-warning signals rooted in the thermodynamics of systems far from equilibrium."""
    },
    "fr": {
        "cardiologia": """# Domaine Scientifique : Cardiologie Computationnelle et Dynamique Cardiaque

## 1. Contexte Scientifique et Défi Clinique
L'anticipation de la **mort subite d'origine cardiaque** induite par une **fibrillation ventriculaire (FV)** demeure l'un des défis majeurs de l'électrophysiologie moderne. Malgré l'abondance de données issues de l'enregistrement Holter continu, les biomarqueurs traditionnels extraits de l'électrocardiogramme (ECG) de surface échouent fréquemment à prévoir la transition vers une arythmie fatale.

## 2. Le Comportement de Tau Systémique
Dans la dynamique cardiovasculaire, **Tau Systémique (τ_s)** ne se contente pas de suivre les fluctuations de la fréquence cardiaque ; il quantifie la **réorganisation relationnelle ordinale** entre l'intervalle RR et son taux de variation.

Avant un événement critique (FV), le cœur ne subit pas un simple "ralentissement critique" (*critical slowing down*). Le système entre plutôt dans un régime de **découplage topologique**. τ_s détecte l'effondrement de la structure symbolique au sein de la variabilité battement par battement, capturant l'épuisement de la synergie physiologique (mesuré par le paramètre **excess3**).

## 3. Limites des Métriques Conventionnelles
- **Variance (SDNN/RMSSD) :** A tendance à augmenter de façon erratique (une signature de type CSD), mais souffre d'une forte susceptibilité aux artefacts et aux extrasystoles.
- **Autocorrélation (AR1) :** Contre toute attente, elle présente souvent une *anti-persistance* avant la FV, contredisant les modèles classiques d'Alerte Précoce (EWS).
- **Tau Systémique (τ_s) :** Fait preuve d'une robustesse exceptionnelle face au bruit synaptique et à la stimulation (pacing) intermittente, offrant une fenêtre d'alerte précoce significativement plus large et un taux de faux positifs drastiquement réduit.

## 4. Preuves Empiriques (Cohorte CCTP)
Les recherches menées sur la base de données *Sudden Cardiac Death Holter Database* (SDDB) démontrent que l'horloge extramentale cardiaque subit une émergence mesurable, établissant une dimension fractale intrinsèque et stable avant la perte critique de l'homéostasie.""",

        "epidemiologia": """# Domaine Scientifique : Épidémiologie Dynamique et Santé Publique

## 1. Contexte Scientifique et Défi Épidémiologique
La transition d'états endémiques vers des **épidémies sévères** (ex. Dengue, maladies infectieuses émergentes) est régie par des dynamiques complexes et non linéaires. Tenter d'anticiper le point de bifurcation épidémiologique en se basant purement sur les taux d'incidence historiques génère des alertes tardives, compromettant ainsi l'efficacité de la réponse de santé publique.

## 2. Le Comportement de Tau Systémique
Dans l'écosystème épidémiologique, **Tau Systémique (τ_s)** évalue la synchronisation et la structure relationnelle entre de multiples vecteurs (ex. variables climatiques, densité de population et taux d'infection stratifiés).

À mesure que le système s'approche d'une flambée épidémique, τ_s détecte une profonde **perte de complexité relationnelle**. Les variables épidémiologiques commencent à s'aligner dans des schémas ordinaux hautement prévisibles bien avant que la variance des cas signalés n'explose. Tau Systémique agit comme un sismographe de la topologie du réseau de contagion.

## 3. Limites des Métriques Conventionnelles
- **Modèles SIR Standards :** Reposent sur des hypothèses de mélange homogène et de taux de contact constants, qui échouent brusquement lors des transitions systémiques critiques.
- **Variance Spatiale :** L'augmentation de la variance dans les signalements de cas se produit simultanément avec l'épidémie, ce qui lui ôte toute utilité prédictive.
- **Tau Systémique (τ_s) :** Capture le couplage silencieux entre les moteurs environnementaux et les hôtes (quantifié via **excess3**), émettant des signaux d'alerte précoce rigoureux basés sur la topologie de l'infection avant la croissance exponentielle.

## 4. Application Pratique
L'intégration de τ_s dans les plateformes de surveillance épidémiologique permet aux administrateurs de la santé publique de stratifier de manière proactive le risque systémique, distinguant efficacement les fluctuations saisonnières bénignes des véritables transitions critiques vers un état épidémique.""",

        "neurociencia": """# Domaine Scientifique : Neurosciences Computationnelles et Dynamique Cérébrale

## 1. Contexte Scientifique et Défi Clinique
Le cerveau humain opère dans un état de criticité auto-organisée. Les transitions pathologiques abruptes, telles que les **crises d'épilepsie**, nécessitent l'identification précise des états *pré-ictaux* dans les signaux électroencéphalographiques (EEG). Cependant, la détection précoce est lourdement entravée par la dimensionnalité écrasante et le bruit de fond inhérent à l'activité corticale.

## 2. Le Comportement de Tau Systémique
Au sein des réseaux neuronaux, **Tau Systémique (τ_s)** quantifie la topologie de la connectivité fonctionnelle dans le domaine temporel. Plutôt que de mesurer l'amplitude des signaux, il évalue la **cohérence ordinale** entre plusieurs canaux EEG.

À l'approche d'une crise d'épilepsie, la neurodynamique subit une transition vers l'hyper-synchronisation. τ_s capture ce phénomène en observant comment la diversité des micro-états relationnels s'effondre drastiquement. Le cadre **RECD** révèle que les structures synergiques d'ordre supérieur (mesurées par **excess3**) se dissolvent, forçant le système à converger vers un attracteur pathologique de basse dimension.

## 3. Limites des Métriques Conventionnelles
- **Analyse Spectrale (FFT) :** Identifie les décalages dans les bandes de fréquences mais reste incapable de mesurer les interactions non linéaires et n-dimensionnelles entre les aires corticales.
- **Exposant de Lyapunov :** D'un coût de calcul prohibitif pour la surveillance clinique en temps réel et hautement sensible au bruit instrumental.
- **Tau Systémique (τ_s) :** En utilisant la permutation symbolique (Bandt-Pompe), il ignore fondamentalement le bruit d'amplitude et filtre les artefacts musculaires, isolant exclusivement l'architecture causale de la transition ictogène imminente.

## 4. Pertinence Clinique
Le paradigme de Tau Systémique fournit à la neurophysiologie un instrument mathématique rigoureux pour tracer "l'empreinte digitale" topologique du cortex cérébral, ouvrant la voie au développement de systèmes de neuromodulation en boucle fermée hautement anticipatifs.""",

        "ecologia": """# Domaine Scientifique : Écologie des Systèmes et Dynamique des Populations

## 1. Contexte Scientifique et Défi Écologique
Les écosystèmes naturels subissent des **changements de régime catastrophiques** (ex. eutrophisation des lacs, désertification, effondrement des pêcheries) déclenchés par des facteurs de stress stochastiques et des interactions trophiques non linéaires. Prédire ces effondrements avant que l'écosystème ne franchisse un point de non-retour (hystérésis) est primordial pour la conservation de l'environnement.

## 2. Le Comportement de Tau Systémique
Dans le domaine de l'écologie mathématique, **Tau Systémique (τ_s)** sert de capteur précis de la résilience structurelle. Il n'analyse pas les densités de population de manière isolée ; il examine plutôt le réseau **d'interdépendances ordinales** entre les espèces (ex. phyto/zooplancton) et les facteurs abiotiques (ex. température, phosphore).

Avant un effondrement écologique, les écosystèmes subissent un grave déclin de leur "connectivité synergique". τ_s perçoit comment les micro-états du réseau trophique perdent leur hétérogénéité structurelle. Le paramètre **excess3** documente mathématiquement l'érosion de la résilience de l'écosystème, identifiant le seuil critique où les interactions stabilisatrices sont submergées par des rétroactions positives déstabilisatrices.

## 3. Limites des Métriques Conventionnelles
- **Variance Spatiale et Autocorrélation (EWS Classiques) :** Génèrent fréquemment des faux positifs induits par le bruit environnemental (climatique) et reposent de manière critique sur l'hypothèse de *Critical Slowing Down* (CSD), qui peut ne pas être valable dans des réseaux écologiques complexes.
- **Biomasse Agrégée :** Un indicateur retardé qui ne reflète l'altération qu'une fois l'effondrement trophique devenu irréversible.
- **Tau Systémique (τ_s) :** Étant invariant aux transformations monotones (immunisé contre certaines fluctuations abiotiques), il isole exclusivement la désintégration de la logique relationnelle sous-jacente de l'écosystème.

## 4. Impact sur la Conservation
L'intégration du cadre RECD donne aux écologues computationnels les moyens d'établir des signaux d'alerte précoce hautement calibrés, protégeant ainsi les écosystèmes fragiles grâce à des fondements topologiques rigoureux.""",

        "finanzas": """# Domaine Scientifique : Éconophysique et Marchés Financiers

## 1. Contexte Scientifique et Défi Économique
Les marchés financiers mondiaux présentent les comportements caractéristiques des systèmes complexes fortement couplés. Les crises de liquidité et les *flash crashes* représentent des transitions de phase entraînées par des dynamiques spéculatives et le trading algorithmique à haute fréquence. Anticiper ces perturbations exige de transcender le paradigme classique de la variance stochastique.

## 2. Le Comportement de Tau Systémique
Au sein de l'éconophysique, **Tau Systémique (τ_s)** mesure la **rigidité topologique** des flux de capitaux. Plutôt que d'évaluer les rendements isolés, il examine la co-évolution ordinale à travers de multiples actifs ou indices financiers (ex. S&P 500, VIX, bons du Trésor).

Avant un effondrement systémique du marché, il se produit une "cristallisation" des dépendances inter-actifs. τ_s détecte la manière dont le système financier entre dans un état d'hyper-synchronisation ordinale. La perte abrupte de degrés de liberté et la dissolution de la synergie de diversification (observée via la contraction de **excess3**) servent de précurseur mathématique au krach financier.

## 3. Limites des Métriques Conventionnelles
- **Volatilité (VIX / GARCH) :** Mesure la dispersion des rendements, mais agit historiquement comme un indicateur coïncident ou réactif, dépourvu de véritable pouvoir d'anticipation.
- **Corrélation de Pearson :** Ne capture que les relations linéaires et s'effondre complètement face à la structure fractale et aux queues épaisses (fat tails) des distributions de rendements des actifs.
- **Tau Systémique (τ_s) :** Totalement affranchi des hypothèses distributionnelles. En opérant dans l'espace symbolique de Bandt-Pompe, il résiste aux valeurs aberrantes (*outliers*) et s'avère capable de détecter l'architecture causale qui orchestre la panique du marché.

## 4. Pertinence Financière
L'implémentation du cadre RECD dote les analystes quantitatifs et les chercheurs financiers d'une instrumentation de nouvelle génération pour auditer le risque systémique, offrant des signaux d'alerte précoce ancrés dans la thermodynamique des systèmes loin de l'équilibre."""
    }
}

for lang, domains in CONTENT.items():
    base_path = f"content/{lang}/dominios"
    os.makedirs(base_path, exist_ok=True)
    for domain, text in domains.items():
        with open(f"{base_path}/{domain}.md", "w", encoding="utf-8") as f:
            f.write(text)

print("Domain narratives successfully generated.")
