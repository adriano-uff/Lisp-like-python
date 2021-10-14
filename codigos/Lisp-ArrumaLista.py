def car(x):
    return x[0]

def cdr(x):
    return x[1:]

def cons(x,y):
    return [x] + y

def ehAtomo(x):
    return not isinstance(x, list)

def soma(vals):
    if vals == []:
        return 0
    else:
        if ehAtomo(car(vals)):
            return car(vals) + soma(cdr(vals))
        else:
            return soma(car(vals)) + soma(cdr(vals))

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

# PP
valores = [[3, 6, 7], [[[8, 4], 0]], [1, 10], 88,[[3,[2,4]]], [44]]
print("antes: ", valores)
print("depois: ", emagrece(valores))
print('soma:',soma(valores))