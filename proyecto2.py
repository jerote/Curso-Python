import PIL
import qrcode
import sys
import time

def generar_codigo():
    print('Vamos a generar un codigo QR')
    time.sleep(2)
    codificar = input('Meté una URL para hacer el QR: ')
    print('Codificando...')
    time.sleep(4)
    img = qrcode.make(codificar)
    nombre = input('Ingresá el ombre del QR: ')
    f = open(f'{nombre}_QR.png', 'wb')
    img.save(f)
    f.close()
    
    print(f'QR {nombre}_QR.png')
    time.sleep(2)
    preguntar_opcion()
    
def preguntar_opcion():
    while True:
        opcion = input('Querés otro QR? S/N: ').casefold()
        if opcion == 'n':
            time.sleep(0.5)
            print('Listo')
            sys.exit()
        elif opcion == 's':
            generar_codigo()
        else:
            print('Sí o Nó 😐')
            
generar_codigo()