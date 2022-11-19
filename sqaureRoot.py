def squareroot(a,b):
    if b == 0:
        return 1
    else:
        return a*squareroot(a,b-1)
print(squareroot(9,3)) 