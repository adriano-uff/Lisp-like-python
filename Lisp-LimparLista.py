def car(x):
	return x[0]

def cons(x,y):
	return [x] + y

def ehAtomo(vals):
	return not isinstance(vals, list)

def emagrecer(vals):
	if vals == []:
		return []
	else:
		if ehAtomo(car(vals)):
			return cons(car(vals), emagrecer(cdr(vals)))
		else:
			return concatena(emagrecer(car(vals)), emagrecer(cdr(vals)))

def concatena(valsA, valsB):
	if valsA == []:
		return valsB
	else:
		if valsB == []:
			return valsA
		else:
			return cons(car(valsA), concatena(cdr(valsA),valsB))

def cdr(x):
	return x[1:]



numeros = [[1,2],3,[[[4,5],6,7],8],9,[4,5,6,5]]
print(emagrecer(numeros))
