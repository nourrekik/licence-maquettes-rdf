import os
from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS, XSD

# Configuration
INPUT_FOLDER = "."  # dossier courant
COURSE = Namespace("http://example.org/course/")

# Critères minimaux
MIN_TEXT_LENGTH = 20  # pour objective ou content

def check_rdf_quality(file_path):
    g = Graph()
    try:
        g.parse(file_path, format="ttl")
    except Exception as e:
        return f"❌ {file_path} invalide (erreur RDF): {e}", False

    errors = []
    for s in g.subjects(RDFS.label, None):
        label = g.value(s, RDFS.label)
        content = g.value(s, COURSE.content)
        objective = g.value(s, COURSE.objective)
        semester = g.value(s, COURSE.semester)
        hours = g.value(s, COURSE.hours)

        if not label or not str(label).strip():
            errors.append(f"  ⛔ label manquant pour {s}")
        if not content or len(str(content).strip()) < MIN_TEXT_LENGTH:
            errors.append(f"  ⚠️ content vide ou trop court pour {s}")
        if not objective or len(str(objective).strip()) < MIN_TEXT_LENGTH:
            errors.append(f"  ⚠️ objective vide ou trop court pour {s}")
        if semester:
            try:
                int(semester.toPython())
            except Exception:
                errors.append(f"  ⚠️ semestre invalide pour {s}: {semester}")
        if hours:
            try:
                float(hours.toPython())
            except Exception:
                errors.append(f"  ⚠️ hours invalide pour {s}: {hours}")

    if errors:
        return f"❌ {file_path} a des problèmes :\n" + "\n".join(errors), False
    return f"✅ {file_path} est complet et cohérent.", True

def main():
    ttl_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".ttl")]
    all_valid = True

    for file in ttl_files:
        result, valid = check_rdf_quality(os.path.join(INPUT_FOLDER, file))
        print(result)
        if not valid:
            all_valid = False

    if all_valid:
        print("\n🎉 Tous les fichiers RDF sont complets et bien structurés.")
    else:
        print("\n⚠️ Des fichiers RDF contiennent des problèmes à corriger.")

if __name__ == "__main__":
    main()
