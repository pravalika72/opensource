x,y,z=map(int,input().split())
a=x*y
b=a/(24*60)
if(b<=z):
    print('YES')
else:
    print('NO')
