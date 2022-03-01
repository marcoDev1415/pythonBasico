
# Creador Marco Antonio Mena Landa

def principal():

 objetivo = int(input('ingresa un numero: '))
 respuesta=0

 while respuesta**2 < objetivo:
      respuesta +=1
      print(respuesta)

 if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
 else:
    print(f'{objetivo} no tiena una raiz cuadrada')


if __name__ == '__main__':
    principal()

