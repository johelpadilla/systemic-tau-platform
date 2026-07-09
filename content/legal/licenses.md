# Licencias y uso

## Software de la plataforma

- Licencia **MIT** (ver `LICENSE` en la raíz del repositorio).
- Autor: Johel Padilla-Villanueva (ORCID [0000-0002-5797-6931](https://orcid.org/0000-0002-5797-6931)).
- Repositorio: https://github.com/johelpadilla/systemic-tau-platform
- Contacto: johel.padilla@upr.edu

## Datos de terceros y demos incluidos

| Fuente | Qué incluye STP | Condición |
|--------|-----------------|-----------|
| PhysioNet **SDDB** | CSV demo `sddb_rr_38_demo.csv`, `sddb_rr_51_demo.csv` — **RR derivado/procesado** para pedagogía (no archivos `.dat` crudos) | Cumplir [PhysioNet Credentialed Health Data Use Agreement / ToS](https://physionet.org/); **citar** la base SDDB y el paper de dominio; no presentar los demos como diagnóstico clínico |
| Generadores sintéticos STP | Series logistic / AR / dengue-like / EEG-like / etc. | MIT vía este software; uso libre con cita de la plataforma |
| DengAI / open challenges | Solo menciones / pipelines educativos (sin redistribuir dumps propietarios) | Según licencia del challenge |
| NTL LTER | Citar data papers; respetar política de uso | No reempacar datos crudos sin permiso |
| Precios de mercado | Demos sintéticos de volatilidad | Uso educativo; no feeds propietarios |

### PhysioNet / SDDB — nota explícita

Los CSV demo **no son una redistribución de la base completa SDDB**. Son extracciones de intervalos RR ya limpiados/exportados para reproducir el flujo del laboratorio y del piloto CCTP. Quien publique resultados debe:

1. Citar PhysioNet y la referencia SDDB correspondiente.
2. Citar el preprint/paper CCTP o del dominio usado.
3. No reclamar equivalencia con el acceso credentialed a PhysioNet ni uso clínico.

## Privacidad de uploads en el Lab web

- Procesamiento en **sesión** (memoria del proceso Streamlit).
- **Sin** base de datos de uploads en v1.0.
- **Sin** reentrenamiento de modelos con datos del usuario.
- No suba PHI/PII ni secretos a despliegues públicos.

## Citación mínima

Al publicar resultados obtenidos con la plataforma, cite:

1. El preprint/paper del dominio.
2. Esta plataforma: *Systemic Tau Platform* v1.0 (MIT), https://github.com/johelpadilla/systemic-tau-platform
3. El dataset original (p.ej. PhysioNet SDDB).
4. Opcional: `systemictau` / `nested-recd` si se usaron como motor.

## Disclaimer

No es un dispositivo médico. No es consejo de inversión. No es un sistema de diagnóstico. Resultados requieren validación científica independiente antes de uso operativo.
