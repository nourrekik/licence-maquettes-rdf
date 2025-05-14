import os
from rdflib import Graph
from rdflib.plugin import PluginException

# 📂 Dossier contenant les fichiers RDF (.ttl)
RDF_FOLDER = "maquettes_rdf"  # Change si besoin

# 🔍 Lister tous les fichiers .ttl du dossier
rdf_files = [f for f in os.listdir(RDF_FOLDER) if f.endswith(".ttl")]

if not rdf_files:
    print("❌ Aucun fichier .ttl trouvé dans le dossier :", RDF_FOLDER)
else:
    all_valid = True
    for filename in rdf_files:
        path = os.path.join(RDF_FOLDER, filename)
        try:
            g = Graph()
            g.parse(path, format="turtle")
            print(f"✅ {filename} est valide.")
        except (Exception, PluginException) as e:
            all_valid = False
            print(f"❌ ERREUR dans {filename} : {e}")

    if all_valid:
        print("\n🎉 Tous les fichiers RDF sont valides.")
    else:
        print("\n⚠️ Des erreurs ont été trouvées.")
