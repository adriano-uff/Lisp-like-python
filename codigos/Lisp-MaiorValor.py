def car(x):
    return x[0]

def cdr(x):
    return x[1:]

def cons(x,y):
    return [x] + y

def quantidade(vals):
    if vals == []:
        return 0
    else:
        return 1 + quantidade(cdr(vals))

def maiordalinha(vals):
    if vals == []:
        return []
    else:
        if quantidade(vals) == 1:
            return car(vals)
        else:
            if car(vals) > car(cdr(vals)):
                return maiordalinha(cons(car(vals),cdr(cdr(vals))))
            else:
                return maiordalinha(cdr(vals))

def maioresdaslinhas(vals):
    if vals == []:
        return []
    else:
        return cons(maiordalinha(car(vals)),maioresdaslinhas(cdr(vals)))

def maiorabsoluto(vals):
    if vals == []:
        return []
    else:
        return maiordalinha(maioresdaslinhas(vals))

#primeiro acha os maiores de cada linha, junta os em uma lista, e depois acha o maior dessa lista (maior dos maiores)
#fique atento ao car(vals), as vezes ele pode ser uma lista [1,2,3]

numeros = [[90,8,7],[4,5,6],[1,20,3],[1,2,3]]
listasimples = [1,2,9]
print(maiorabsoluto(numeros))