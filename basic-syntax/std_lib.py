# internal
print('internal')
print(sum([1,2,3]))
print(min(1,2,3))
print(max(1,2,3))
print(max([1,2,3]))
print(eval('(1+2)*3'))
print((1+2)*3)
lastNames = {'김': 'kim', "이": 'lee', '박': 'park'}
print(sorted(lastNames))
print(sorted(lastNames, key=lambda a: lastNames[a], reverse=True))

# itertools (순열, 조합)
print('itertools')
from itertools import permutations, combinations, combinations_with_replacement, product
data = ['a', 'b', 'c', 'c']
print(list(permutations(data, 2)))  # nP2(순열)
print(list(product(data, repeat=2)))    # 중복 허용
print(list(combinations(data, 2)))   # nC2(조합)
print(list(combinations_with_replacement(data, 2)))  # 중복 허용

# collections
print('collections')
from collections import Counter
c = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print(c['a'])
print(dict(c))


# math
print('math')
import math
def lcm(a, b):
    return a*b // math.gcd(a, b)

a = 21
b = 14
print(math.gcd(a, b))
print(lcm(a, b))


# heapq : 힙 자료구조

# bisect : 이진 탐색



