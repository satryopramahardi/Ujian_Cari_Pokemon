def pangkat(a,b):
    h=a
    for i in range (1,b):
        h *= a
    return h

print(pangkat(2, 2))
print(pangkat(3, 3))
print(pangkat(10, 5))