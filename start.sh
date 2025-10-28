#!/usr/bin/env bash
# start.sh

# 1. Aplicar migraciones
echo "Aplicando migraciones..."
python manage.py migrate --noinput

# 2. Recolectar archivos estáticos
echo "Recolectando estáticos..."
python manage.py collectstatic --noinput



# 3. Iniciar el servidor Gunicorn
echo "Iniciando Gunicorn..."
gunicorn config.wsgi --log-file -