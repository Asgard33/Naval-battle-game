# 🚢 Jeu de Bataille Navale

Jeu de bataille navale implémenté en Python, intégrant une IA suivant sur une stratégie hunt-and-target, plusieurs modes de jeu (IA vs IA, joueur vs IA) et une architecture modulaire.

## Fonctionnalités

- Gameplay classique de bataille navale
- IA aléatoire (IA)
- IA avancée basée sur une stratégie hunt-and-target (IA+)
- Plusieurs modes de jeu :
    - Joueur vs Joueur
    - Joueur vs IA+
    - IA+ vs IA+
    - IA+ vs IA (pour mettre en évidence les différences de performance)
- Structure du code modulaire et lisible

---

## Stratégie de l'IA

L'IA utilise une approche heuristique pour prendre ses décisions :

- Priorise les cases en fonction des touches précédentes
- Cible les cases voisines après une touche réussie
- Évite les cases déjà jouées
- Utilise une combinaison de règles pour simuler un jeu stratégique

---

## Origine du projet

Ce projet est basé sur un projet académique de groupe développé en 2023.
Version originale disponible ici : https://github.com/Ruby44444/Bataille-Navale

Dans ce projet, j'ai personnellement :

- Conçu et implémenté une IA heuristique avancée (IA+) basée sur une stratégie hunt-and-target :
  - Phase de recherche aléatoire sans répétition
  - Phase de ciblage après détection d'un navire
- Implémenté la logique de placement des navires (manuelle et automatique)

J'ai également intégré la logique de l'IA dans la boucle de jeu principale (`naval_battle`).

---

## Améliorations et refactorisation

J'ai amélioré le projet original en :

- Supprimant les modes de jeu inutiles pour améliorer la clarté et l'expérience utilisateur
- Ajoutant quelques fonctionnalités pour améliorer l'expérience utilisateur
- Restructurant le code pour mieux séparer le gameplay et la simulation
- Ajoutant un mode simulation avec export des données en CSV pour l'analyse des performances

---

## 📊 Résultats

- L'IA+ surpasse significativement l'IA aléatoire
- La stratégie heuristique améliore l'efficacité des touches
