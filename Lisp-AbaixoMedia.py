def car(x):
    return x[0]

def cdr(x):
    return x[1:]

def cons(x,y):
    return [x] + y

def soma(val):
    if val == []:
        return 0
    else:
        return car(val) + soma(cdr(val))

def quantidade(val):
    if val == []:
        return 0
    else:
        return 1 + quantidade(cdr(val))

def media(val):
    return soma(val) / quantidade(val)

def maioresMedia(val, media):
    if val == []:
        return []
    else:
        if car(val) < media:
            return cons(car(val),maioresMedia(cdr(val), media))

        else:
            return maioresMedia(cdr(val), media)

numeros = [2, 7, 5, 4, 1, 8, 9, 5 , 6, 3, 8, 9, 4, 2, 5, 7, 9, 5, 2, 5, 4, 5, 4]

print('media:',media(numeros))
print('menores que a media:', maioresMedia(numeros,media(numeros)))