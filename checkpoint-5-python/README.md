# Checkpoint 5 - Introducción a Python

## 1. ¿Qué es un condicional?

Un condicional es una estructura que permite que un programa tome decisiones.

### ¿Para qué sirve?
Un condicional se usa para que el programa haga una cosa u otra según se cumpla una condición.

### Sintaxis
```python
if condicion:
    # código
elif otra_condicion:
    # código
else:
    # código
Ejemplo

edad = 20

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

Explicación sencilla

Python comprueba si la condición es verdadera. Si lo es, ejecuta un bloque de código, si no, ejecuta otro. Al principio este tema puede parecer muy básico, pero ayuda mucho para entender cómo toma decisiones un programa.

2. ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

Los principales bucles en Python son for y while.

¿Para qué sirven?

Al principio me costó diferenciar for y while, sirven para repetir acciones sin tener que escribir el mismo código muchas veces.

Sintaxis
for variable in secuencia:
    # código
while condicion:
    # código
Ejemplo
for numero in range(5):
    print(numero)
contador = 0

while contador < 5:
    print(contador)
    contador += 1
Explicación sencilla

El bucle for se usa cuando sabemos cuántas veces repetir algo. El while se usa mientras una condición sea verdadera. A mí esta parte al principio me costó un poco más, sobre todo diferenciar cuándo usar `for` y cuándo usar `while`.

3. ¿Qué es una lista por comprensión en Python?

Es una forma rápida de crear listas en una sola línea.

¿Para qué sirve?

Sirve para crear listas de forma más sencilla y rápida.

Sintaxis
[nuevo_elemento for elemento in secuencia]
Ejemplo
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]

print(cuadrados)
Explicación sencilla

Se crea una nueva lista usando otra lista y aplicando una operación a cada elemento.

4. ¿Qué es un argumento en Python?

Un argumento es un valor que se pasa a una función.

¿Para qué sirve?

Sirve para que la función trabaje con diferentes datos.

Sintaxis
funcion(argumento)
Ejemplo
def saludar(nombre):
    print("Hola " + nombre)

saludar("Maialen")
Explicación sencilla

"Maialen" es el valor que se le pasa a la función para que la use.

5. ¿Qué es una función lambda en Python?

Es una función pequeña sin nombre.

¿Para qué sirve?

Sirve para hacer operaciones simples en una sola línea.

Sintaxis
lambda argumentos: expresion
Ejemplo
suma = lambda a, b: a + b
print(suma(2, 3))
Explicación sencilla

Hace lo mismo que una función normal pero de forma más rápida y corta.

6. ¿Qué es un paquete pip?

pip es el gestor de paquetes de Python.

¿Para qué sirve?

Se usa para instalar librerías de Python que luego podemos utilizar en el código. 

Sintaxis
pip install nombre_paquete
Ejemplo
pip install requests
Explicación sencilla

Con pip puedes instalar herramientas ya hechas por otros desarrolladores.

Conclusión

En este trabajo se han explicado conceptos básicos de Python como los condicionales, los bucles, las listas por comprensión, los argumentos, las funciones lambda y el uso de pip.