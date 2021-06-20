a = set([1,1,2,2,3,3,4])
print(a)

a.add(6)
print(a)

# not work
# a.add([7,8])
# print(a)

a.update([9, 0])
print(a)