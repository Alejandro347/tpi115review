#!/usr/bin/env bash
# start.sh

# 1. Aplicar migraciones
echo "Aplicando migraciones..."
python manage.py migrate --noinput

# 2. Recolectar archivos estáticos
echo "Recolectando estáticos..."
python manage.py collectstatic --noinput

# 🔑 LÍNEA DEFINITIVA: CREACIÓN SILENCIOSA DEL SUPERUSUARIO
# Crea un usuario "admin" con el email "admin@ues.edu.sv" y la contraseña "password"
# (¡CAMBIA 'password' por una contraseña segura y REAL!)
echo "Creando Superusuario (silencioso)..."
python manage.py createsuperuser --noinput --username admin --email admin@ues.edu.sv || true

# 3. Forzar el cambio de la contraseña inmediatamente DESPUÉS de la creación
# Esto es necesario para que el usuario creado anteriormente tenga una contraseña establecida
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.filter(username='admin').first().set_password('Salvac0la').save()
EOF

# 4. Iniciar el servidor Gunicorn
echo "Iniciando Gunicorn..."
gunicorn config.wsgi --log-file -