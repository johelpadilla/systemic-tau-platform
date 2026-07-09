import re
import os

path = "app/locales.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Add keys to ES
es_injection = """
        "footer_text": "<strong>Systemic Tau Platform</strong> · v1.0 · Alineado con <em>systemictau</em>, <em>nested-recd</em> y CCTP/SDDB",
        "footer_disclaimer": "<strong>Descargo de responsabilidad:</strong> Esta plataforma es estrictamente para fines educativos y de investigación. No está destinada para uso clínico o diagnóstico médico. <br/><strong>Contacto:</strong> Johel Padilla-Villanueva (johel.padilla@upr.edu)",
"""
content = content.replace('"es": {', '"es": {' + es_injection)

# Add keys to EN
en_injection = """
        "footer_text": "<strong>Systemic Tau Platform</strong> · v1.0 · Aligned with <em>systemictau</em>, <em>nested-recd</em> and CCTP/SDDB",
        "footer_disclaimer": "<strong>Disclaimer:</strong> This platform is strictly for educational and research purposes. It is not intended for clinical use or medical diagnosis. <br/><strong>Contact:</strong> Johel Padilla-Villanueva (johel.padilla@upr.edu)",
"""
content = content.replace('"en": {', '"en": {' + en_injection)

# Add keys to FR
fr_injection = """
        "footer_text": "<strong>Systemic Tau Platform</strong> · v1.0 · Aligné avec <em>systemictau</em>, <em>nested-recd</em> et CCTP/SDDB",
        "footer_disclaimer": "<strong>Avis de non-responsabilité :</strong> Cette plateforme est strictement à des fins éducatives et de recherche. Elle n'est pas destinée à un usage clinique ou à un diagnostic médical. <br/><strong>Contact :</strong> Johel Padilla-Villanueva (johel.padilla@upr.edu)",
"""
content = content.replace('"fr": {', '"fr": {' + fr_injection)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
