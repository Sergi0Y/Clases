// EJERCICIO 1
//Escribe un programa que pida dos números enteros al usuario, los sume, reste, multiplique y divida (si el segundo número no es 0), luego imprima los resultados.

/* #include <stdio.h>

int main() {
    int num1, num2;

    printf("Ingresa dos números enteros: ");
    scanf("%d %d", &num1, &num2);

    printf("La suma es: %d\n", num1 + num2);
    printf("La resta es: %d\n", num1 - num2);
    printf("La multiplicación es: %d\n", num1 * num2);
    if (num2 != 0) {
        printf("La división es: %.2f\n", (float)num1 / num2);
    } else {
        printf("No se puede dividir por 0.\n");
    }

    return 0;
} */



// EJERCICIO 2
//Escribe un programa que pida un número entero y determine si es positivo, negativo o cero. Imprime un mensaje correspondiente.

/* #include <stdio.h>

int main() {
    int num;

    printf("Ingresa un número: ");
    scanf("%d", &num);

    if (num > 0) {
        printf("El número es positivo.\n");
    } else if (num < 0) {
        printf("El número es negativo.\n");
    } else {
        printf("El número es cero.\n");
    }

    return 0;
} */



// EJERCICIO 3
/* Escribe un programa que pida una letra ('A', 'B' o 'C') y haga lo siguiente:
Si es 'A', imprime "Primera opción".
Si es 'B', imprime "Segunda opción".
Si es 'C', imprime "Tercera opción".
Si es otra letra, imprime "Opción no válida". */

/* #include <stdio.h>

int main() {
    char opcion;
    
    printf("Ingresa una letra (A, B o C): ");
    scanf("%c", &opcion);
    
    switch (opcion) {
        case 'A':
            printf("Primera opción.\n");
            break;
        case 'B':
            printf("Segunda opción.\n");
            break;
        case 'C':
            printf("Tercera opción.\n");
            break;
        default:
            printf("Opción no válida.\n");
    }
    
    return 0;
} */



//EJERCICIO 4 
//Escribe una función que reciba dos números y devuelva su suma. Luego, en la función main, pide al usuario que ingrese dos números y llama a la función para obtener la suma y mostrar el resultado.

/* #include <stdio.h>

// Función que recibe dos números y devuelve su suma
int sumar(int num1, int num2) {
    return num1 + num2;
}

int main() {
    int num1, num2, resultado;

    // Pedir al usuario que ingrese dos números
    printf("Ingresa el primer número: ");
    scanf("%d", &num1);
    
    printf("Ingresa el segundo número: ");
    scanf("%d", &num2);

    // Llamar a la función para obtener la suma
    resultado = sumar(num1, num2);

    // Mostrar el resultado
    printf("La suma de %d y %d es: %d\n", num1, num2, resultado);

    return 0;
} */



// EJERCICIO 5
//Escribe un programa que pida al usuario su nombre completo (usando scanf o fgets), y luego imprima el nombre en mayúsculas.

/* 
#include <stdio.h>

//Se incluye para poder usar funciones que manejan caracteres como toupper()
#include <ctype.h>


int main() {

    //creamos un array de caracteres con espacio 100 caracteres
    char nombre[100];
    
    printf("Ingresa tu nombre completo: ");
    
    //***************************************************************************************
    //IMPORTANTE: scanf no permite espacios al momento de escribir, cosa que si permite fgets
    //***************************************************************************************

    //Lee la linea completa y la guarda en el nombre
    fgets(nombre, 100, stdin);

    //******************************************************************************************************
    //STDIN significa "standart input"es una forma de hacer una referencia al texto que ingresará el usuario se aplica cuando usamos fgets
    
    //scanf() usa internamente de forma automática stdin, por eso no lo escribimos cuando usamos el scanf
    //pero a diferencia con fgets hay que declararlo siempre.
    //******************************************************************************************************
    
    for (int i = 0; nombre[i] != '\0'; i++) {
        //Se recorre el array nombre carácter por carácter hasta que encuentre '\0', que es el carácter nulo que indica el fin de la cadena. 

        nombre[i] = toupper(nombre[i]); 
        //toupper(nombre[i]): Convierte el carácter actual a mayúscula, si es una letra minúscula. Si no es una letra, lo deja igual. 
    }
    
    printf("Tu nombre en mayúsculas es: %s\n", nombre);
    //Muestra el nombre ya transformado, usando %s para imprimir cadenas.
    
    return 0;
} 
 */    

