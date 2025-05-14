# 📘 Projet de conversion des maquettes de Licence en RDF

Ce dépôt regroupe les maquettes de Licence (L1, L2, L3 – Informatique, Math-Info, MIAGE) converties au format RDF Turtle dans le cadre de mon stage de recherche à l’Université de Nantes.  
L’objectif est d’automatiser la génération de graphes de connaissances à partir des maquettes pédagogiques, en suivant un pipeline structuré.

## 🎯 Objectifs

- Extraire les données essentielles des maquettes : objectifs, contenu, crédits ECTS, volume horaire, semestre, niveau, responsable  
- Nettoyer et structurer ces données dans des fichiers `.csv`  
- Générer automatiquement les fichiers `.ttl` au format RDF via un script Python  
- Organiser les fichiers par spécialité (INFO, MATH-INFO, MIAGE) et par niveau (L1, L2, L3)

## 🗂️ Structure du dépôt

licence-maquettes-rdf/  
├── BodyOfKnowledge/  
├── maquette_pdf/  
├── maquettes/  
├── maquettes_csv/  
├── maquettes_csv_clean/  
│   ├── L1-INFO.csv  
│   ├── L1-MATH-INFO.csv  
├── maquettes_rdf/  
│   ├── L1-INFO.ttl  
│   ├── L1-MATH-INFO.ttl  
├── maquettes_xlsx/  
├── rdf_output/  
├── venv/  
├── .gitignore  
├── pyvenv.cfg  
├── clean_vertical_csv.py  
├── csv_to_rdf.py  
├── validate_rdf.py  
├── validate_rdf_quality.py  
└── README.md


Chaque dossier de maquette contient :  
- le fichier PDF original  
- le fichier CSV nettoyé  
- le fichier TTL généré automatiquement

## ⚙️ Installation et 🚀 Utilisation

# 1. Cloner le dépôt  
git clone https://github.com/nourrekik/licence-maquettes-rdf.git  
cd licence-maquettes-rdf

# 2. Créer un environnement virtuel  
python3 -m venv venv  
source venv/bin/activate

# 3. Installer les dépendances  
pip install -r requirements.txt

# 4. Nettoyer les fichiers CSV bruts  
python converter/clean_vertical_csv.py

# 5. Convertir les fichiers CSV nettoyés en RDF (.ttl)  
python converter/csv_to_rdf.py

# 6. Vérifier la validité syntaxique des RDF  
python converter/validate_rdf.py

# 7. Vérifier la qualité des RDF (présence des champs requis)  
python converter/validate_rdf_quality.py

## 🧩 Dépendances

Ce projet utilise :  
- pandas : traitement et manipulation des fichiers CSV  
- rdflib : génération et validation des graphes RDF  
Toutes les dépendances sont listées dans `requirements.txt`.

## 🧪 Pipeline résumé

- Les maquettes PDF sont converties en `.csv` via iLovePDF + Apple Numbers  
- Les fichiers `.csv` sont nettoyés automatiquement avec `clean_vertical_csv.py`  
- Les CSV nettoyés sont transformés en RDF avec `csv_to_rdf.py`  
- Les fichiers RDF sont vérifiés par `validate_rdf.py` et `validate_rdf_quality.py`
## Contexte

Ce travail est réalisé dans le cadre de mon stage de recherche au LS2N (Université de Nantes), dans le projet SPARQLLLM, encadré par Hala Skaf-Molli et Pascal Molli.