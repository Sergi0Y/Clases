# Clase 3

## crear pagina principal:

### En urls.py

```python
path('', views.hola_mundo),
#dejar las comillas vacías = "Home"
```

**_¡¡¡¡pero antes!!!_**
se debe importar views

```python
from principal import views
```

Esta sirve para que no se deba importar cada view que se realiza, sino que se agrega asi:

```python
from principal import views
path ('',views.nombre_funcion)
```

---

### Crear superusuario

#### 1. Antes de la creación debe estar creada la bd, `(db.sqlite3)`

```bash
python manage.py migrate
```

##### 2. Creando el usuario

```bash
python manage.py createsuperuser
```

en la terminal se mostrará
&bull; Username: Ahí se escribe `admin`
&bull; Email: (opcional)
&bull; Password: Es escribe una clave
&bull; Confirm Pass: repetir

---

### Crear páginas completas en views.py

##### Se usa la carpeta templates

###### 1. Dentro de la carpeta principal creamos esto: templates/principal/
###### 2. Dentro de esta carpeta creamos nuestro archivo `html`.
   Para que django pueda leer el archivo se debe importar `render` en principal/views.py:

```python
from django.shortcuts import render #
```

###### 3. Ahora debemos registrar la url:
   En urls.py, debemos tener el import de views

```python
path('web_name/', views.web_name),
```

o si se quiere dejar como main

```python
path('',views.web_name)
```

###### 4. Si se quiere usar el css (externo) se debe trabajar en la carpeta static:
   Se hace algo similar a la creación de templates pero con static

```bash
principal/
└── static/
    └── principal/
        └── styles.css
```

- `static/`: carpeta que debes crear
- `principal/`: subcarpeta para organizar archivos estáticos
- `styles.css`: archivo de estilos

###### 5. En Django no se usan vínuclos directos, ya que las carpetas están protegidas:
   El comienzo del html debe ser así:

```html
{% load static %}
<!-- 1. IMPORTANTE: Esto va en la primera línea -->
<!DOCTYPE html>
<html lang="es">
  <head>
    <!--metas-->
    <title>Mi página con Django</title>
    <!-- 2. La ruta correcta usando la etiqueta de Django -->
    <link rel="stylesheet" href="{% static 'principal/styles.css' %}" />
  </head>
  <body>
    <h1>Hola Django</h1>
  </body>
</html>
```

---

### Herencia de plantillas

###### 1. Vamos a crear un archivo `base.html` en el cual ingresaremos el diseño que irá fijo en todas las páginas, este lo vamos a crear en `templates/principal/base.html`. Dentro de este código irá el contenido variable con al etiqueta `{% block content %}`

```html
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <link rel="stylesheet" href="{% static 'principal/styles.css' %}">
</head>
    <nav>
        <h1>Título Fijo de mi Web</h1>
    </nav>
    <main>
        {% block content %}
        <!-- Aquí se inyectará el código de las otras páginas -->
        {% endblock %}
    </main>
    <footer>
        <hr>
        <p>Derechos Reservados 2026 - Clase de Django</p>
    </footer>
</body>
</html>
```

###### 2. Luego modificaremos nuestro `index.html` para que cambie sólo lo necesario, ya no necesita tener la estructura básica porque la va a heredar de `base.html` . Es importante que lo primero que escriban sea `{% extends 'principal/base.html' %}`

```html
{% extends 'principal/base.html' %} {% block content %}
<h2>Esta es la página de Inicio</h2>
<p>Bienvenidos alumnos, este contenido es único de esta página.</p>
{% endblock %}
```

### CONEXIÓN Python &harr; HTML

###### 1. Primero deberemos crear nuestros datos que vamos a mostrar de forma dinámica. En el archivo views.py, debemos modificar la función **main**, así debe quedar:

```python
def main(request):
    datos ={
        "nombre_curso": "Programación Backend con Django",
        "profesor": "Sergio",
        "n_alumnos": 15,
        "lista_alumnos": ["Juan", "María", "Pedro", "Ana"]
    }
    return render(request, 'principal/index.html',datos)
```

###### 2. Luego en nuestro archivo **index.html** debemos agregar la variable que queremos mostrar, en este caso será nombre_curso:

```html
{% extends 'principal/base.html' %} {% block content %}
<h2>Esta es la página de Inicio</h2>
<p>Bienvenidos alumnos, este es el curso de {{ nombre_curso }}.</p>
<!-- Aqui va nuestra variable -->
{% endblock %}
```

###### 3. Además podemos crear listas o tablas dinámicas con bucles for

```html
<p>Listado de alumnos</p>
<ul>
  {% for alumno in lista_alumnos %}
  <li>{{ alumno }}</li>
  {% endfor %}
</ul>
```
