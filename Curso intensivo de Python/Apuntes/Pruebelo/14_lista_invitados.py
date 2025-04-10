invitados_cena = ['Elon Musk', 'Steve Jobs', 'Tyler Joseph']

print(f'Hola {invitados_cena[0]} te invito a cenar')
print(f'Hola {invitados_cena[1]} te invito a cenar')
print(f'Hola {invitados_cena[2]} te invito a cenar')

print(f'{invitados_cena[1]} no podra asistir a la cena')
invitados_cena[1] = 'Stephen Hawking'

print(f'Hola {invitados_cena[0]} te invito a cenar')
print(f'Hola {invitados_cena[1]} te invito a cenar')
print(f'Hola {invitados_cena[2]} te invito a cenar')

print(f'Acabamos de encontrar una mesa más grande, por lo que invitaré a más personas')
invitados_cena.insert(0, 'Michael Jackson')
invitados_cena.insert(1, 'Albert Einstein')
invitados_cena.append('Keanu Reeves')
print(f'Hola {invitados_cena[0]} te invito a cenar')
print(f'Hola {invitados_cena[1]} te invito a cenar')
print(f'Hola {invitados_cena[2]} te invito a cenar')
print(f'Hola {invitados_cena[3]} te invito a cenar')
print(f'Hola {invitados_cena[4]} te invito a cenar')
print(f'Hola {invitados_cena[5]} te invito a cenar')

print(f'La mesa no llega a tiempo, por lo que solo podre invitar a dos personas')
print(f'Lo siento {invitados_cena.pop()}, no podras asistir a la cena')
print(f'Lo siento {invitados_cena.pop()}, no podras asistir a la cena')
print(f'Lo siento {invitados_cena.pop()}, no podras asistir a la cena')
print(f'Lo siento {invitados_cena.pop()}, no podras asistir a la cena')

print(f'El numero de invitados es: {len(invitados_cena)}')

del invitados_cena[0]
del invitados_cena[0]
print(invitados_cena)