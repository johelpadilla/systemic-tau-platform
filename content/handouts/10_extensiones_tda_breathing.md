# Extensiones operativas — Breathing Window y TDA / Betti

**Audiencia:** estudiantes de Lab (semana 3–6) y docentes  
**Estado:** **operativo** en el Lab STP (no “en desarrollo”)  
**Rol:** extensión pedagógica del núcleo τ_s + RECD + EWS + surrogates

---

## 1. Mensaje clave

| Capa | Componentes | ¿Claim principal? |
|------|-------------|-------------------|
| **Núcleo** | τ_s, RECD/excess3, EWS clásicas, surrogates, hash | Sí |
| **Extensiones** | Breathing window, TDA β₀/β₁, memoria ordinal | Complemento / contraste |

El Lab **no depende** de TDA ni breathing para funcionar. Cuando se activan, aparecen en la pestaña **Extensiones**, en el reporte y en Methods.

---

## 2. Breathing window

### Idea

En regímenes volátiles, una W fija grande **suaviza de más** la transición.  
Breathing mapea la **volatilidad local** a un tamaño de ventana impar:

- alta volatilidad → **W más corta** (más reactivo)  
- régimen estable → **W más larga** (más suave)

### Cómo usarlo en el Lab

1. Active **Breathing window** (por defecto en modo Full).  
2. Ejecute.  
3. Pestaña **Extensiones** o el eje secundario en τ_s: serie **W(t)**.  
4. Documente el rango W observado (p.ej. W∈[21–101]).

### Lectura honesta

Breathing cambia la **resolución temporal** de τ_s. No inventa acoplamiento: si el control AR sigue plano, no force una narrativa.

---

## 3. TDA / Betti en ventanas

### Idea

En cada ventana se construye un **point cloud** (delay embedding multivariado) y se resumen números de Betti:

- **β₀** — componentes conexas (¿el cloud se fragmenta o se unifica?)  
- **β₁** — ciclos (estructura “con agujeros” / 1-esqueleto)

### Backends

| Backend | Cuándo | Notas |
|---------|--------|-------|
| **ripser** | Si `pip install systemic-tau-platform[tda]` | Persistencia clásica |
| **VR 1-skeleton** | Siempre (fallback) | β₀ = componentes; β₁ = \|E\|−\|V\|+β₀ |

Ambos son **proxies pedagógicos** de topología del estado. No son un pipeline TDA de producción multi-escala.

### Cómo usarlo en el Lab

1. Active **TDA / Betti**.  
2. Ejecute (cuesta más que solo τ_s; use Fast + TDA en demos cortos o Full).  
3. Pestaña **Extensiones**: curvas β₀(t), β₁(t) + marcador de evento.  
4. Métricas: mean/Δ β₀, β₁ y `tda_backend` en el JSON/reporte.

### Lectura dual ampliada

| Pregunta | Herramienta |
|----------|-------------|
| ¿Se reorganiza el orden compartido? | τ_s, excess3 |
| ¿El panel univariado se mueve? | var / AR1 |
| ¿El cloud de estados cambia de topología? | β₀ / β₁ |
| ¿El Δ relacional es residual bajo nulo cruzado? | p_surr |

**No** reemplace la columna relacional por TDA. Use TDA para **contrastar**: a veces β₁ se mueve cuando var es ambigua; a veces no aporta.

---

## 4. CLI

```bash
# Extensiones on (también default en --mode full)
stp analyze data.csv --domain synthetic --breathing --tda -o report.md --json out.json

stp analyze data.csv --mode full -o report.md
```

---

## 5. Checklist de entrega con extensiones

- [ ] Claim principal basado en τ_s / excess3 / p_surr (+ EWS)  
- [ ] Breathing/TDA declarados como extensión  
- [ ] Backend TDA reportado (`ripser` o `vr_skeleton`)  
- [ ] Rango W si breathing  
- [ ] Hash de la corrida  
- [ ] Sin promesas clínicas/operativas basadas en β₁  

---

## 6. Errores frecuentes

| Error | Corrección |
|-------|------------|
| “TDA aún no está listo” | Está operativo como extensión; actualice la app |
| Publicar solo β₁ | Añada lectura dual del núcleo |
| Confundir fallback VR con ripser multi-escala | Cite el backend |
| Activar TDA en series enorme sin subsample | Use modo Fast o series demo del catálogo |

---

*Handout extensiones STP · Breathing + TDA operativos en el Lab*
