#include <stdio.h>
#include <string.h>

/* 
La información de los empleados de la empresa IPSYSTEM está almacenada en una variable de tipo struct llamada “empleado”. La información con que se cuenta de cada empleado es: id, nombre y sueldo.
Por tanto se pide: Realizar un programa en C que lea un array de estructuras con los datos de los N trabajadores de la empresa y que imprima los datos del empleado que tenga el mayor y menor salario.


 */

struct empleado{
    int id;
    char name[25];
    int salary;
  
};

int main(){    

struct empleado emp[100];

int cantE;
int hSalary;
char hSName[25]; //IMPORTANTE MISMA CANTIDAD DE CARACTERES
printf("Ingrese la cantidad de empleados a ingresar: ");
scanf("%d", &cantE);

    for (int i = 0; i < cantE; i++)
    {
        printf("\nIngrese id del empleado N°%d: ", i+1);        
        scanf("%d", &emp[i].id);    
        while (getchar() != '\n'); // Limpiar buffer

        printf("Ingrese nombre del empleado N°%d :", i+1);
        fgets(emp[i].name, sizeof(emp[i].name), stdin);

        emp[i].name[strcspn(emp[i].name, "\n")] = '\0'; // limpiar el salto de línea después de fgets        
        //Esto es importante al momento de copiar o comparar cadenas de texto ya que pueden aparecer errores solamente con el salto de línea adicional

        printf("Ingrese sueldo del empleado N°%d: ", i+1);
        scanf("%d", &emp[i].salary);
             
    }

    hSalary = emp[0].salary;    
    for (int i = 0; i < cantE; i++)
    {        
        if(hSalary<emp[i].salary){  
            hSalary = emp[i].salary;        
            strcpy(hSName, emp[i].name);            
        }

    }
    
    printf("El trabajador con mayor salario es %s y su salario es: %d",hSName, hSalary);
    

  /*   for (int i = 0; i < cantE; i++)
    {
        printf("\nEl id del empleado n° %d es: %d\n", emp[i].id, emp[i].id);        
        printf("El nombre del usuario n°%d es: %s",emp[i].id, emp[i].name);
        printf("El saldo del usuario n°%d es: %d\n",emp[i].id, emp[i].salary);        
    } */
    
    return 0;
}   
