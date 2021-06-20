# 정수형으로 변환
n = int(input())
print(n)

# split
data = input().split()
print(data)

# split then int()
int_data = map(int, input().split())
print(int_data)

# num of el defined (unpacking)
a, b, c = input().split()
print(f'a : {a}, b : {b}, c : {c}')

import sys;
# efficient
print('large input : ')
largeInput = sys.stdin.readline().rstrip()
print(largeInput.split())
