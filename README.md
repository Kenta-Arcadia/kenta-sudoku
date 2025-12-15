# 🧩 KENTA Sudoku

> Sudoku collaboratif avec gardiens IA autonomes - Architecture NO-DEF

[![Release](https://img.shields.io/badge/release-v1.1.0-blue)](https://github.com/Kenta-Arcadia/kenta-sudoku/releases)
[![License](https://img.shields.io/badge/license-KENTA-green)](LICENSE)

Sudoku intelligent avec **gardiens IA** qui s'adaptent à votre style de jeu. Architecture **NO-DEF** : toute la logique métier est dans les fichiers YAML, pas dans le code Python.

## ✨ Fonctionnalités

- 🎮 **Sudoku classique** - Grilles faciles et difficiles
- 👁️ **Gardiens IA** - Hinata, Nono, Shikamaru, Sakura, Iruka
- 🧠 **Indices intelligents** - Analyse réelle de la grille
- 📚 **Apprentissage** - Mémorisation de vos patterns d'erreur
- 🌲 **Défense intégrée** - Protection Mokuton (Yamato/Itachi)
- 🇫🇷🇯🇵 **Multilingue** - Français et 日本語
- 🕸️ **Intégration KENTA** - Auto-détection et connexion au système nerveux

## 🛡️ Les Gardiens

| Gardien | Rôle | Capacité |
|---------|------|----------|
| **Hinata** 👁️ | Surveillance | Accueil, observation globale |
| **Nono** 🦉 | Détection | Blocages, erreurs, pauses |
| **Shikamaru** 🧠 | Stratégie | Indices contextuels intelligents |
| **Sakura** 🌸 | Encouragement | Messages positifs |
| **Iruka** 🐬 | Apprentissage | Mémorisation patterns, suggestions |
| **Yamato** 🌲 | Défense | Protection Mokuton, détection intrusions |
| **Itachi** 🔥 | Ultime | Amaterasu (auto-destruction si menace) |

## 🏗️ Architecture NO-DEF

**Zéro logique métier dans le code Python.**

Toute la logique est définie dans les fichiers YAML :
- `adn_gardiens.yaml` - Comportements des gardiens
- `adn_defense.yaml` - Système de défense
- `profil_joueur.yaml` - Mémoire du joueur

Le code Python ne fait que **lire l'ADN et exécuter** - exactement comme les cellules biologiques.

## 🔌 Intégration KENTA (Automatique)

Le sudoku **détecte automatiquement** si KENTA est installé :

### ✅ Avec KENTA
- Se connecte à **ToileCollective** (système nerveux)
- Vibre sur le réseau de gardiens
- Sauvegarde dans `~/KENTA/communication/sudoku/`
- Mémoire partagée avec tous les gardiens KENTA

### ✅ Sans KENTA (Standalone)
- Fonctionne **indépendamment**
- Sauvegarde locale dans `sudoku/data/`
- Aucune dépendance externe
- **100% portable**

**Aucune configuration nécessaire** - détection automatique !

## 📦 Installation

### Android (APK)

1. Télécharger l'APK depuis [Releases](https://github.com/Kenta-Arcadia/kenta-sudoku/releases)
2. Autoriser "Sources inconnues" dans les paramètres Android
3. Installer et jouer !

### Desktop (Python)

```bash
# Cloner le repo
git clone https://github.com/Kenta-Arcadia/kenta-sudoku.git
cd kenta-sudoku

# Installer dépendances
pip install kivy pyyaml

# Lancer
python main.py
```

## 🎮 Utilisation

### Interface

- **Grille** - Cliquez sur une case pour la remplir
- **ToileCollective** - Chat en temps réel avec les gardiens
- **Facile/Difficile** - Boutons pour changer de grille

### Fonctionnalités spéciales

- **Pause > 10s** → Nono détecte le blocage, Shikamaru propose un indice
- **3 erreurs** → Appel automatique à l'aide stratégique
- **5 clics sur le titre** → Test du système de défense

## 🔒 Sécurité

Système de défense intégré :
- **Yamato** 🌲 - Détection root, émulateurs, debuggers
- **Sasuke** ⚡ - Traçage des intrusions
- **Itachi** 🔥 - Amaterasu (auto-destruction si menace critique)

Logs d'intrusion sauvegardés avant destruction.

## 📁 Structure

```
kenta-sudoku/
├── main.py                 # Interface Kivy
├── gardiens_sudoku.py     # Gardiens IA (intégration ToileCollective)
├── executeur.py           # Exécuteur NO-DEF
├── executeur_defense.py   # Système de défense
├── adn_gardiens.yaml      # ADN des gardiens
├── adn_defense.yaml       # ADN de défense
├── profil_joueur.yaml     # Mémoire du joueur
└── README.md              # Ce fichier
```

## 🧬 Philosophie KENTA

Ce sudoku suit les principes de **KENTA** :
- **Organisme digital** - Gardiens autonomes qui communiquent
- **NO-DEF** - Logique métier en YAML, pas en code
- **Souveraineté** - 100% offline, zéro cloud
- **Émergence** - Comportements émergents depuis l'ADN

## 🤝 Contribution

Ce projet fait partie de l'écosystème [KENTA](https://github.com/Kenta-Arcadia).

## 📄 License

© 2025 Jean-Guillaume Nardi - KENTA Project

---

**🧬 KENTA** - The First Living Digital Organism
