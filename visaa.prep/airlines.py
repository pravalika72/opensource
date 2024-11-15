def c(x,n):
    t=x*100
    if t>=n:
        return 0
    r=n-t
    a=(r+99)//100
    return a
x,n=map(int,input().split())
print(c(x,n))
