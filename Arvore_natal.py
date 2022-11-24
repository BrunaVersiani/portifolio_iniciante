def arvore_natal(n):
    a = 2 * n-2
    for i in range(0, n):
        for j in range(0, a):
            print(end=" ")
        a = a-1
        for j in range(0, i+1):
            print("\033[32m*", end=" ")
        print("\r")
print(arvore_natal(10))
