def car(x):
    return x[0]

def cdr(x):
    return x[1:]

def cons(x,y):
    return [x] + y

def valoresNaFaixa(vals,min,max):
    if vals == []:
        return []
    else:
        if car(vals) > min and car(vals) < max:
            return cons(car(vals),valoresNaFaixa(cdr(vals),min,max))
        else:
            return valoresNaFaixa(cdr(vals),min,max)

numeros = [2, 7, 5, 4, 1, 8, 9, 6, 3, 8, 9, 4, 2, 5, 7, 9, 2, 5, 4, 5, 4]

#retorna os valores na faixa especificada
print('valores na faixa:',valoresNaFaixa(numeros,4,8))