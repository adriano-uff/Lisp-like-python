def car(x):
    return x[0]

def cdr(x):
    return x[1:]

def cons(x, y):
    return [x] + y

def quantidade(val):
    if val == []:
        return 0
    else:
        return 1 + quantidade(cdr(val))

def comparar(pivot,lista):
    if pivot > car(lista):
        return cons(car(lista),separar(cons(pivot,cdr(lista))))
    else:
        return cons(pivot,separar(lista))

def separar(vals):
    if cdr(vals) == []:
        return vals
    else:
        return comparar(car(vals),cdr(vals))

def bubblesort(n,vals):
    if n < 1:
        return vals
    else:
        return bubblesort(n-1,separar(vals))


numeros = [11,9,10,8,20,150,4,3,2,1,0,5]

#organizar em ordem crescente
print(bubblesort(quantidade(numeros),numeros))