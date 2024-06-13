#!/bin/bash

set -e

# Esperar hasta que la base de datos esté lista
while ! pg_isready -h $HOST -p 5432 -U $USER; do
  echo "Esperando a la base de datos..."
  sleep 2
done

# Ejecutar Odoo
exec "$@"
