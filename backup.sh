#!/bin/bash

# Navegar al repositorio 
cd /workspaces/upgraded-octo-tribble

# Añadir todos los cambios
git add .

# Hacer commit con mensaje
git commit -m "Actualización de mods, scripts y del mundo"

# Subir los cambios a GitHub
git push origin main

echo "Todos los cambios han sido subidos correctamente."
