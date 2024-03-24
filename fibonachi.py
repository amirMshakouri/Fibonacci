def fibo(num):
    aval=[1,1]
    n1 = 1
    n2 = 1
    for i in range(2,num):
        n3 =n1+n2
        aval.append(n3)
        n1 = n2
        n2 = n3
    return aval
print(fibo(5))
