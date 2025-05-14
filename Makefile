# Makefile pour automatiser les étapes du projet licence-maquettes-rdf

# Commande principale : tout faire
all: clean convert syntax quality

# Nettoyage des CSV
clean:
	@echo "🔹 Nettoyage des fichiers CSV..."
	python clean_vertical_csv.py

# Conversion CSV ➝ RDF
convert:
	@echo "🔹 Conversion des fichiers CSV en RDF..."
	python csv_to_rdf.py

# Vérification de la syntaxe RDF
syntax:
	@echo "🔹 Vérification de la syntaxe RDF..."
	python validate_rdf.py

# Vérification de la qualité RDF
quality:
	@echo "🔹 Vérification des champs obligatoires dans les RDF..."
	python validate_rdf_quality.py

# Commande pour tout refaire proprement
reset:
	rm -rf maquettes_csv_clean/* rdf_output/*
	@echo "✅ Répertoires maquettes_csv_clean/ et rdf_output/ vidés."

