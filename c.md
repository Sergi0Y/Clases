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


### Configurar UTF-8

	chcp 65001

Este comando sirve para arreglar la codificación UTF-8 en powershell para poder ver correctamente los caracteres especiales ***(desde símbolos de monedas hasta emojis)***

---

# printf()

	int main(){
    char libro[]  = "El programador pragmático";
    printf(libro);
    return 0;
	}

En C, printf() espera un formato de salida. Sin embargo, ***en algunos casos***, si pasas directamente una variable de tipo string (arreglo de caracteres), el compilador y la función printf() pueden interpretarlo correctamente.

---
Si se dan cuenta en el siguiente código si aplico la sintaxis ***"%s"*** esto 
debido a que en la variable libro ya tengo un signo de porcentaje, printf() toma el primer argumento como una cadena de formato, lo que significa que si la cadena tiene % seguido de otra letra (%d, %s, etc.), printf() intentará interpretarlo como un formato y puede causar un error o un comportamiento inesperado.


	int main(){
    	char libro[]  = "El programador 100% pragmático.";
    	printf("%s",libro);
    	return 0;
	}

## Especificadores de formato:
***Resumen: ***

	Enteros: %d, %i, %u, %x, %o
	Flotantes: %f, %e, %g
	Cadenas y caracteres: %s, %c
	Punteros: %p
	Largos: %ld, %lu, %lld, %llu
	Porcentaje: %%

### 1. Enteros
&bull; %d: Imprime un entero con signo (por ejemplo, -5 o 42)

	int num = 42;
	printf("%d\n", num);  // Imprime: 42

&bull; %i: También imprime un entero con signo. Es equivalente a %d.

	int num = -10;
	printf("%i\n", num);  // Imprime: -10

&bull; %u: Imprime un entero sin signo (es decir, solo valores positivos).

	unsigned int num = 100;
	printf("%u\n", num);  // Imprime: 100

&bull; %x: Imprime un entero en formato hexadecimal (letras en minúsculas).

	int num = 255;
	printf("%x\n", num);  // Imprime: ff

&bull; %X: Imprime un entero en formato hexadecimal (letras en mayúsculas).

	int num = 255;
	printf("%X\n", num);  // Imprime: FF

&bull; %o: Imprime un entero en formato octal (base 8).

	int num = 8;
	printf("%o\n", num);  // Imprime: 10

&bull; %ld: Imprime un entero largo con signo.

	long num = -100000L;
	printf("%ld\n", num);  // Imprime: -100000

&bull; %lu: Imprime un entero largo sin signo.

	unsigned long num = 100000L;
	printf("%lu\n", num);  // Imprime: 100000


&bull; %ld: Imprime un entero largo largo con signo.

	long num = -1234567890;
	printf("%lld\n", num);  // Imprime: -1234567890

&bull; %lu: Imprime un entero largo largo sin signo.

	unsigned long num = 1234567890;
	printf("%llu\n", num);  // Imprime: 1234567890

### 2. Floats

&bull; %f: Imprime un número de punto flotante en formato decimal.

	float num = 3.14;
	printf("%f\n", num);  // Imprime: 3.140000


&bull; %e: Imprime un número en notación científica (en minúsculas).

	float num = 123456.789;
	printf("%e\n", num);  // Imprime: 1.234568e+05


&bull; %E: Imprime un número en notación científica (en mayúsculas).

	float num = 123456.789;
	printf("%E\n", num);  // Imprime: 1.234568E+05


&bull; %g: Imprime un número en formato normal o en notación científica, dependiendo de cuál sea más compacto.

	float num = 0.000123;
	printf("%g\n", num);  // Imprime: 0.000123

&bull; %.2f\n Especifica cuántos decimales mostrar en un número flotante

	printf("%.2f\n", 3.14159);  // Imprime: 3.14
	printf("%.3f\n", 3.14159);  // Imprime: 3.141

### 3. Caracteres y cadenas

&bull; %c: Imprime un solo carácter.

	char letra = 'A';
	printf("%c\n", letra);  // Imprime: A

&bull; %s: Imprime una cadena de caracteres (se asume que la cadena está terminada en \0).

	char str[] = "Hola, mundo!";
	printf("%s\n", str);  // Imprime: Hola, mundo!

### 4. Punteros y direcciones de memoria

&bull; %p: Imprime una dirección de memoria (dirección de un puntero).

	int num = 42;
	int *ptr = &num;
	printf("%p\n", ptr);  // Imprime la dirección de memoria de ptr
