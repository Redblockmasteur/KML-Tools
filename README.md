# KML Tools

## Introduction

**KML Generator** est une application permettant de créer facilement des fichiers KML à partir de coordonnées GPS. Conçue avec une interface intuitive basée sur Tkinter, elle offre une carte interactive pour sélectionner des points et générer des carrés géographiques avec des attributs personnalisés.

L'application est compatible avec **Windows, macOS et Linux** et peut être utilisée directement via un exécutable ou exécutée à partir du code source Python.

---

## Fonctionnalités

- **Carte interactive** : Sélectionnez un point en cliquant sur la carte.
- **Personnalisation** : Définissez la taille du carré, la couleur de la ligne et sa largeur.
- **Données supplémentaires** : Ajoutez des métadonnées au fichier KML.
- **Multilingue** : Disponible en français et en anglais.
- **Interface simple** : Basée sur Tkinter et intégrant `tkintermapview`.

---
![image](https://github.com/user-attachments/assets/74e69eb7-57dd-47e9-8002-92bf858fd1c2)

## 📥 Téléchargement des exécutables

Les versions compilées pour **Windows, macOS et Linux** sont disponibles dans les [releases GitHub](https://github.com/Redblockmasteur/KML-Tools/releases).

### 📌 Windows  
Téléchargez **`KML_Generator.exe`** et exécutez-le.

### 🍏 macOS  
Téléchargez **`KML_Generator.app`**, puis ouvrez-le (**peut nécessiter l'autorisation d'exécution**).

### 🐧 Linux  
Téléchargez **`KML_Generator`**, puis exécutez-le avec :
```sh
chmod +x KML_Generator
./KML_Generator
```
## Exécution depuis Python

Si vous souhaitez exécuter l'application directement depuis le code source, voici les étapes :

### 📌 Prérequis

 - Python 3.10+

 - Dépendances : `tkinter`, `Pillow`, `geopy`, `tkintermapview`, `pyinstaller`

### 📦 Installation des dépendances
```sh
pip install tkinter pillow geopy tkintermapview pyinstaller
```

### ▶️ Lancer l'application
```sh
python square.py
```

### 🛠️ Compilation de l'application

Si vous souhaitez générer l'exécutable par vous-même, voici la procédure avec PyInstaller.

Windows
```sh
pyinstaller --onefile --windowed --icon=logo.ico --name "KML_Generator" square.py

macOS
```sh
pyinstaller --onefile --windowed --icon=logo.icns --name "KML_Generator" square.py
```

Linux
```sh
pyinstaller --onefile --windowed --icon=logo.png --name "KML_Generator" square.py
```

L'exécutable généré sera disponible dans le dossier `dist/`.

### 📂 Structure du projet

```sh
KML-Generator/
│── square.py          # Code source principal
│── logo.ico           # Icône pour Windows
│── logo.icns          # Icône pour macOS
│── logo.png           # Icône alternative
│── README.md          # Documentation du projet
```

# 🤝 Contributions

Les contributions sont les bienvenues ! Vous pouvez proposer des améliorations ou signaler des bugs en ouvrant une issue sur se repo.

# 📜 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser et de le modifier selon vos besoins, tant que vous incluez la mention de copyright originale.

# Crédits

tkinter (inclus dans Python)

tkintermapview (MIT)

Pillow (HSL, équivalent MIT)

geopy (MIT)

PyInstaller (GPLv2)

Données cartographiques :
L'application utilise OpenStreetMap via tkintermapview.

## 🎉 Remerciements

Merci aux développeurs et mainteneurs des bibliothèques open-source utilisées dans ce projet :

 - tkinter → Interface graphique

 - tkintermapview → Gestion de la carte interactive

 - Pillow → Gestion des icônes et images

 - geopy → Calculs de distance

 - PyInstaller → Compilation en exécutable


Auteur : Antoine Chatelain

