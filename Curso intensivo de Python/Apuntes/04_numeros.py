# Números en Python
entero = 10
print(entero)
print(type(entero))

decimal = 10.5
print(decimal)
print(type(decimal)) # Muestra el tipo de dato

complejo = 3 + 4j
print(complejo)
print(type(complejo))

# Convertir un número decimal a entero
entero = int(decimal)
print(entero)
print(type(entero))
# Convertir un número entero a decimal
decimal = float(entero)
print(decimal)
print(type(decimal))
# Operaciones con números enteros
print(10 + 5)
print(10 - 5) 
print(10 * 5) 
print(10 / 5) # Siempre devuelve un número decimal
print(10 ** 5) # Potencia
# Operaciones con números decimales
print(10.5 + 5.5)
print(10.5 - 5.5)
print(10.5 * 5.5)
print(10.5 / 5.5)
print(10.5 ** 5.5)
# Operación con ambos tipos de números
print(10 + 5.5) # Siempre devuelve un número decimal

# Una forma de representar números largos
universe_age = 14_000_000_000 # Solo lo hace más legible
print(universe_age) # Cuando lo imprime no muestra los guiones bajos

# Asignación múltiple
x, y, z = 1, 2, 3 # Sirve para asignar varios valores a varias variables
print(x, y, z)

# Constantes son valores que no cambian durante la ejecución del programa
PI = 3.14159 # Se recomienda usar mayúsculas para indicar que es una constante