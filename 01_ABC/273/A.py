def func(k):
    if k>0:
        return k*func(k-1)
    else:
        return 1

N = int(input())

print(func(N))