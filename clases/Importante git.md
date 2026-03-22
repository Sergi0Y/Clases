# Pasos para enviar a git nuestra carpeta

# ⚠️¡¡IMPORTANTE!!⚠️
Se debe subir una archivo llamado **.gitignore** en la carpeta raiz de nuestro proyecto, con este contenido:
```bash
env/
db.sqlite3
__pycache__/
*.pyc
.DS_Store
```
## Pasos

### 1. Iniciar Git en tu carpeta del escritorio
```bash
git init
```


### 2. Conectar tu carpeta local con tu repositorio de GitHub
```bash
git remote add origin https://github.com/username/Repo.git
```
### 3. Preparar todos tus archivos de Django
```bash
git add .
```

### 4. Crear el primer "paquete" de cambios
```bash
git commit -m "Proyecto inicial Django"
```

### 5. Subir todo a la rama 'Django', esto reemplazará los archivos que estaban antes
```bash
git push origin master:Django --force
```
### 6. Subir cambios nue