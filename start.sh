#!/usr/bin/env bash
# start.sh

# 1. Aplicar migraciones
echo "Aplicando migraciones..."
python manage.py migrate --noinput

# 2. Recolectar estáticos
echo "Recolectando estáticos..."
python manage.py collectstatic --noinput

# 🔑 CREACIÓN/ACTUALIZACIÓN SILENCIOSA DEL SUPERUSUARIO
# Ejecuta código Python para asegurar que el usuario existe y tiene la contraseña correcta.
echo "Creando/Actualizando Superusuario (silencioso)..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()

# Datos del superusuario
ADMIN_USERNAME = 'admin'
ADMIN_EMAIL = 'admin@ues.edu.sv'
ADMIN_PASSWORD = 'Salvac0la'  # <--- ¡CAMBIA ESTO!

# Intenta obtener el usuario o crearlo
if not User.objects.filter(username=ADMIN_USERNAME).exists():
    user = User.objects.create_superuser(
        username=ADMIN_USERNAME,
        email=ADMIN_EMAIL,
        password=ADMIN_PASSWORD
    )
    print("Superusuario creado con éxito.")
else:
    # Opcional: Si ya existe, actualiza la contraseña (solo para asegurar)
    user = User.objects.get(username=ADMIN_USERNAME)
    user.set_password(ADMIN_PASSWORD)
    user.save()
    print("Superusuario actualizado con éxito.")

EOF

# 3. Iniciar el servidor Gunicorn
echo "Iniciando Gunicorn..."
gunicorn config.wsgi --log-file -