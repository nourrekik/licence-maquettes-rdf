import os
import pandas as pd

# Dossiers d'entrée/sortie
xlsx_dir = "maquettes_xlsx"
csv_output_dir = "maquettes_csv"

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(csv_output_dir, exist_ok=True)

# Parcourir tous les fichiers .xlsx du dossier
for file in os.listdir(xlsx_dir):
    if file.endswith(".xlsx"):
        input_path = os.path.join(xlsx_dir, file)
        output_filename = file.replace(".xlsx", ".csv")
        output_path = os.path.join(csv_output_dir, output_filename)

        try:
            # Lire le fichier Excel
            df = pd.read_excel(input_path, engine="openpyxl")

            # Supprimer les colonnes contenant "responsable" dans le nom
            for col in df.columns:
                if "responsable" in col.lower():
                    df[col] = ""

            # Exporter en CSV (anonymisé)
            df.to_csv(output_path, index=False, sep=';', encoding='utf-8')
            print(f"✅ Converti (anonymisé) : {input_path} → {output_path}")

        except Exception as e:
            print(f"❌ Erreur avec {file} : {e}")

