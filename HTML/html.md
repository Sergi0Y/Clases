# Estructura básica

## nodo doctype

Lo primero a tener en cuenta en cualquier archivo de tipo HTML es un nodo, no etiqueta ni elemento, que va al comienzo de todo, este nodo sirve par aespecificar la version de html que el documento está utilizando, esta declaración le dice al navegador como debe interpretar y renderizar el código html de la página.

```html
<!DOCTYPE html>
```

## Cuerpo de la página

Luego de escribir el doctype, vamos a usar la etiqueta **<html>** es un elemento raiz y la declaración del principio de nuestro documento en donde tendremos todo el contenido.

```html
<!DOCTYPE html>
<html>
  código html
</html>
```

## Contenido Raíz

Como se menciona anteriormente nosotros trabajamos con html que es el contenido raíz o principal, pero este a su vez de subdivide en dos, **head** y **body**, dentro del body es donde realmente va todo nuestro código. Así quedaría el código de nuestra página

```html
<!DOCTYPE html>
<html>
  <head> </head>
  <body>
    código html
  </body>
</html>
```

### HEAD

Nuestro head nos sirve para introducir metadatos, informacion extra, donde van los tipos de archivos CSS que vamos a usar, una descripción de la página, autor o autores de esta, es parte del código que no se va a redenderizar y que nos sirve para darle información a la página. Por ejemplo aquí es donde va el UTF-8, el cual nos sirve para saber el tipo de codificación con la cual vamos a trabajar. Ahora vamos a ver cada punto del siguiente ejemplo, explicando para qué sirven. Es importante mencionar que existen muchos tipos de metadatos, algunos propios para cada tipo de navegador, por lo que no vamos a ver todos los que existen, sino los más usados.

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width" />
  <meta title="WebPage name" />
  <meta name="robots" content="index, follow"/>
  <meta name="theme-color" content="#09f" />
  <link rel="icon" type="image/jpg" href="/HTML/images/yop.jpg">
  <meta name ="description" content="explicación breve sobre qué trata tu página">
</head>
```

&bull; **UTF-8** Nos permite trabajar con emojis, tiles y letras o caracterizaciones propias del español, como la letra ñ o solamente con la virgulilla (~)

&bull; **viewport** Este meta se usa para permitir una mejor adaptabilidad del contenido. Sirve para que el ancho del contenido sea el mismo del ancho de la pantalla del dispositivo en el cual se está visualizando la página para que, a partir de ahí, se acomode el contenido y sea manipulable si perder la estrcutura que nosotros hemos creado. Se usa principalmente para dispositivos móviles, pero afecta el comportamiento del sitio en cualquier dispositivo con pantalla escalable, como tablets o navegadores de escritorio con ventana reducida.

&bull; **title** La estiqueta title además de brindarnos un título para nuestra página (el cual aparece en la pestaña), nos sirve al momento de ralizar las búsquedas por google o por cualquier navegador, va a encontrar nuestra página según el title que le hayamos asignado, por lo que es muy importante que sepan elegir bien un nombre para nuestra web

&bull; **robots** Se usa para dirigirse a los bots de google o de los navegadores que recorren la web para buscar contenido, con el **content** digo que esta será mi index para que aparezca en los  resultados de búsquedas y el **follow** sirve por si agregamos enlaces dentro de mi página, me permite seguirlos y analizarlos. Si no se incluye, los navegadores los asumiran por defecto, pero es mucho mejor agregarlo para tener un mejor control sobre el SEO (optimización para motores de búsqueda)

&bull; **theme-color** Este meta nos brinda una mayor personalización de la página, lo que hace es cambiar el color de la barra superior de nuestra web, con el color que agregamos en el **content**. Este funciona solamente para celulares, es posible verlos desde los computadores pero hay que hacer pasos, en cambio desde el celular es inmediato.

&bull; **favicon** Este a diferencia del resto, no es un metadato, se usa la etiqueta **link** ya que está enlazando un recurso, el cual es el ícono que aparece en la pestaña cuando abrimos nuestra página.

&bull; **description** Este atributo es de suma importancia, ya que además de servir como una breve descripción del contenido de mi web, generalmente, es el texto que aparece abajo del título al momento de buscar mi página en google por ejemplo


&bull;
&bull;
&bull;
&bull;






----
### BODY

---

# Títulos

Las etiquetas de títulos de escriben con h seguido del número de este (desde el 1 al 6) en orden descendente

```html
<h1>ejemplo de h1</h1>
```

&bull; H1 &rarr; Título más grande
&bull; H6 &rarr; Título más pequeño, similar a un párrafo (p)

# Párrafo

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

# Atributos

Las etiquetas además pueden poseer atributos, estos son sirven para definir propiedades de la misma, por ejemplo en la etiqueta imagen, se agrega el atributo **src** (source) que es de donde vamos a obtener nuestra imagen.
Respecto sobre los atributos y dependiendo de lo que se vaya a incluir en el no es obligatorio el uso de comillas, por ejemplo, yo tengo un atributo **title** y agregaré cadenas de texto entonces si es necesario usar las comillas, pero, si usamos los atributos **width** o **height** los cuales trabajan con unidades de medida (números) no es necesario agregarlas
Existen varios tipos:
Atributos específicos y globales o generales

### Específicos

&bull;El atributo **src** de la etiqueta **img** especifica la ruta de donde va a obtener mi imagen, esta puede ser local o una url

&bull;El atributo **href** de la etiqueta **a** especifica una url a la cual el hipervínculo nos va a llevar

&bull;El atributo **alt** usado en la etiqueta **img** me genera un texto alternativo en caso de que la imagen no esté disponible

### Globales

&bull;Los atributos **width** y **height** son generalmente usados en la etiqueta **img** el cual me asigna los tamaños que va a tomar

&bull;El atributo **style** es usado para añadir estilos a mi elemento, como puede ser un color, tipo de fuente, tamaño, etc.

&bull;El atributo **lang** de la etiqueta **html** define el lenguaje de la página web

&bull;el atributo **title** define información extra sobre un elementos. Además si se agrega en una imagen por ejemplo, al poner el cursor sobre esta, sale lo que escribimos dentro de title

- **id**: Asigna un ID único al elemento.

- **class**: Asigna una clase CSS al elemento. Se usa para elementos que se repiten

- **hidden**: Oculta el elemento.

- **accesskey**: Define una tecla de acceso para el elemento.

- **contenteditable**: Permite editar el contenido del elemento.

- **dir**: Define la dirección del texto (LTR o RTL).

- **tabindex**: Define el orden de enfoque del elemento.

--

---

# Estilos por defecto

Los navegadores poseen estilos por defecto, esto se le llaman **Stylesheet user agent**, estos dependen (en su mayoría son similares pero hay leves variaciones) del navegador que se estuviese usando, por ejemplo al declarar un h1 en Chrome de veía de x manera y al mostrar el mismo h1 en Mozila de veía de z manera, esto no estaba bien, ya que lo que se busca al momento de declarar los estilos es que siempre sean los mismos independiente de donde se este viendo. Para poder solucionar este problema se creó el css reset, para que se viese igual en cualquier navegador.


