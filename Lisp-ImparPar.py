def car(x):
    return x[0]

def cdr(x):
    return x[1:]

def cons(x,y):
    return [x] + y

def pares(vals):
    if vals == []:
        return []
    else:
        if car(vals) % 2 == 0:
            return cons(car(vals),pares(cdr(vals)))
        else:
            return pares(cdr(vals))

def impares(vals):
    if vals == []:
        return []
    else:
        if car(vals) % 2 != 0:
            return cons(car(vals),impares(cdr(vals)))
        else:
            return impares(cdr(vals))

numeros = [2, 7, 5, 4, 1, 8, 9, 5 , 6, 3, 8, 9, 4, 2, 5, 7, 9, 5, 2, 5, 4, 5, 4]

print('pares:',pares(numeros))
print('impares:',impares(numeros))