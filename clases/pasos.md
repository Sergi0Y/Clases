# Backend con Django

**Flujo de datos:**

URL (La dirección) ➔ VIEW (La lógica en Python) ➔ TEMPLATE (El dibujo en HTML).

>⚠️**IMPORTANTE:** Si la página no carga, el error está en uno de estos tres⚠️

---

- [Backend con Django](#backend-con-django)
    - [Configuración Página Principal](#configuración-página-principal)
    - [Crear superusuario](#crear-superusuario)
      - [1. Revisar Base de Datos](#1-revisar-base-de-datos)
      - [2. Creando el usuario](#2-creando-el-usuario)
    - [Crear páginas completas en views.py](#crear-páginas-completas-en-viewspy)
      - [1. Creación carpeta templates](#1-creación-carpeta-templates)
      - [2. Crear HTML](#2-crear-html)
      - [3. Registrar URL](#3-registrar-url)
      - [4. Uso de CSS](#4-uso-de-css)
      - [5. Manejo de Archivos Estáticos](#5-manejo-de-archivos-estáticos)
    - [Herencia de plantillas](#herencia-de-plantillas)
      - [1. Crear plantilla](#1-crear-plantilla)
      - [2. Creación de Página Dinámica](#2-creación-de-página-dinámica)
    - [CONEXIÓN Python ↔ HTML](#conexión-python--html)
      - [1. Definir el Contexto en la Vista](#1-definir-el-contexto-en-la-vista)
      - [2. Concatenar variable](#2-concatenar-variable)
      - [3. Listas y tablas con bucles](#3-listas-y-tablas-con-bucles)



### Configuración Página Principal

En `urls.py` modificamos de esta manera
```python
path('', views.hola_mundo),
#dejar las comillas vacías = "Home"
```

⚠️ **Nota crítica:** Antes de definir las rutas, debes importar views:

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

#### 1. Revisar Base de Datos 
Antes de la creación debe estar creada la bd, `(db.sqlite3)`

```bash
python manage.py migrate
```

#### 2. Creando el usuario

```bash
python manage.py createsuperuser
```

en la terminal se mostrará
> - Username: Ahí se escribe `admin`
> - Email: (opcional)
> - Password: Es escribe una clave
> - Confirm Pass: repetir

---

### Crear páginas completas en views.py


#### 1. Creación carpeta templates
Dentro de la carpeta principal creamos esto: `principal/templates/principal/`. Quedaría así:
```
principal/
└── templates/
    └── principal/        
```

#### 2. Crear HTML
Dentro de la carpeta principal creamos nuestro archivo `html`.

Para que django pueda leer el archivo se debe importar `render` en principal/views.py:

```python
from django.shortcuts import render #
```

#### 3. Registrar URL


En urls.py, debemos tener el import de views

```python
path('web_name/', views.web_name),
```

o si se quiere dejar como main

```python
path('',views.web_name)
```

#### 4. Uso de CSS
Si se quiere usar el css externo se debe trabajar en la carpeta **static**:

Se hace algo similar a la creación de templates pero con static

```
principal/
└── static/
    └── principal/
        └── styles.css
```

- `static/`: carpeta que debes crear
- `principal/`: subcarpeta para organizar archivos estáticos
- `styles.css`: archivo de estilos

#### 5. Manejo de Archivos Estáticos 
En Django no se usan vínculos directos, ya que las carpetas están protegidas. Por eso, el comienzo del HTML debe ser así:

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

#### 1. Crear plantilla
Vamos a crear un archivo `base.html`, en el cual ingresaremos el diseño que irá fijo en todas las páginas, este lo vamos a crear en `templates/principal/base.html`. Dentro de este código irá el contenido variable con al etiqueta `{% block content %}`

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
Para que Django pueda "hablar" con el HTML y pasarle datos, usamos dos tipos de llaves. Es vital no confundirlas:

**Variables {{ ... }}** (Doble Llave):

**Uso**: Para mostrar información que viene de Python (el contenido).

**Ejemplo:**
```html
<h1>Hola {{ nombre_curso }}</h1>
```
**Regla**: Si quieres que se vea el dato en la pantalla, usa esta.

**Etiquetas de Control {% ... %}** (Llave y Porcentaje):

**Uso**: Para dar órdenes o lógica (bucles, condiciones, importar archivos).

**Ejemplo:** 
```python
{% for alumno in lista %} o {% load static %}.
```

**Regla de Oro:** Casi todas las órdenes de bloque deben cerrarse, con un: **{% endfor %}.**

#### 2. Creación de Página Dinámica
Luego modificaremos nuestro `index.html` para que cambie sólo lo necesario, ya no necesita tener la estructura básica porque la va a heredar de `base.html`. 
**🛑 Regla Crítica:** La etiqueta **{% extends %} **debe ser siempre la primera línea del archivo. Si hay un espacio o comentario arriba, la herencia fallará.

```html
{% extends 'principal/base.html' %} {% block content %}
<h2>Esta es la página de Inicio</h2>
<p>Bienvenidos alumnos, este contenido es único de esta página.</p>
{% endblock %}
```

### CONEXIÓN Python &harr; HTML

#### 1. Definir el Contexto en la Vista
Primero deberemos crear nuestros datos que vamos a mostrar de forma dinámica. En el archivo views.py, debemos modificar la función **main**, así debe quedar:
**Archivo:** `principal/views.py`
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

#### 2. Concatenar variable
Luego en nuestro archivo **index.html** debemos agregar la variable que queremos mostrar, en este caso será nombre_curso:

```html
{% extends 'principal/base.html' %} {% block content %}
<h2>Esta es la página de Inicio</h2>
<p>Bienvenidos alumnos, este es el curso de {{ nombre_curso }}.</p>
<!-- Aqui va nuestra variable -->
{% endblock %}
```

#### 3. Listas y tablas con bucles
Además podemos crear listas o tablas dinámicas con bucles for

```html
<p>Listado de alumnos</p>
<ul>
  {% for alumno in lista_alumnos %}
  <li>{{ alumno }}</li>
  {% endfor %}
</ul>
```
A diferencia de Python donde usamos sangría (espacios), en el HTML de Django debemos avisar dónde termina un proceso.

Recordatorio de cierre en HTML:

>**{% for %}** ➔ requiere {% endfor %}
**{% if %}** ➔ requiere {% endif %}
**{% block %}** ➔ requiere {% endblock %}
