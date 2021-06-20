def factorial(n):
    value = n
    if(n != 1):
        return value * factorial(n-1)
    else:
        return value

print(factorial(5))

# global variable
glo_var = 0
def addToGloVar():
    global glo_var
    glo_var += 1

print(glo_var)
addToGloVar()
print(glo_var)

glo_list = [0, 1, 2]
def addToGloList():
    glo_list.append(3)

print(glo_list)
addToGloList()
print(glo_list)

# packing
def packFunc():
    a = 1
    b = 2
    c = 'three'
    return a, b, c

print(packFunc())
a,b,c = packFunc()
print(a,b,c)
c,d,e = packFunc()
print(c,d,e)

# lambda
# basic
print((lambda a: factorial(a))(5))

# func parameter
data = [('one', 1), ('two', 2), ('three', 3)]
def extractKey(t):
    return t[0]

print(sorted(data, key=extractKey))
print(sorted(data, key=lambda a: a[0]))

# multiple list 
l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]

sumList = map(lambda a,b: a+b, l1, l2)
print(list(sumList))


# map
l = [1,2,3,4,5]
ml = map(lambda a: a**2, l)
print(list(ml))

t = (1, 2, 3, 4, 5)
mt = map(lambda a : a**2, t)
print(list(mt))

d = {1: 'one', 2: 'two', 3: 'three'}
map(print, d)
map(lambda a: print(f'{a}: {d[a]}'), d)