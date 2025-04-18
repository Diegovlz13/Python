# Una lista es una colección de elementos y se define entre corchetes []
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Para acceder a un elemento de la lista se utiliza el índice, que empieza en 0
print(bicycles[0])  # Accede al primer elemento
print(bicycles[2].title())  # Accede al tercer elemento y lo convierte a mayúsculas la primera letra

# Para acceder a los elementos de la lista desde el final se utilizan índices negativos
print(bicycles[-1])  # Accede al último elemento
print(bicycles[-2])  # Accede al penúltimo elemento y así sucesivamente

# Uso de listas junto a cadenas f strings
message = f'My first bicycle was a {bicycles[0].title()}'
print(message)

# Cambiar el valor de un elemento de la lista
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'  # Cambia el primer elemento
print(motorcycles)

# Añadir elementos a la lista
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')  # Añade un elemento al final de la lista
print(motorcycles)

# Insertar un elemento en una posición específica
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0, 'ducati')  # Inserta un elemento en la posición 0
print(motorcycles)

# Eliminar un elemento de la lista en una posición específica
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]  # Elimina el elemento en la posición 1
print(motorcycles)

# Eliminar el último elemento de la lista y trabajarlo
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()  # Elimina el último elemento y lo guarda en una variable
print(motorcycles)
print(f'The last motorcycle I owned was a {popped_motorcycle.title()}')
# Tambien se puede eliminar un elemento en una posición específica
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop(0)  # Elimina el elemento en la posición 1 y lo guarda en una variable
print(motorcycles)
print(f'The first motorcycle I owned was a {popped_motorcycle.title()}')

# Eliminar mediante el valor - solo se elimina la primera coincidencia
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')  # Elimina el elemento con el valor 'ducati'
print(motorcycles)

# Ordenar una lista alfabeticamente 
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)  
# Ordenar una lista en orden inverso
cars.sort(reverse=True)  # Ordena la lista en orden inverso
print(cars)
# Ordenar una lista temporalmente
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))  # Ordena la lista temporalmente
print(cars)  # La lista original no se modifica

# Invertir el orden de los elementos de la lista
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() 
print(cars) 

# Obtener la longitud de una lista
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))  # Devuelve la longitud de la lista

# Nota: Las listas generar errores si el indice esta fuera de rango.
# Nota: Para acceder al último elemento de una lista se puede usar el índice -1, pero si esta vacía generará un error.


