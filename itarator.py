def geometric(a0,an,c):
    while a0 < an  :
        yield a0
        a0 = c*a0

def divisors(n):
    for i in range(1,n):
        if n%i == 0:
            yield n//i
            a=n//i*n//i
            while n%a==0:
                yield n//i
                a= a*n//i

def filter(sel, other):
    for i in other:
        if sel(i):
            yield i

def permutations(n):
    if n == 0 : 
        yield []
    else :
        for i in permutations( n - 1 ) : 
            for a in [1,0,1] :
                i. append(a) 
                yield i
                i. pop()