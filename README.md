# CESI — Supports de cours & exercices

<p align="center">
  <strong>Un seul dépôt pour tous les supports de cours CESI</strong>
</p>

---

Ce dépôt regroupe des **supports de cours**, **exercices**, **sujets** et **templates** utilisés en formation au CESI. Tout est regroupé ici pour que les étudiants puissent retrouver facilement les bases de travail, les énoncés et les projets de fin de module.

---

## Contenu

| Dossier | Description |
|--------|-------------|
| **INFAL26_Introduction_aux_Api** | Introduction aux API REST — squelette d’API Express, CRUD utilisateurs, sujet dans `SUJET.md` |
| **INFAL26_Exercice_TS** | Exercice TypeScript — POO (interfaces, classes, voitures), tests à lancer avec `pnpm test` |
| **INFAL26_Exercice_REACT** | Exercice React — liste de tâches, `useState`, composants ; `pnpm start` / `pnpm test` |
| **INFAL26_Exercice_JS** | Exercice JavaScript — POO (gestion d’un zoo), tests avec `npm run test` |
| **INFRAL26_DBSqlite** | Base SQLite pour le projet Pokédex (module INFRAL26) — fichier `PAL.db` + README |
| **Pong-EduGames** | Projet Pong (INFAL135) — Pygame + API FastAPI, scores en JSON |
| **pokenative** | Template Expo (React Native) — projet de fin de cours mobile (module INF25), Expo Router, TypeScript |

Chaque dossier contient le code, les sujets (quand il y en a) et un README pour démarrer.

---

## Pour les étudiants

- **Exercices** : ouvrez le dossier de l’exercice, lisez le README ou le fichier de sujet, installez les dépendances (`pnpm install` ou `npm install` selon le projet), puis lancez les tests ou l’application comme indiqué.
- **Templates / starters** : copiez le dossier qui vous intéresse et travaillez dessus pour votre projet (ex. `pokenative` pour une app mobile).
- **Supports de cours** : ce sont les bases fournies par le formateur ; vous pouvez les cloner ou les télécharger depuis ce dépôt.

---

## Structure du dépôt

```
.
├── INFAL26_Introduction_aux_Api/   # API REST (Express)
├── INFAL26_Exercice_TS/            # Exercice TypeScript
├── INFAL26_Exercice_REACT/         # Exercice React
├── INFAL26_Exercice_JS/            # Exercice JavaScript
├── INFRAL26_DBSqlite/              # BDD SQLite Pokédex
├── Pong-EduGames/                  # Pong Pygame + FastAPI
├── pokenative/                     # Template Expo React Native
├── repos.txt                       # Liste des dépôts d’origine (archivés)
├── scripts/                        # Utilitaires (ex. clone-repos.sh)
└── README.md                       # Ce fichier
```

---

*Support de cours et exercices — formation CESI.*
