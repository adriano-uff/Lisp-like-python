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

numeros = [2, 7, 5, 4, 1, 8, 9, 5 , 6, 3, 8, 9, 4, 2, 5, 7, 9, 5, 2, 5, 4, 5, 4]

#retorna a quantidade de valores
print('quantidade:',quantidade(numeros))