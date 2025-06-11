# Headers

Las etiquetas de títulos de escriben con h seguido del número de este (desde el 1 al 6) en orden descendente

```html
<h1>ejemplo de h1</h1>
```

&bull; H1 &rarr; Título más grande
&bull; H6 &rarr; Título más pequeño, similar a un párrafo (p)

#Párrafo
dentro de mis párrafos si yo quiero destacar una palabra o palabras, se usa la etiqueta strong
&bull; ejemplo:

```html
<p>
  15 años de experiencia como <strong>Ingeniero de software de la NASA</strong>.
  Creador de contenido y divulgador científico
</p>
```

# Listas

Adicionalmente a lo anterior también podemos agregar listas ordenadas y no ordenadas, las no ordenadas son listas sin indices y las ordenadas si lo poseen.
La sintaxis para escribir listas es la siguiente:
Primero se escriben las etiquetas **ul** que serán mi comienzo y final de lista, luego, dentro de estas etiquetas irá mi contenido o mi listado, en etiquetas **li**

&bull;ejemplo:

```html
<ul>
  <li>Google</li>
  <li>Yahoo</li>
  <li>Bing</li>
  <li>DuckDuckGo</li>
</ul>
```

# Imágenes
<img src="https://static.vecteezy.com/system/resources/thumbnails/006/054/084/small/retro-style-background-with-grunge-texture-free-vector.jpg">
Podemos agregar imágenes en nuestra página web, para ello, existen dos maneras.
La primera es descargando la imagen y trabajando localmente:
```
<img src = /images/fondo.png>
```
La otra forma es pasarle directamente el link de la imagen dentro de mi etiqueta:
```
<img src = https://static.vecteezy.com/system/resources/thumbnails/006/054/084/small/retro-style-background-with-grunge-texture-free-vector.jpg>
```

&bull;La primera forma podría volver mi página un poco más lenta ya que debe cargar más elementos y dependiendo del tamaño de la o las imágenes se demorará más o menos 
&bull;Por otro lado, la segunda forma de agregar imágenes, es más rapida en comparación con la primera, pero corro el riesgo de que la página de donde saqué mi imagen se caiga y no esté disponible. 


