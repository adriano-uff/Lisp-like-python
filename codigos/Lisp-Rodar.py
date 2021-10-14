def car(x):
    return x[0]

def cdr(x):
    return x[1:]

def cons(x,y):
    return x + [y]

def rodar(vals,qtd):
    if vals == []:
        return []
    else:
        if cdr(vals) == []:
            return vals
        else:
            if qtd == 0:
                return vals
            else:
                return operacao(vals,qtd)

def operacao(vals,qtd):
    if qtd > 0:
        return operacao(cons(cdr(vals),car(vals)),qtd - 1)
    else:
        return vals

lista = [1,2,3,4,5]
qtd = 2
print(rodar(lista,qtd))