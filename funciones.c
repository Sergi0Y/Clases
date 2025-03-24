//Suma
/* 
#include <stdio.h>

//los nombres de las funciones idelmente tienen que explicar de la forma más breve posible que es lo que hace la misma
void sumar(int num1, int num2)
{
    printf("%d\n", num1 + num2);
}

int main()
{
    sumar(1,2);
    sumar(3,4);
    return 0;
} */

// MULTIPLICACIÓN

#include <stdio.h>

int multiplicar (int num1, int num2){
    return num1 * num2;
}

int main (){
    //printf("%d", multiplicar(3,4));

    int resultado = multiplicar(3,4);
    printf("%d", resultado);
    return 0; 
}