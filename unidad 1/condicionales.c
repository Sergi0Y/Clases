// IF - ELSE IF

/* #include <stdio.h>
int main (){

   int entero = 9;
   if (entero == 99){
    printf("Es 99");
   }
   else if (entero == 100){
    printf("Es 100");
   }else{
    printf("No es ni 99 ni 100");
   }
   return 0;
} */

// SWITCH

/* #include <stdio.h>
int main()
{
    char color;

    // switch sólo acepta int y char
    switch (color)
    {
    //importante usar comillas simples
    case 'V':
        printf("Éxito");
        break;
    case 'A':
        printf("Advertencia");
        break;

    default:
        printf("Error");
        break;
    }
    return 0;
} */
//con menu
/* #include <stdio.h>
int main()
{
    char color;
    printf("*********************\n");
    printf("ingrese \"A\" para Éxito\n\"V\" para Advertencia\nCualquier otro caracter para Error\n");
    printf("*********************\n\n");
    printf("ingrese un valor: ");
    scanf(" %c", &color);

        // switch acepta int y char
        switch (color)
    {
    case 'V':
        printf("Éxito");
        break;
    case 'A':
        printf("Advertencia");
        break;

    default:
        printf("Error");
        break;
    }
    return 0;
} */


// BUCLE WHILE 

    // contador while

#include <stdio.h>


int main (){
    int entero = 100;
    int num = 110;

    while (entero <= num){
        printf("%d\n", entero);
        entero++;
    }

    return 0;
}