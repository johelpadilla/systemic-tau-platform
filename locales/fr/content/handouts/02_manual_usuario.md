# Manuel utilisateur

## Installation
```bash
cd systemic-tau-platform
python -m venv .venv && source .venv/bin/activate
pip install -e .
streamlit run app/Home.py
```

## Carte
Accueil · Fondements · Mathématiques · Domaines · Lab · Parcours · Preuves · Enseignement · Matériels.

## Langue
Barre latérale **Langue** : Español (source) · English · Français. Toute l’UI et le contenu éducatif suivent la sélection.

## Étapes du Lab
1. Données (catalogue / CSV) 2. Paramètres 3. Exécuter 4. Résultats + export.

## CLI
```bash
stp analyze data.csv --domain cardiology --breathing --tda -o report.md
stp serve
```

## Dépannage
Erreurs d’import : réinstallez le paquet éditable ; hard-refresh Streamlit. CSV univarié : proxy automatique [x, |Δx|].
