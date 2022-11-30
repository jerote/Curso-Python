# Ejercicio 3.3.a

def norma_del_vector(x=int(), y=int()):
    norma = (x**2 + y**2)//2
    return norma
    
norma_del_vector(6, 95)

# Ejercicio 3.3.b

def resta_de_ambos(x1=int(), y1=int(), x2=int(), y2=int()):
    max1, min1 = max((x1, y1)), min((x1, y1))
    max2, min2 = max((x2, y2)), min((x2, y2))

    resta_de_ambos = max1 - min1, max2 - min2
    return resta_de_ambos

print(resta_de_ambos(x1=54, y1=120, x2=35, y2=42))

# print(resta_de_ambos())

# Ejercicio 3.3.c

# def distancia():
#     distancia = norma_del_vector
#     print(distancia())

# print(resta_de_ambos())

