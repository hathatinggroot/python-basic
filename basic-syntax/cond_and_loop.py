# conditional
a = 10
if 0 < a < 11:
    print('cool')

b = int(input('input number : '))
if (b > 10):
    pass
elif (b < 10):
    print(f'input number is {b}')
else:
    print('input number is 10')


# loop
print('loop in list')
l = [1,2,3,4,5]
for i in l:
    print(i)

print('loop in tuple')
t = (1,2,3,4,5)
for i in t:
    print(i)

print('loop in dict')
d = {1: 'one', 2: 'two', 3: 'three'}
for i in d:
    print(f'{i} : {d[i]}')