# Una cadena es cualquier texto que va entre comillas simples o dobles
name = 'diego'
last_name = "velazquez"
# Se pueden utilizar comillas simples y dobles en una misma cadena
message = 'Le dije a mi amigo: "¡Python es mi lenguaje favorito!"'
print(message)
# Cambiar formato a título, mayúsculas y minúsculas
name = 'diego'
print(name.title()) # Diego
print(name.upper()) # DIEGO
print(name.lower()) # diego

# Unir cadenas
first_name = 'diego'
last_name = 'velazquez'
full_name = f'{first_name} {last_name}'
print(f'Hello, {full_name.title()}!') # Diego Velazquez!

# Tabulaciones y saltos de línea
print('\tPython')
print('Python\nC++\nJava\nJavaScript')

# Eliminar espacios en blanco al inicio y al final de una cadena
name = 'diego   '
print(name.rstrip()) # derecha
name = '   diego'
print(name.lstrip()) # izquierda
name = '   diego   '
print(name.strip()) # ambos lados