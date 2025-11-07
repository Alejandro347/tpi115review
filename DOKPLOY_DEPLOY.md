# Guía de Despliegue en Dokploy

Esta guía te ayudará a desplegar la aplicación TPI115 Review en Dokploy.

## Prerrequisitos

- Una instancia de Dokploy funcionando
- Acceso a un repositorio Git (GitHub, GitLab, etc.)
- Base de datos PostgreSQL (puede ser provista por Dokploy o externa)

## Pasos para Desplegar

### 1. Preparar el Repositorio

Asegúrate de que todos los archivos necesarios estén en tu repositorio:
- ✅ `Dockerfile`
- ✅ `.dockerignore`
- ✅ `requirements.txt`
- ✅ `config/settings.py` (configurado para PostgreSQL)

### 2. Crear la Aplicación en Dokploy

1. Inicia sesión en tu instancia de Dokploy
2. Ve a **Applications** → **New Application**
3. Selecciona **Git Repository** como fuente
4. Conecta tu repositorio (GitHub/GitLab)
5. Selecciona la rama (típicamente `main` o `master`)

### 3. Configurar la Base de Datos

#### Opción A: Base de datos de Dokploy

1. En Dokploy, crea una nueva base de datos PostgreSQL
2. Anota las credenciales (host, puerto, nombre, usuario, contraseña)

#### Opción B: Base de datos externa

Usa cualquier servicio de PostgreSQL (Render, Railway, Supabase, etc.)

### 4. Configurar Variables de Entorno

En la configuración de la aplicación en Dokploy, agrega las siguientes variables de entorno:

#### Variables Requeridas

```env
# Base de datos (formato de URL completa)
DATABASE_URL=postgresql://usuario:contraseña@host:puerto/nombre_db

# Django Secret Key (genera uno nuevo para producción)
SECRET_KEY=tu-secret-key-super-seguro-aqui

# Debug (False en producción)
DEBUG=False

# URL del sitio
SITE_URL=https://tu-dominio.com

# Allowed Hosts (separados por comas)
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com
```

#### Variables Opcionales

```env
# Timezone
TZ=UTC

# Idioma
LANGUAGE_CODE=es-es

# Site ID (para django.contrib.sites)
SITE_ID=1
```

### 5. Configurar el Build

En Dokploy, configura:

- **Build Command**: (dejar vacío, el Dockerfile maneja todo)
- **Start Command**: `gunicorn config.wsgi --bind 0.0.0.0:8000 --workers 3 --timeout 120`
- **Port**: `8000`

### 6. Configurar el Dominio

1. En la configuración de la aplicación, agrega tu dominio
2. Dokploy configurará automáticamente el proxy reverso
3. Asegúrate de que los DNS apunten correctamente

### 7. Ejecutar Migraciones

Después del primer despliegue, ejecuta las migraciones:

**Opción A: Desde Dokploy**
- Ve a la aplicación → **Shell**
- Ejecuta: `python manage.py migrate`

**Opción B: Modificar el Dockerfile temporalmente**
Agrega al CMD del Dockerfile:
```dockerfile
CMD sh -c "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn config.wsgi --bind 0.0.0.0:8000 --workers 3 --timeout 120"
```

### 8. Crear Superusuario

Para acceder al panel de administración:

1. Ve a **Shell** en Dokploy
2. Ejecuta: `python manage.py createsuperuser`
3. Sigue las instrucciones

### 9. Verificar el Despliegue

1. Visita tu dominio
2. Verifica que la aplicación carga correctamente
3. Prueba crear una reseña
4. Accede a `/admin/` con tu superusuario

## Comandos Útiles

### Ejecutar en el contenedor (Shell de Dokploy)

```bash
# Migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Shell de Django
python manage.py shell

# Ver logs
# (Los logs están disponibles en la interfaz de Dokploy)
```

## Solución de Problemas

### Error: "No module named 'django'"
- Verifica que `requirements.txt` esté en el repositorio
- Revisa los logs de build en Dokploy

### Error: "Database connection failed"
- Verifica que `DATABASE_URL` esté correctamente configurada
- Asegúrate de que la base de datos esté accesible desde el contenedor
- Verifica firewall/red en Dokploy

### Error: "Static files not found"
- Ejecuta: `python manage.py collectstatic --noinput`
- Verifica que `STATIC_ROOT` esté configurado en `settings.py`

### Error: "DisallowedHost"
- Agrega tu dominio a `ALLOWED_HOSTS` en las variables de entorno
- O configura `ALLOWED_HOSTS=*` temporalmente para debug

## Estructura de Archivos Importantes

```
tpi115review/
├── Dockerfile              # Configuración de Docker
├── .dockerignore            # Archivos a ignorar en build
├── docker-compose.yml       # Para desarrollo local (opcional)
├── requirements.txt         # Dependencias de Python
├── config/
│   └── settings.py          # Configuración de Django
└── manage.py                # Script de gestión de Django
```

## Notas Adicionales

- **WhiteNoise**: Ya está configurado para servir archivos estáticos
- **Gunicorn**: Configurado con 3 workers (ajusta según recursos)
- **PostgreSQL**: Recomendado para producción (SQLite solo para desarrollo)
- **HTTPS**: Dokploy maneja SSL automáticamente con Let's Encrypt

## Actualizaciones Futuras

Para actualizar la aplicación:
1. Haz push de los cambios a tu repositorio
2. Dokploy detectará los cambios y reconstruirá automáticamente
3. O manualmente: **Redeploy** en la interfaz de Dokploy

## Soporte

Si tienes problemas:
1. Revisa los logs en Dokploy
2. Verifica las variables de entorno
3. Asegúrate de que la base de datos esté accesible
4. Consulta la documentación de Dokploy: https://dokploy.com/docs

