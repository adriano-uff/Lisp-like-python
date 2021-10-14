def car(x):
    return x[0]

def cdr(x):
    return x[1:]

def cons(x,y):
    return [x] + y

def quantidade(vals):
    if vals == []:
        return 0
    else:
        return contarSubLista(car(vals)) + quantidade(cdr(vals))

def contarSubLista(vals):
    if vals == []:
        return 0
    else:
        return 1 + contarSubLista(cdr(vals))



def somalinha(vals):
    if vals == []:
        return 0
    else:
        return car(vals) + somalinha(cdr(vals))

def somarlinhasMatriz(vals):
    if vals == []:
        return []
    else:
        return cons(somalinha(car(vals)),somarlinhasMatriz(cdr(vals)))

def somarListadeSomas(vals):
    if vals == []:
        return 0
    else:
        return car(somarlinhasMatriz(vals)) + somarListadeSomas(cdr(vals))

def mediaDaMatriz(vals):
    if vals == []:
        return []
    else:
        return somarListadeSomas(vals) / quantidade(vals)

listasimples = [1,2,3,4,5]
numeros = [[1,1,1],[3,3,3],[2,2,2]]


print(contarSubLista(numeros))
print(quantidade(numeros))
print(somarlinhasMatriz(numeros))
print(somarListadeSomas(numeros))
print(mediaDaMatriz(numeros))