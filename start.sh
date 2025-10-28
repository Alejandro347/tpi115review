#!/usr/bin/env bash
# start.sh

# 1. Aplicar migraciones para crear las tablas de la base de datos
echo "Aplicando migraciones..."
python manage.py migrate --noinput

# 2. Recolectar archivos estáticos para que Bootstrap funcione
echo "Recolectando estáticos..."
python manage.py collectstatic --noinput

# 3. Iniciar el servidor Gunicorn (TU APLICACIÓN)
echo "Iniciando Gunicorn..."
gunicorn config.wsgi --log-file -