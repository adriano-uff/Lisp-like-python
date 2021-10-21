def car(x):
    return x[0]

def cdr(x):
    return x[1:]

def cons(x,y):
    return [x] + y

def ehAtomo(x):
    return not isinstance(x, list)

def emagrece(vals):
    if vals == []:
        return []
    else:
        if ehAtomo(car(vals)):
            return cons(car(vals), emagrece(cdr(vals)))
        else:
            return concatena(emagrece(car(vals)), emagrece(cdr(vals)))

def concatena(valsA, valsB):
    if valsA == []:
        return valsB
    else:
        if valsB == []:
            return valsA
        else:
            return cons(car(valsA), concatena(cdr(valsA), valsB))

valores = [[3, 6, 7], [[[8, 4], 0]], [1, 10], 8,[[3,[2,4]]], [9]]

#arrumar o emaranhado de listas em uma unica lista
print("antes: ", valores)
print("depois: ", emagrece(valores))