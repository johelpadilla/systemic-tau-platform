# Licences et usage

## Logiciel de la plateforme

- Licence **MIT** (voir `LICENSE` à la racine du dépôt).
- Auteur : Johel Padilla-Villanueva (ORCID [0000-0002-5797-6931](https://orcid.org/0000-0002-5797-6931)).
- Dépôt : https://github.com/johelpadilla/systemic-tau-platform
- Contact : johel.padilla@upr.edu

## Données tierces et démos incluses

| Source | Ce que STP fournit | Condition |
|--------|--------------------|-----------|
| PhysioNet **SDDB** | CSV démo `sddb_rr_38_demo.csv`, `sddb_rr_51_demo.csv` — **RR dérivé/traité** à des fins pédagogiques (pas de fichiers `.dat` bruts) | Respecter les [ToS / accords PhysioNet](https://physionet.org/) ; **citer** SDDB et l'article du domaine ; ne pas présenter les démos comme diagnostic clinique |
| Générateurs synthétiques STP | Séries logistic / AR / dengue-like / EEG-like / etc. | MIT via ce logiciel ; usage libre avec citation de la plateforme |
| DengAI / challenges ouverts | Mentions / pipelines éducatifs uniquement | Selon la licence du challenge |
| NTL LTER | Citer les data papers ; respecter la politique d'usage | Ne pas reconditionner les données brutes sans autorisation |
| Prix de marché | Démos synthétiques de volatilité | Usage éducatif ; pas de flux propriétaires |

### PhysioNet / SDDB — note explicite

Les CSV démo **ne constituent pas** une redistribution de la base SDDB complète. Ce sont des exports RR nettoyés pour reproduire le flux du Lab et la grammaire du pilote CCTP. Quiconque publie des résultats doit :

1. Citer PhysioNet et la référence SDDB pertinente.
2. Citer le preprint/article CCTP ou du domaine utilisé.
3. Ne pas revendiquer l'équivalence avec l'accès credentialed PhysioNet ni un usage clinique.

## Confidentialité des uploads du Lab web

- Traitement en **session** (mémoire du processus Streamlit).
- **Pas** de base de données d'uploads en v1.0.
- **Pas** de réentraînement de modèles sur les données utilisateur.
- N'envoyez pas de PHI/PII ni de secrets sur les déploiements publics.

## Citation minimale

En publiant des résultats obtenus avec la plateforme, citez :

1. Le preprint/article du domaine.
2. Cette plateforme : *Systemic Tau Platform* v1.0 (MIT), https://github.com/johelpadilla/systemic-tau-platform
3. Le jeu de données original (p.ex. PhysioNet SDDB).
4. Optionnel : `systemictau` / `nested-recd` s'ils ont servi de moteur.

## Avertissement

Ce n'est pas un dispositif médical. Ce n'est pas un conseil d'investissement. Ce n'est pas un système de diagnostic. Les résultats exigent une validation scientifique indépendante avant usage opérationnel.
