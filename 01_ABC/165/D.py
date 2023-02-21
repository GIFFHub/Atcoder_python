

if __name__ == '__main__':
    A, B, N = map(int, input().split())


    if N < B:
        x = N
    else:
        x = B-1
    ans = (A*x)//B - A*(x//B)
    print(ans)
