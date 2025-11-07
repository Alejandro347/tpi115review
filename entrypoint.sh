#!/bin/bash
# entrypoint.sh - Script de inicio para Docker/Dokploy
# Este script ejecuta migraciones y recolecta archivos estáticos antes de iniciar Gunicorn

set -e

echo "🚀 Iniciando aplicación TPI115 Review..."

# Esperar a que la base de datos esté lista (opcional, útil si la DB está en otro contenedor)
if [ -n "$DATABASE_URL" ]; then
    echo "⏳ Esperando conexión a la base de datos..."
    # Pequeña espera para que la DB esté lista
    sleep 2
fi

# Aplicar migraciones
echo "📦 Aplicando migraciones de base de datos..."
python manage.py migrate --noinput || {
    echo "❌ Error al aplicar migraciones"
    exit 1
}

# Recolectar archivos estáticos
echo "📁 Recolectando archivos estáticos..."
python manage.py collectstatic --noinput || {
    echo "⚠️  Advertencia: Error al recolectar archivos estáticos (continuando...)"
}

# Iniciar Gunicorn
echo "✅ Iniciando servidor Gunicorn..."
exec "$@"

