# proyecto-django
proyecto-django


# Clonar el proyecto:
  git clone https://github.com/jtfrancov3/proyecto-django.git

# Crear un entorno virtual:
  python -m venv env

# Activar el entorno virtual:
  Windows: .\env\Scripts\activate
  macOS/Linux: source env/bin/actívate

# Instalar Django usando pip: 
  pip install django

  # Nota: En caso de existir actualizaciones, actualizar el pip:
	python.exe -m pip install --upgrade pip

# Moverse al directorio del proyecto clonado:
  cd proyecto-django

# Crear migraciones:
  python .\manage.py makemigrations

# Migrar la base de datos
  py .\manage.py migrate

# Ejecutar el servidor de desarrollo:
  python manage.py runserver

# Ingresar a la URL del proyecto
  http://127.0.0.1:8000/login

# Credenciales de acceso para pruebas:
  Usuario: jtfrancov
  Contraseña: 123456

# Notas:
  Ya se tienen datos de prueba de categorias para poder probar el CRUD