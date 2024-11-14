n,x,y=map(int,input().split())
r=x*n
if(y%x==0 and r>y):
    print('YES')
else:
    print('NO')
