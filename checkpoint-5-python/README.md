# Documentación Técnica: Fundamentos de Python - Checkpoint 5

## Introducción

En esta documentación se explican algunos de los conceptos fundamentales de Python trabajados durante este bloque. El objetivo es ofrecer un material claro y detallado para personas que están comenzando en el mundo de la programación, explicando qué es cada concepto, para qué sirve, cómo se utiliza y mostrando ejemplos prácticos.

---

## 1. ¿Qué es un condicional y para qué sirve?

### Definición

Un condicional es una estructura de control que permite que un programa tome decisiones en función de si una condición es verdadera o falsa.

### ¿Para qué sirve?

Sirve para que el programa no ejecute siempre las mismas instrucciones, sino que pueda reaccionar de forma diferente según la situación.

### ¿Por qué se utiliza?

Sin condicionales, los programas serían completamente lineales y no podrían adaptarse a diferentes casos. Gracias a ellos, podemos crear lógica real dentro del programa.

### Ejemplos de uso

* Comprobar si un usuario ha introducido correctamente una contraseña
* Verificar si hay stock antes de vender un producto
* Determinar si un número es mayor o menor que otro

### Sintaxis

En Python se utilizan las palabras clave `if`, `elif` y `else`.

```python
edad = 20

if edad >= 18:
    print("Acceso permitido: Eres mayor de edad.")
else:
    print("Acceso denegado: Eres menor de edad.")
```

### Explicación del ejemplo

El programa comprueba si la variable `edad` es mayor o igual a 18.
Si la condición es verdadera, se ejecuta el primer bloque.
Si no, se ejecuta el bloque del `else`.

### Operadores de comparación

* `==` igual
* `!=` distinto
* `>` mayor que
* `<` menor que
* `>=` mayor o igual
* `<=` menor o igual

### Operadores lógicos

* `and` (y)
* `or` (o)
* `not` (no)

### Beneficios

* Permiten crear programas dinámicos
* Adaptan el comportamiento del programa
* Son fundamentales para la lógica de programación

---

## 2. Tipos de bucles en Python

### ¿Qué es un bucle?

Un bucle es una estructura que permite repetir un bloque de código varias veces sin tener que escribirlo repetidamente.

### ¿Por qué son útiles?

* Ahorran tiempo
* Evitan repetir código (principio DRY)
* Permiten trabajar con grandes cantidades de datos

### Bucle for

Se utiliza cuando sabemos cuántas veces queremos repetir una acción o cuando recorremos una colección.

```python
frutas = ["manzana", "pera", "plátano"]

for fruta in frutas:
    print(f"Me gusta comer {fruta}")
```

### Explicación

El bucle recorre la lista `frutas` y en cada iteración imprime un elemento.

### Bucle while

Se utiliza cuando no sabemos cuántas veces se repetirá el proceso.

```python
contador = 0

while contador < 5:
    print(f"El contador vale: {contador}")
    contador += 1
```

### Explicación

El bucle se ejecuta mientras `contador` sea menor que 5.
En cada vuelta, el contador aumenta en 1.

### Diferencias entre for y while

* `for`: cuando conocemos el número de repeticiones
* `while`: cuando depende de una condición

### Precaución

Si la condición de un `while` nunca deja de cumplirse, se crea un bucle infinito.

---

## 3. Listas por comprensión (List Comprehensions)

### Definición

Una lista por comprensión es una forma abreviada de crear listas en Python en una sola línea.

### ¿Para qué sirve?

Permite escribir código más limpio y eficiente.

### Sintaxis general

```python
[nueva_expresion for elemento in lista]
```

### Ejemplo

```python
numeros = [1, 2, 3, 4]

cuadrados = [n**2 for n in numeros]
```

### Forma tradicional

```python
cuadrados = []
for n in numeros:
    cuadrados.append(n**2)
```

### Explicación

La lista por comprensión hace lo mismo que el bucle, pero en una sola línea.

### Ejemplo con condición

```python
pares = [n for n in numeros if n % 2 == 0]
```

### Beneficios

* Código más corto
* Mejor legibilidad
* Mayor eficiencia

---

## 4. ¿Qué es un argumento en Python?

### Definición

Un argumento es el valor real que se pasa a una función cuando se llama.

### Diferencia entre parámetro y argumento

* Parámetro: variable definida en la función
* Argumento: valor que se envía al ejecutar la función

### Ejemplo

```python
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Maialen")
```

### Explicación

`nombre` es el parámetro.
`"Maialen"` es el argumento.

### ¿Por qué son importantes?

Permiten que las funciones trabajen con diferentes datos, haciendo el código reutilizable.

---

## 5. Funciones Lambda

### Definición

Una función lambda es una función pequeña y anónima que se define en una sola línea.

### Sintaxis

```python
lambda argumentos: expresion
```

### Ejemplo

```python
doble = lambda x: x * 2
print(doble(5))
```

### Explicación

La función recibe un valor y devuelve el doble.

### ¿Cuándo se usan?

* Operaciones simples
* Funciones temporales
* Como argumento en funciones como `map()` o `filter()`

### Diferencia con funciones normales

* `lambda`: corta y sin nombre
* `def`: más completa y reutilizable

---

## 6. ¿Qué es un paquete pip?

### Definición

`pip` es el gestor de paquetes de Python que permite instalar, actualizar y eliminar librerías externas.

### ¿Qué es PyPI?

PyPI (Python Package Index) es el repositorio donde se encuentran la mayoría de paquetes disponibles para Python.

### ¿Para qué sirve?

Permite reutilizar código creado por otros desarrolladores y ahorrar tiempo.

### Comandos básicos

```bash
pip install nombre_del_paquete
pip list
pip uninstall nombre_del_paquete
```

### Ejemplo real

```bash
pip install requests
```

### Beneficios

* Ahorro de tiempo
* Acceso a miles de librerías
* Facilita el desarrollo

---

## 🛠️ Ejercicios Prácticos

### 1. Bucle for

```python
for i in range(1, 6):
    print(f"Iteración número: {i}")
```

### 2. Función suma con 3 argumentos

```python
def suma(a, b, c):
    return a + b + c

print(suma(10, 5, 2))
```

### 3. Función lambda equivalente

```python
suma_lambda = lambda a, b, c: a + b + c
print(suma_lambda(10, 5, 2))
```

### 4. Búsqueda en lista

```python
nombre_buscado = "Enrique"
lista_nombres = ["Jessica", "Paul", "George", "Henry", "Adán"]

if nombre_buscado in lista_nombres:
    print(f"{nombre_buscado} sí está en la lista.")
else:
    print(f"{nombre_buscado} no se encuentra en la lista.")
```

### Explicación

Se utiliza el operador `in` para comprobar si el nombre está dentro de la lista.

---

## Conclusión

En este documento se han explicado conceptos fundamentales de Python como condicionales, bucles, listas por comprensión, argumentos, funciones lambda y el uso de pip. Estos conceptos son esenciales para desarrollar programas más complejos y eficientes, y forman la base del aprendizaje en programación.
