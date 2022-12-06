# a) Crear una función que tome una lista de valores flotantes,
# calcule la media de los valores y la devuelva como valor de retorno.

def media(valores = []):
    media = sum(valores) / len(valores)

    return media

# media([5.8, 10.2, 2.3, 35.1, 7.16])

# b) Crear una función que tome una lista de valores flotantes,
# calcule la mediana de los valores y la devuelva como valor de retorno.

def mediana(valores = []):

    ordenados = sorted(valores)
        
    if len(ordenados) % 2 != 0:
        mitad = int((len(ordenados) - 1) / 2)
        mediana = ordenados[mitad]
    else:
        mitad = int(len(ordenados) / 2)
        centro1 = ordenados[mitad]
        centro2 = ordenados[mitad + 1]
        mediana = round((centro1 + centro2) / 2, 2)

    return mediana

# flotantes([17.3, 42.12, 6.9, 37.1, 9.3, 5.87])

# c) Crear una función que tome una lista de valores flotantes
# y calcule la desviación estándar.

def std_dev(valores=[]):

    # Ecuación para tener presente
    # σ = √Σ(Xi - µ)²/(n - ­1)

    mean = sum(valores) / len(valores) # µ - letra griega 'mu' - es la sumatoria de los numeros del listado sobre la candtidad de numeros.
    sigma = 0 # Σ - letra griega 'sigma' mayúscula representa la sumatoria de los número del listado

    for i in range(len(valores)):
        sigma += (valores[i] - mean) ** 2 # Σ(Xi - µ)² - suma a sigma el resultado del cuadrado de la resta de binomio de cada búmero número en el listado

    std_dev = (sigma / (len(valores) - 1)) ** (1/2) # raíz cuadrada de la división de sigma sobre la cantidad de números 'n' menos 1 

    return std_dev

# std_dev([170, 155, 160, 185, 145])

# d) Crear un programa principal que cumpla con los siguientes puntos:
# i) Solicite que se ingrese por teclado el número de valores a ingresar.

def ingreso():
    num_valores = int(input('Ingrese el número de valores: '))

    while num_valores <= 1:
        num_valores = int(input('Ingrese un valor mayor a 1: '))
        continue

    return num_valores

num_valores = ingreso()
        
# ii) Crear una lista de valores flotantes ingresados por teclado. La lista
# debe tener tantos valores como indique el número obtenido en el punto anterior.

def flotantes():
    lista_float = []
    i = 0

    while i < num_valores:
        i += 1
        valor = input(f'Ingrese el valor Nº {i}: ')
        lista_float.append(int(valor))
        continue

    return lista_float

lista_float = flotantes()

# iii) Mostrar por pantalla los valores ingresados bajo el mensaje “Los
# valores son:” y luego los valores.

print('Los valores ingresados son:')
print(lista_float)

# iv) Calcular y mostrar por pantalla la media, la desviación estándar y la
# mediana de los valores.

media = media(lista_float)
std_dev = std_dev(lista_float)
mediana = mediana(lista_float)

print(f'- La media de {lista_float} es: {round(media, 2)}')
print(f'- La desviación estándar es: {round(std_dev, 2)}')
print(f'- La mediana es {mediana}.')