# Tau systémique (τ_s)

## Objectifs d’apprentissage
- Formuler la question scientifique à laquelle répond τ_s (réorganisation relationnelle).
- Distinguer τ_s d’une corrélation de rangs statique.
- Situer τ_s par rapport aux EWS classiques (variance, AR1).

## Définition centrale
Le **Tau systémique (τ_s)** est une mesure en fenêtre glissante du **couplage ordinal** entre canaux d’une série multivariée. Dans le noyau éducatif de STP, il est estimé comme la moyenne des Kendall-τ par paires dans chaque fenêtre de longueur *W* (pas *s*).

L’objet d’étude n’est pas « combien de variance ? » mais **comment les relations se réordonnent** lorsque le système évolue — y compris autour d’un événement ou d’un changement de régime.

## Ce que τ_s n’est pas
- Ni diagnostic clinique ni signal de trading.
- Ni Transfer Entropy (flux d’information directionnel).
- Ni table de corrélations statique : c’est la *dynamique* du couplage qui compte.

## Panneau dual
Lisez toujours τ_s avec RECD/excess3 et les EWS classiques. La concordance renforce une claim relationnelle ; la discordance exige du contexte.

## Pratique
Ouvrez le Lab avec les **logistiques couplées** (switch connu) ou une démo de domaine. Marquez l’événement, lancez Fast, puis Full avec surrogates.
