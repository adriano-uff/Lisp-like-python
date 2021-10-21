def car(x):
    return x[0]

def cdr(x):
    return x[1:]

def cons(x,y):
    return [x] + y

def menoresqueValor(vals, valor):
    if vals == []:
        return []
    else:
        if car(vals) < valor:
            return cons(car(vals),menoresqueValor(cdr(vals), valor))
        else:
            return menoresqueValor(cdr(vals), valor)

def maioresqueValor(vals, valor):
    if vals == []:
        return []
    else:
        if car(vals) > valor:
            return cons(car(vals),maioresqueValor(cdr(vals), valor))
        else:
            return maioresqueValor(cdr(vals), valor)

numeros = [2, 7, 5, 4, 10, 8, 9, 5 , 6, 3, 8, 15, 4, 1, 5, 7, 5, 2]

#retornar apenas os valores maiores e menores que os escolhidos
print('menor que o valor escolhido:',menoresqueValor(numeros,4))
print('maiores que o valor escolido:',maioresqueValor(numeros,8))