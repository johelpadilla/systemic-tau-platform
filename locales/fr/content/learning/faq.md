# Foire aux questions (réponses approfondies)

Ces réponses ciblent de vrais malentendus de 3e cycle et de relecture par les pairs — pas une FAQ marketing.

---

## A. Concepts

### Le Tau systémique n’est-il qu’un Kendall tau avec du marketing ?

Non. La parenté avec les statistiques de rangs est réelle dans le **substrat ordinal**, mais l’objet de τ_s est la **dynamique de réorganisation du couplage** en fenêtres, souvent multi-échelle et liée au RECD. Une corrélation de rangs statique ne définit ni une horloge ni les niveaux Φ₁–Φ₃.

### En quoi diffère-t-il de la Transfer Entropy ?

| | Transfer Entropy | τ_s + RECD / excess3 |
|--|------------------|----------------------|
| Question | Combien A améliore-t-il la prédiction de B ? | Comment la structure ordinale conjointe se réorganise-t-elle et fait-elle avancer l’horloge ? |
| Direction | Explicitement directionnelle | Relationnelle / synergique (pas un graphe causal) |
| Usage v1.0 | Horizon Full | Noyau du Lab |

Ils sont **complémentaires**. Ne substituez pas l’un à l’autre dans un article sans justifier la question.

### Pourquoi Bandt–Pompe plutôt que SAX ou d’autres symboles ?

Parsimonie, invariance monotone et écosystème mature (entropie de permutation, articles du paradigme). SAX et d’autres alphabets sont des extensions possibles ; ce ne sont **pas** le standard du pilote CCTP ni le noyau v1.0.

### Qu’est-ce que le « signe dépendant du contexte » ?

Cela signifie que **Δτ_s ou Δexcess3 peuvent monter ou baisser** vers un événement selon le régime (p.ex. FA, pacing, phase d’épidémie). La preuve se joue sur : (1) magnitude du changement, (2) concordance des métriques, (3) p-valeurs sous surrogates, (4) récit de domaine — pas un panneau universel « toujours positif = mauvais ».

---

## B. Données et pratique

### Puis-je utiliser une seule variable ?

Le noyau est multivarié (N≥2). Avec une série, la plateforme construit le proxy  
X=[z(x), z(|Δx|)]. C’est un pont éducatif légitime, pas un laissez-passer pour toute claim univariée.

### Combien de surrogates ?

Mode Fast : peu (exploration). Full : plus. Rapportez n, méthode (phase-shuffle / IAAFT), seed et la coupure d’événement.

### Et le TDA et la Breathing Window ?

**Extensions** opérationnelles du Lab. Activez-les en Full ou via cases ; lisez-les dans l’onglet Extensions. Elles ne **remplacent pas** τ_s + RECD + EWS + surrogates.

---

## C. Éthique et citation

### Puis-je clamer une maturité clinique ou opérationnelle ?

Non pour les claims produit v1.0. La cardiologie est l’ancre empirique (CCTP/SDDB) ; les autres domaines priorisent pédagogie et transfert. Bornez chaque claim.

### Comment citer ?

Citez l’article/pilote empirique pour les claims cardiaques ; pour les démos, indiquez « démo synthétique / domain-like pédagogique » et joignez Methods + hash de repro.
