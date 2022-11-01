def func(x):
    return x**2+x*2+3


if __name__ == '__main__':
    t = int(input())
    ans = func(func(func(t)+t) +func(func(t)))
    print(ans)
