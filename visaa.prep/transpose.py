n=int(input())
m=[]
for i in range(n):
    n1=list(map(int,input().split()))
    while(len(n1)!=n):
        n1=list(map(int,input().split()))
    m.append(n1)
t=[[n1[i] for n1 in m] for i in range(n)]
for n1 in t:
    print(' '.join(map(str,n1)))
