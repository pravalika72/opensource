n=int(input())
arr=list(map(int,input().split()))
a=int(input())

for i in range(n):
    if(arr[i]==a):
        print(i)
        break
else:
    print('-1')
