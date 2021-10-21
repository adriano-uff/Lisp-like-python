def car(x):
    return x[0]

def cdr(x):
    return x[1:]

def cons(x,y):
    return [x] + y

def quantidade(val):
    if val == []:
        return 0
    else:
        return 1 + quantidade(cdr(val))

def menorValor(vals):
    if vals == []:
        return []
    if quantidade(vals) == 1:
        return car(vals)
    if car(vals) < car(cdr(vals)):
        return menorValor(cons(car(vals),cdr(cdr(vals))))
    else:
        return menorValor(cdr(vals))

def maiorValor(vals):
    if vals == []:
        return []
    if quantidade(vals) == 1:
        return car(vals)
    if car(vals) > car(cdr(vals)):
        return maiorValor(cons(car(vals),cdr(cdr(vals))))
    else:
        return maiorValor(cdr(vals))

numeros = [2, 7, 5, 4, 8, 9, 5 , 6, 3, 8, 9, 4, 2, 5, 7, 9, 5, 2, 5, 4, 5, 4]

#retorna o menor e o maior da lista
print('menor valor da lista:',menorValor(numeros))
print('maior valor da lista:',maiorValor(numeros))