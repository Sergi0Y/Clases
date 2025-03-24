// 1.- PUNTEROS


/* #include <stdio.h>

int main()
{
   // --------
   //puntero -> type *name 
    int var = 1;  //casa
    int *puntero = &var; //mapa
    printf("valor de variable: %d\n", var);
    printf("direccion de memoria de var: %p\n", &var);
    printf("puntero que tiene la dirección de memoria: %d\n", puntero);
    printf("valor a través del puntero: %d\n", *puntero);
    return 0;
}
 */    //--------




// 2.- CICLO RECORRER ARRAY
 /* 
    //--------

    //puntero -> type *name
    // son 4 debido a que los arrays siempre es uno más que hace referencia al final de éste que es \0
    /*
#include <stdio.h>
    int main (){
    
     char *animales[4] = {"gorrión", "gato", "perro", "pez"};
    
    
    no asignar esto espera que alguien se de cuenta
    int = i -> malo
    int i; -> bueno

    int i;

    for (i = 0; i < 4; i++)
    {
        printf("%s\n, animales[i]);
    }

    //Segunda forma de escribir un bucle pequeño
    for (i = 0; i <4; i++) printf("%s\n, animales[i]);

    
        return 0;
    }
 */



// 3.- ESPECIFICADOR FORMATO STRING 
/* 
#include <stdio.h>
    int main()
{
    char libro[2] = "El programador 100% pragmático";
    printf("%s", libro);
    return 0;
} */