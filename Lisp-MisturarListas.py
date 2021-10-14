def car(x):
    return x[0]

def cdr(x):
    return x[1:]

def cons(x, y):
    return [x] + y

def acharLugar(x, lista1):
    if lista1 == []:
        return cons(x, lista1)
    elif x > car(lista1):
        return cons(car(lista1), acharLugar(x, cdr(lista1)))
    elif x <= car(lista1):
        return cons(x,lista1)

def misturar(lis1, lis2):
    if lis2 == []:
        return lis1
    if lis1 == []:
        return lis2
    else:
        return misturar(acharLugar(car(lis2), lis1), cdr(lis2))

a = [1,3,5,7,9]
b = [2,4,6,8]
print(misturar(a, b))