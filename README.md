# 📘 Projet de conversion des maquettes de Licence en RDF

Ce dépôt regroupe les maquettes de Licence (L1, L2, L3 – Informatique, Math-Info, MIAGE) converties au format RDF Turtle dans le cadre de mon stage de recherche à l’Université de Nantes.  
L’objectif est d’automatiser la génération de graphes de connaissances à partir des maquettes pédagogiques, en suivant un pipeline structuré.

## 🎯 Objectifs

- Extraire les données essentielles des maquettes : objectifs, contenu, crédits ECTS, volume horaire, semestre, niveau, responsable  
- Nettoyer et structurer ces données dans des fichiers `.csv`  
- Générer automatiquement les fichiers `.ttl` au format RDF via un script Python  
- Organiser les fichiers par spécialité (INFO, MATH-INFO, MIAGE) et par niveau (L1, L2, L3)
- Vérifier le contenu RDF généré via des requêtes SPARQL


## 🗂️ Structure du dépôt

licence-maquettes-rdf/
├── BodyOfKnowledge/ # Référentiels externes (ex : ACM)
├── maquette_pdf/ # Maquettes PDF originales
├── maquettes/ # Anciennes maquettes ou brouillons
├── maquettes_csv/ # Fichiers CSV bruts exportés
├── maquettes_csv_clean/ # CSV nettoyés automatiquement
├── maquettes_rdf/ # Fichiers RDF finaux (.ttl)
├── maquettes_xlsx/ # Versions intermédiaires Excel
├── rdf_output/ # Autres RDF générés temporairement
├── venv/ # Environnement virtuel Python
├── .gitignore
├── Makefile # Automatisation des tâches
├── README.md # Ce fichier
├── requirements.txt # Dépendances Python
├── clean_vertical_csv.py # Nettoyage des CSV
├── csv_to_rdf.py # Conversion CSV → RDF
├── validate_rdf.py # Vérification syntaxique RDF
├── validate_rdf_quality.py # Vérification des champs RDF
├── query_rdf.py # Requête SPARQL de validation
└── xlsx_to_csv.py # Conversion Excel → CSV


Chaque dossier de maquette contient :  
- le fichier PDF original  
- le fichier CSV nettoyé  
- le fichier TTL généré automatiquement


---

## ⚙️ Installation et 🚀 Utilisation

```bash
# 1. Cloner le dépôt
git clone https://github.com/nourrekik/licence-maquettes-rdf.git
cd licence-maquettes-rdf

# 2. Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Nettoyer les fichiers CSV bruts
python clean_vertical_csv.py

# 5. Convertir les fichiers CSV nettoyés en RDF (.ttl)
python csv_to_rdf.py

# 6. Vérifier la validité syntaxique des RDF
python validate_rdf.py

# 7. Vérifier la qualité des RDF (présence des champs requis)
python validate_rdf_quality.py

# 8. Interroger un fichier RDF avec SPARQL (exemple)
python query_rdf.py


## 🧩 Dépendances

Ce projet utilise :  
- pandas : traitement et manipulation des fichiers CSV  
- rdflib : génération et validation des graphes RDF  
- SPARQLLM : alignement sémantique (optionnel)

Toutes les dépendances sont listées dans `requirements.txt`.

## 🧪 Pipeline résumé

- Les maquettes PDF sont converties en `.csv` via iLovePDF + Apple Numbers  
- Les fichiers `.csv` sont nettoyés automatiquement avec `clean_vertical_csv.py`  
- Les CSV nettoyés sont transformés en RDF avec `csv_to_rdf.py`  
- Les fichiers RDF sont vérifiés par `validate_rdf.py` et `validate_rdf_quality.py`
-  Les RDF sont validés via validate_rdf.py et validate_rdf_quality.py
## Contexte

Ce travail est réalisé dans le cadre de mon stage de recherche au LS2N (Université de Nantes), dans le projet SPARQLLLM, encadré par Hala Skaf-Molli et Pascal Molli.