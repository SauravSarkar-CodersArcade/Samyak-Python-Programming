# is and is not : Identity Operator
# id() is a function not sn operator
# id gives the address
# is operator compares the address
a = 10
b = 20
print(id(a), id(b))
if a is not b:
    print('Diff identity')
else:
    print('Same identity')
c = 10
d = 10
print(id(c), id(d))
if c is d:
    print('Same identity')
else:
    print('Diff identity')