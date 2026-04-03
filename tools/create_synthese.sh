#!/bin/bash
# Script de création du fichier synthese.md
# Concatène tous les fichiers .md de Fiches_Solutions et génère la synthèse dans tools/

OUTPUT="synthese.md"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE_DIR="$(cd "$SCRIPT_DIR/../Fiches_Solutions" && pwd)"

# Supprimer le fichier de sortie s'il existe déjà
rm -f "$SCRIPT_DIR/$OUTPUT"

# Parcourir tous les fichiers .md triés alphabétiquement
for file in "$SOURCE_DIR"/*.md; do
    filename=$(basename "$file")

    # Exclure le fichier de sortie lui-même
    if [ "$filename" = "$OUTPUT" ]; then
        continue
    fi

    # Titre du fichier sans l'extension .md
    title="${filename%.md}"

    # Ajouter séparateur + titre + contenu
    {
        echo "---"
        echo ""
        echo "# $title"
        echo ""
        cat "$file"
        echo ""
        echo ""
    } >> "$SCRIPT_DIR/$OUTPUT"
done

echo "synthese.md créé avec $(grep -c '^# ' "$SCRIPT_DIR/$OUTPUT") fiches."
