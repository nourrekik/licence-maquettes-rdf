import os
import csv
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, XSD

# 📂 Dossiers d’entrée et sortie
CSV_FOLDER = "maquettes_csv_clean"
RDF_FOLDER = "maquettes_rdf"

# Créer le dossier de sortie s’il n’existe pas
os.makedirs(RDF_FOLDER, exist_ok=True)

# Namespace personnalisé
NS = Namespace("http://example.org/course/")

# Champs attendus
expected_fields = {"code_UE", "label", "objectifs", "contenu", "volume_horaire", "ects", "semestre", "niveau"}

def safe_literal(value, datatype):
    if value.strip() == "":
        return None
    try:
        if datatype == XSD.int:
            return Literal(int(value), datatype=datatype)
        elif datatype == XSD.float:
            return Literal(float(value), datatype=datatype)
        else:
            return Literal(value.strip(), datatype=datatype)
    except:
        return None

# 🔄 Parcourir tous les CSV
for filename in os.listdir(CSV_FOLDER):
    if not filename.endswith(".csv"):
        continue

    path = os.path.join(CSV_FOLDER, filename)
    g = Graph()
    g.bind("ns1", NS)
    g.bind("rdfs", RDFS)
    g.bind("xsd", XSD)

    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        
        if not expected_fields.issubset(reader.fieldnames):
            print(f"⚠️ {filename} ignoré : colonnes manquantes.")
            continue

        for row in reader:
            subject = NS[row["code_UE"].strip()]
            g.add((subject, RDFS.label, Literal(row["label"].strip())))

            for field, predicate, dtype in [
                ("contenu", NS.content, XSD.string),
                ("objectifs", NS.objective, XSD.string),
                ("niveau", NS.level, XSD.string),
                ("volume_horaire", NS.hours, XSD.float),
                ("ects", NS.ects, XSD.float),
                ("semestre", NS.semester, XSD.int),
            ]:
                value = safe_literal(row.get(field, ""), dtype)
                if value is not None:
                    g.add((subject, predicate, value))

    # 💾 Écriture du fichier TTL
    out_name = os.path.splitext(filename)[0] + ".ttl"
    out_path = os.path.join(RDF_FOLDER, out_name)
    g.serialize(destination=out_path, format="turtle")
    print(f"✅ RDF généré : {out_name}")

