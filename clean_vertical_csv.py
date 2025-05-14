import os
import csv
import re

input_dir = "maquettes_csv"
output_dir = "maquettes_csv_clean"
os.makedirs(output_dir, exist_ok=True)

# Clés à extraire
keep_keys = {
    "Objectifs (résultats d'apprentissage)": "objectifs",
    "Contenu": "contenu",
    "Volume horaire total": "volume_horaire",
    "Semestre": "semestre",
    "Niveau": "niveau",
    "Pondération pour chaque matière": "ects"
}

def extract_hours(text):
    match = re.search(r'TOTAL\s*:\s*(\d+)', text)
    return match.group(1) if match else ""

def extract_ects(text):
    match = re.search(r'\b(\d{1,2})\b', text)
    return match.group(1) if match else ""

for file in os.listdir(input_dir):
    if file.endswith(".csv"):
        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, file)

        with open(input_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            rows = list(reader)

        cleaned = []
        i = 0
        while i < len(rows):
            if len(rows[i]) < 2 or not rows[i][0].startswith("X"):
                i += 1
                continue

            ue = {
                "code_UE": rows[i][0].strip(),
                "label": rows[i][1].strip(),
                "objectifs": "",
                "contenu": "",
                "volume_horaire": "",
                "ects": "",
                "semestre": "",
                "niveau": ""
            }
            i += 1

            while i < len(rows) and (rows[i][0].strip() == "" or not rows[i][0].startswith("X")):
                key = rows[i][0].strip()
                value = rows[i][1].strip() if len(rows[i]) > 1 else ""

                if key in keep_keys:
                    if key == "Volume horaire total":
                        ue["volume_horaire"] = extract_hours(value)
                    elif key == "Pondération pour chaque matière":
                        ue["ects"] = extract_ects(value)
                    else:
                        ue[keep_keys[key]] = value

                i += 1

            cleaned.append(ue)

        with open(output_path, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["code_UE", "label", "objectifs", "contenu", "volume_horaire", "ects", "semestre", "niveau"], delimiter=';')
            writer.writeheader()
            writer.writerows(cleaned)

        print(f"✅ Fichier nettoyé : {output_path}")

