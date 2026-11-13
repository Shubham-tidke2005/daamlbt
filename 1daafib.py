def fib(n):
    a=0
    b=1
    for i in range(0,n+1):
        if(i <= 1):
            print(i,end=" ")
        else:
            print(a+b,end=" ")
            res=a+b
            a=b
            b=res
            
def fib_rec(n):
    if(n<=1):
        return n
    else:
        return fib_rec(n-1)+fib_rec(n-2)


print(fib_rec(8))
print(fib(8))