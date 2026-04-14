# 1. Crear un bucle for de Python

for numero in range(5):
    print(numero)


# 2. Crear una función llamada suma que tome 3 argumentos y devuelva la suma

def suma(a, b, c):
    return a + b + c

resultado = suma(2, 3, 4)
print("Resultado de la suma:", resultado)


# 3. Crear una función lambda con la misma funcionalidad

suma_lambda = lambda a, b, c: a + b + c

resultado_lambda = suma_lambda(2, 3, 4)
print("Resultado con lambda:", resultado_lambda)


# 4. Comprobar si "Enrique" está en la lista

nombre = "Enrique"
lista_nombre = ["Jessica", "Paul", "George", "Henry", "Adán"]

if nombre in lista_nombre:
    print(nombre, "está en la lista")
else:
    print(nombre, "no está en la lista")