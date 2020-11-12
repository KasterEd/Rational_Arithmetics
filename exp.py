def exp(x) :
    sum = x
    term = x
    n = 1
    while term != 0:
        term = term *x/n
        sum = sum+ term
        n +=1
    return sum 

print(exp(1))
print(exp(0.05))
print(exp(-5.5))
