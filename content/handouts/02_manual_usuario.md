# Systemic Tau Platform — Manual de usuario

**Audiencia:** estudiantes, docentes, investigadores que usan la app local  
**Versión:** v1.0  
**Alcance:** interfaz Streamlit + CLI `stp`

---

## 1. Instalación y arranque

### Requisitos

- Python 3.10+ recomendado  
- Entorno virtual  
- Dependencias del proyecto (`pip install -e .` o `requirements.txt`)

### Arranque de la interfaz

Desde la raíz del repositorio:

```bash
streamlit run app/Home.py
# o
stp serve
```

Abra la URL local que imprime Streamlit (por defecto `http://localhost:8501`).

### Nota sobre actualizaciones del código

Si edita el paquete `stp` mientras Streamlit corre, recargue la página o reinicie el servidor. El bootstrap de la app prioriza el `src/` del repositorio para evitar instalaciones editables obsoletas.

---

## 2. Mapa de la aplicación

| Página | Función pedagógica |
|--------|-------------------|
| **Home** | Portada, valor del núcleo, deep-links |
| **Fundamentos** | Teoría τ_s, límites EWS, RECD, excess3, CSD, filosofía |
| **Matemática** | Mapa formal + sandbox Bandt–Pompe |
| **Dominios** | Madurez empírica + textos por dominio + link al Lab |
| **Laboratorio** | Pipeline completo y exportaciones |
| **Ruta de aprendizaje** | Secuencia, glosario, FAQ en pantalla |
| **Evidencia** | Cohorte de referencia CCTP / demos |
| **Docencia** | Syllabus 6 semanas y rúbrica |
| **Materiales** | Descargas (este manual y el resto de handouts) |

La pestaña de planes comerciales **no** forma parte del núcleo educativo v1.0.

---

## 3. Laboratorio — flujo paso a paso

### 3.1 Cargar datos

Tres vías:

1. **Catálogo** — demos sintéticos y samples SDDB (cuando existen en `data/samples/`).  
2. **CSV propio** — columnas numéricas; el adapter de dominio sugiere variables.  
3. **Deep-link** desde Dominios / Home (`?dataset=...&domain=...`).

Cada entrada del catálogo puede traer:

- `domain` y preset (W, stride, m, θ₃)  
- `event_index` o `event_fraction` (corte pre/post)  
- `variables` y `ground_truth` de diseño (en demos)

### 3.2 Roles y evento

- Elija el **dominio** (cardiología, epidemiología, clima, educación, …).  
- Marque un **índice de evento** si conoce el onset (VF, brote, sequía, mitad de curso…).  
- Sin evento, el Lab usa partición **1ª mitad vs 2ª mitad** (diseño exploratorio: declárelo).

### 3.3 Parámetros

| Parámetro | Rol |
|-----------|-----|
| `window` (W) | Longitud de la ventana de τ_s |
| `stride` | Paso entre ventanas |
| `m`, `delay` | Embedding Bandt–Pompe (v1.0 típico: m=3, delay=1) |
| `theta3` | Umbral de Φ₃ |
| `n_surrogates` | Réplicas del nulo (0 = sin p_surr) |
| `surrogate_method` | `phase_shuffle` (default) o `iaaft` |
| `mode` | `fast` (clase) / `full` (más coste) |
| Breathing / memoria | Opcionales; no bloquean el núcleo |

**Regla docente:** empiece por el **preset del dominio**; documente cualquier desvío.

### 3.4 Ejecutar e interpretar

Tras **Analizar**:

1. Series con marcador de evento.  
2. Trayectoria τ_s.  
3. Panel RECD / excess3.  
4. Panel EWS clásicas (control).  
5. Lectura dual (plantilla, sin LLM).  
6. Métricas: Δτ_s, Δexcess3, p_surr, hash.

### 3.5 Exportar

| Archivo | Contenido |
|---------|-----------|
| Reporte `.md` | Narrativa + métricas + métodos |
| `result.json` | Series y métricas serializables |
| Methods | Párrafo listo para papers / entregas |

Conserve siempre el **repro_hash**: fija parámetros + huella de los datos de la corrida.

---

## 4. Catálogo de demos (orientación)

| ID | Dominio | Para enseñar… |
|----|---------|----------------|
| `synthetic_coupled_logistic` | sintético | Señal fuerte de acoplamiento |
| `synthetic_ar_noise` | sintético | Control casi-nulo |
| `cardiac_like_demo` / `sddb_rr_*` | cardiología | Proxy CCTP / sample real |
| `dengue_like_demo` | epidemiología | Brote + clima |
| `eeg_like_demo` | neurociencia | Lock-in de canales |
| `ecology_like_demo` | ecología | Bloom / nutrientes |
| `climate_drought_demo` | clima | Régimen de sequía |
| `education_cohort_demo` | educación | Cohorte / aula |
| `social_polarization_demo` | social | Polarización (juguete) |
| `sleep_fragmentation_demo` | fisiología | Fragmentación circadiana |
| `finance_like_demo` | finanzas | Régimen de vol (no trading) |

Los demos sintéticos tienen **ground truth de diseño**. No los presente como evidencia empírica del dominio real.

---

## 5. CLI

```bash
# Análisis batch
stp analyze ruta/datos.csv \
  --domain epidemiology \
  --window 13 --stride 1 \
  -o salida/reporte.md \
  --json salida/resultado.json

# Servir la UI
stp serve
```

Consulte `stp analyze -h` para flags actualizados.

---

## 6. Buenas prácticas de reproducibilidad

1. Fije `seed` cuando use surrogates.  
2. Exporte MD + JSON de corridas que cite.  
3. Cite dataset original (PhysioNet, etc.) además del software.  
4. No reutilice un hash de un demo sintético como si fuera cohorte clínica.  
5. Si actualiza código, vuelva a correr y compare hashes.

---

## 7. Solución de problemas frecuentes

| Síntoma | Qué revisar |
|---------|-------------|
| `ImportError` de símbolos STP | Reinstalar `pip install -e .` y reiniciar Streamlit |
| Página en blanco / error de import | Recarga dura; bootstrap debe apuntar a este repo |
| Δτ_s ≈ 0 en todo | ¿Control AR? ¿W demasiado grande? ¿Una sola variable mal elegida? |
| Φ₃ siempre 0 | Normal con ruido; mire **excess3** continuo |
| p_surr inestable | Suba n_surr; fije seed; no use n=2 para claims |
| CSV no carga | Columnas no numéricas; encoding; faltan ≥2 series útiles |

---

## 8. Límites éticos (resumen)

- Investigación y **docencia**, no certificación clínica/operativa.  
- Dominios no cardio: madurez distinta; no extrapole la fuerza del piloto CCTP.  
- Datos de terceros: cumplan sus licencias (PhysioNet, LTER, …).

Detalle: handout *Ética y alcance*.

---

*STP Manual de usuario · material descargable para cursos y autoestudio.*
