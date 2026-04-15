# Mi Documentación de Python - Checkpoint 5

Hola! Soy Maialen. He preparado esta documentación para explicar los conceptos básicos de Python que hemos visto en este módulo. Mi idea es que sea una guía sencilla para cualquier persona que esté empezando en el equipo. Espero que os ayude!

---

## 1. ¿Qué es un condicional? 
Un condicional es como un semáforo en el código. Permite que el programa tome decisiones: "Si pasa esto, haz aquello; si no, haz esto otro".

* **¿Para qué sirve?** Para que el programa no sea siempre lineal y pueda reaccionar a diferentes situaciones (por ejemplo, dejar pasar a un usuario solo si su edad es correcta).
* **Sintaxis:** Usamos `if`, `elif` y `else`.

**Ejemplo:**

```python
edad = 20

if edad >= 18:
    print("Eres mayor de edad, puedes pasar.")
else:
    print("Eres menor de edad, vuelve a casa.")
```

## 2. Los Bucles: For y While 
Los bucles sirven para repetir una tarea muchas veces sin tener que escribir el mismo código una y otra vez. ¡Nos ahorran muchísimo trabajo y evitan errores!

Bucle for: Lo usamos cuando sabemos cuántas veces queremos repetir algo o para recorrer una lista de elementos.

Bucle while: Se repite mientras una condición sea verdadera. Hay que tener cuidado para que no se quede infinito.

¿Por qué son útiles? Porque si tienes que imprimir 100 nombres, con un bucle lo haces en 2 líneas en lugar de 100.

## 3. Listas por Comprensión 
Esto me pareció un lío al principio, pero en verdad es solo un "truco" para crear listas nuevas a partir de otras en una sola línea. Es mucho más limpio y elegante.

**Ejemplo comparativo:**

```Python
numeros = [1, 2, 3]

# Forma normal con bucle
dobles = []
for n in numeros:
    dobles.append(n * 2)

print(dobles)
```

```python
numeros = [1, 2, 3]

# Con lista por comprensión
dobles = [n * 2 for n in numeros]

print(dobles)
```

## 4. ¿Qué es un argumento? 
Un argumento es el "dato" o la información que le pasamos a una función para que pueda hacer su trabajo.

Piensa en una función que suma números: los números que le das son los argumentos. Si no le das los datos, la función no tiene nada con lo que operar. Es la "materia prima" de nuestras funciones.

## 5. ¿Qué es una función lambda? 
Las funciones Lambda son como "funciones de bolsillo". Son anónimas (no tienen nombre) y se escriben en una sola línea de código.

Se usan para tareas muy sencillas y rápidas. Cuando no quieres crear una función completa con def porque solo vas a usar esa lógica una vez, usas una lambda.

## 6. ¿Qué es un paquete PIP? 
PIP es el gestor de paquetes de Python. Imagina que es como una "App Store" para programadores.

¿Para qué sirve? Para instalar librerías o herramientas que otros desarrolladores ya han creado (como para manejar bases de datos o crear gráficos). Solo tienes que escribir pip install nombre_del_paquete y ya puedes usarlo sin tener que inventar tú la rueda.

## 7. Ejercicios prácticos
A continuación, presento la resolución de los ejercicios prácticos solicitados:

### 1. Bucle `for`

```python
for i in range(5):
    print(f"Estamos en el paso número {i}")
```

### 2. Función suma con 3 argumentos

```python
def mi_suma(a, b, c):
    return a + b + c

resultado = mi_suma(10, 5, 2)
print("El resultado de mi suma es:", resultado)
```

### 3. Función lambda equivalente

```python
suma_rapida = lambda a, b, c: a + b + c
print("Suma con lambda:", suma_rapida(10, 5, 2))
```

### 4. Comprobación de nombre en lista

```python
nombre_buscado = "Enrique"
lista_nombres = ["Jessica", "Paul", "George", "Henry", "Adán"]

if nombre_buscado in lista_nombres:
    print(f"¡Sí! {nombre_buscado} está en la lista.")
else:
    print(f"Vaya, parece que {nombre_buscado} no aparece por aquí.")
```
Documentación creada por Maialen Sarasola para el Checkpoint 5.
