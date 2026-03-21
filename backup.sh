#!/bin/bash

# Resolución dinámica del directorio base según la ubicación del script
cd "$(dirname "$0")" || exit 1

# Evaluación de estado para evitar commits vacíos
if [ -z "$(git status --porcelain)" ]; then
    echo "El sistema no detectó cambios nuevos; el respaldo se omite."
    exit 0
fi

# Generación de variables dinámicas para trazabilidad
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Secuencia de control de versiones
git add .
git commit -m "Respaldo del servidor: $TIMESTAMP"
git push origin "$BRANCH"

echo "El respaldo se completó y los cambios subieron correctamente a la rama $BRANCH."
