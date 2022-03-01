

# Autor Marco Antonio Mena

# Raiz con aproximacion

def principal():

    objetivo = int(input('Escoge un numero:'))
    epsilon = 0.01 # presion

    paso= epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta<=objetivo:
        respuesta += paso
        print(respuesta)

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f"Nose encontro la raiz cuadrada {objetivo}")
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

if __name__ == '__main__':
    principal()

