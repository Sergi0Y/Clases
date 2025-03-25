//IMPRIMIR CHAR Y NUM

/* #include <stdio.h>

int main()
{
    int numeros[5] = {1, 2, 3, 4, 5};    
    int myNum = 15;
    char myLetter = 'D';
    printf("My number is %d and my letter is %c", myNum, myLetter);
    return 0;
} */
dsfsd

//PRINT Y SCANF
/*  
#include <stdio.h>

int main() {
    int num1;
    int num2;
    printf("Ingresa el primer número: ");
    scanf("%d", &num1);
    printf("Ingresa el segundo número: ");
    scanf("%d", &num2);

    int suma = num1 + num2 ;

    printf("tu primer número es: %d\n", num1);
    printf("tu segundo número es: %d\n", num2);
    printf("la suma es: %d\n", suma );
return 0;
 } 

*/


// USAR CHAR COMO STRING

#include <stdio.h>

int main () {
    char* name = "aafsdfsdfsd";
    printf("%s", name);
    
    return 0;
}

/* El asterisco (*) en char* indica que la variable es un puntero, lo que permite manejar cadenas de texto almacenadas en memoria. No convierte un char en string, sino que simplemente apunta al primer carácter de una cadena, lo que permite que printf("%s", name); imprima toda la cadena hasta encontrar \0 (carácter nulo).
 */ 
