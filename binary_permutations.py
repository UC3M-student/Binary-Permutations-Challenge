from itertools import permutations

def listallbinarypermutations(n):
    n = n - 1
    x = 2**n
    w = bin(x)
    w = w[3:]
    lst = []
    lst2 = []
    lst3 = []
    for i in range(1,n+2,1):
        a = permutations(w)
        lst.append(tuple(a))
        w = w.replace("0","1",1)

    for y in lst:
        for z in y:
            lst2.append(z)
    lst2 = list(set(lst2))

    lst2 = [("1",) + i for i in lst2]
    
    for i in lst2:
        lst3.append(int("".join(i)))
    
    lst3.sort()
    
    return print(lst3)

listallbinarypermutations(4)
