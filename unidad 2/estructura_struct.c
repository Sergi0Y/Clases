

/* 
#include <stdio.h>
struct Libro {
    char titulo[100];  // String
    int año;          // Entero
    int disponible;   // 0 = No, 1 = Sí
}; */

// Definición de la estructura

/* 
struct Producto {
    char nombre[50]; // String
    int precio;      // Decimal
    int disponible;  // 0 = No, 1 = Si
};



int main() {
    // Declarar una variable de tipo Producto
    struct Producto producto1;  // Ahora producto1 contiene nombre, precio e id.

    // Acceder a los campos
    strcpy(producto1.nombre, "Laptop");  // Asignar nombre (usar strcpy para strings)
    producto1.precio = 899.99;           // Asignar precio
    producto1.disponible = 1;                  // Asignar disponibilidad

    printf("Nombre: %s\n", producto1.nombre);
    return 0;
} */
/* 

#include <string.h>

struct Producto {
    char nombre[50];
    double precio;
};

int main() {
    struct Producto p1, p2;

    // Usando fgets para ingresar el nombre
    printf("Ingresa el nombre del producto 1: ");
    fgets(p1.nombre, sizeof(p1.nombre), stdin);

    // Agregamos el precio
    p1.precio = 1000.0;

    // Usando strcpy para copiar un nombre predefinido
    strcpy(p2.nombre, "Pan Integral");
    p2.precio = 1500.0;

    // Mostrar los productos
    printf("\nProducto 1:\nNombre: %sPrecio: %.2f\n", p1.nombre, p1.precio);
    printf("\nProducto 2:\nNombre: %s\nPrecio: %.2f\n", p2.nombre, p2.precio);

    return 0;
} */




#include <stdio.h>
#include <string.h>

struct Producto {
    char nombre[50];
    int precio;
};

int main() {
    struct Producto p1, p2;

    // Producto 1
    printf("Ingresa el nombre del producto 1: ");
    fgets(p1.nombre, sizeof(p1.nombre), stdin);
    

    printf("Ingresa el precio: ");
    scanf("%d", &p1.precio);

    /* 

    Cuando mezclas funciones como scanf y fgets, ocurre esto:
    1.- scanf lee datos pero deja el '\n' en el buffer (porque no lo consume).

    2.- fgets lee hasta encontrar un '\n', pero si hay uno residual en el buffer, se ejecuta    inmediatamente sin esperar nueva entrada.

    ¿Qué pasa si no usamos limpiamos el buffer?
        Pasa que el programa "se salta" el fgets para el nombre del producto 2 en este caso.

    Para eliminar caracteres residuales como \n se usa un bucle que recorre la línea hasta eliminarlos

    while (getchar() != '\n');  // Lee y descarta todo hasta el '\n'

    ¿Cómo funciona?
        getchar() lee un carácter del buffer.

        Si es '\n', el bucle termina (buffer limpio).

        Si no, sigue leyendo y descartando.
    */
    while (getchar() != '\n'); // Limpiar buffer

    // Producto 2
    printf("Ingresa el nombre del producto 2: ");
    fgets(p2.nombre, sizeof(p2.nombre), stdin);
    

    printf("Ingresa el precio: ");
    scanf("%d", &p2.precio);

    // Mostrar los productos
    printf("\nProducto 1:\nNombre: %sPrecio: %d\n", p1.nombre, p1.precio);
    printf("\nProducto 2:\nNombre: %sPrecio: %d\n", p2.nombre, p2.precio);

    return 0;
}



/*  #include <stdio.h>

 int main() {
     char nombre[5];
 
     printf("¿Cómo te llamas? ");
     fgets(nombre, sizeof(nombre), stdin);  // AQUÍ usamos stdin
 
     printf("%lu",sizeof(nombre));
     printf("Hola, %s", nombre);
     return 0;
     
 }
 
 */