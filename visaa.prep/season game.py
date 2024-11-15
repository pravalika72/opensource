def f(m):
    if m<1 or m>12:
        return 'Invalid'
    elif m in[3,4,5]:
        return 'Spring'
    elif m in [6,7,8]:
        return 'Summer'
    elif m in [9,10,11]:
        return 'Autumn'
    else:
        return 'Winter'
m=int(input())
print(f(m))
