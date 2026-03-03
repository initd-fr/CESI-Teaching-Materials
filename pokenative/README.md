# Pokenative — Starter Développement d'application mobile (CESI)

Starter pédagogique pour le module **Développement d'application mobile** au CESI. Les étudiants peuvent s’en servir à leur convenance pour réaliser leur **projet de fin de cours**. Base fournie : application **Expo** (React Native) cross-platform (iOS, Android, web), **Expo Router**, **TypeScript** strict, New Architecture. Un écran d’accueil placeholder ; la stack (navigation, Reanimated, Haptics, WebView) est en place. Pas de sujet imposé — chacun construit son projet à partir de cette base (voir [SUJET.md](./SUJET.md)).

---

## 1. Contexte

**Problème adressé :** en formation, éviter de perdre du temps sur la configuration (Expo, Metro, Babel, routing). Ce starter fournit une base opérationnelle : Expo Router, layouts, TypeScript, dépendances déjà choisies (Reanimated, Safe Area, etc.). Les étudiants l’utilisent librement pour leur projet de fin de cours — écrans, navigation, intégration API selon leur propre cahier des charges. Pas de sujet unique imposé.

---

## 2. Stack technique

| Couche               | Technologie                                                         |
| -------------------- | ------------------------------------------------------------------- |
| Framework            | React 18, React Native 0.76                                         |
| Toolchain            | Expo SDK 52                                                         |
| Routing / Navigation | Expo Router 4 (file-based), React Navigation 7 (Stack, Bottom Tabs) |
| Langage              | TypeScript 5 (strict)                                               |
| UI / UX              | expo-blur, expo-haptics, expo-splash-screen, expo-status-bar        |
| Animations           | react-native-reanimated, react-native-gesture-handler               |
| Plateformes          | iOS, Android, Web (Metro, static export)                            |
| Build                | New Architecture (React Native) activée                             |

---

## 3. Architecture

```
├── app/
│   ├── _layout.tsx      # Layout racine : Stack (Expo Router)
│   └── index.tsx        # Écran d’accueil (placeholder)
├── assets/             # Images (icon, splash, adaptive-icon, favicon)
├── app.json             # Config Expo (slug, scheme, plugins, experiments.typedRoutes)
├── package.json
└── tsconfig.json       # Alias @/* → ./*
```

- **Expo Router** : une route par fichier sous `app/`. `_layout.tsx` définit le layout (Stack) et les écrans sont déclarés par les fichiers (ex. `index.tsx` → `/`).
- **Navigation** : React Navigation est utilisé sous le capot par Expo Router ; possibilité d’ajouter des ongles (Bottom Tabs) ou des stacks imbriqués via des dossiers et layouts.
- **Typed routes** : `experiments.typedRoutes` dans `app.json` pour des routes typées (Expo Router).

---

## 4. Choix techniques et justifications

| Choix                        | Justification                                                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Expo (managed workflow)      | Démarrage rapide, builds EAS possibles plus tard, pas de natif à maintenir à la main au début.                         |
| Expo Router                  | Routing déclaratif par fichiers, aligné avec les usages modernes (Next.js-like), deep linking et scheme configurables. |
| TypeScript strict            | Réduction des bugs et meilleure maintenabilité ; alias `@/*` pour des imports propres.                                 |
| New Architecture             | Préparer la base pour les perfs et les patterns futurs (Fabric, TurboModules) si besoin.                               |
| Reanimated + Gesture Handler | Déjà présents pour animations et gestes dès qu’un écran interactif sera ajouté.                                        |
| Web (Metro, static)          | Une seule codebase pour mobile et web ; export statique possible pour hébergement web.                                 |

---

## 5. Points complexes / challenges techniques

- **Cross-platform** : gérer les différences iOS / Android / Web (Safe Area, statut bar, clavier) ; `react-native-safe-area-context` et `expo-status-bar` sont déjà en dépendances.
- **Routing et deep linking** : scheme `myapp` dans `app.json` ; à compléter selon le besoin (universal links, intent Android).
- **Évolution vers EAS Build** : le projet est prêt pour des builds natifs (EAS) et des profils (dev, preview, production) sans changement majeur.

---

## 6. Sécurité / performance

- Aucune donnée sensible ni clé en dur dans le repo ; les variables d’environnement (ex. API) iront dans `.env` (fichiers `.env*.local` déjà ignorés).
- Pas d’auth ni de couche réseau implémentées pour l’instant ; à ajouter au moment de l’intégration API.
- Performance : New Architecture activée ; Reanimated pour les animations côté natif quand elles seront utilisées.

---

## 7. Déploiement / infra

- **Dev local** : `npm install` puis `npx expo start` (Expo Go, simulateur iOS/Android, ou web).
- **Scripts** : `npm run android`, `npm run ios`, `npm run web` pour cibler une plateforme.
- **Build natif / EAS** : non configuré dans ce repo ; ajout possible via `eas.json` et EAS Build pour binaires et stores.

---

## Pour les participants (CESI)

**[SUJET.md](./SUJET.md)** décrit le contenu du starter et comment le lancer. Ce dépôt est une base à votre disposition pour réaliser votre projet de fin de cours ; vous l’utilisez et l’adaptez à votre convenance.

**Démarrage rapide :** `npm install` → `npx expo start`. Puis Expo Go (QR code), simulateur iOS/Android ou web.
