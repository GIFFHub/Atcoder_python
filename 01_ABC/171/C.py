import string

if __name__ == '__main__':
    N = int(input())
    alf = string.ascii_lowercase
    T = []
    while True:
        mod = N % 26
        T.append(mod)
        N //= 26
        if N < 26:
            T.append(N)
            break

    for i in range(len(T)-1):
        if T[i] <= 0:
            T[i+1] -= 1
    if T[-1] == 0:
        T.pop(-1)
    T.reverse()
    ans = []
    for t in T:
        ans.append(alf[t-1])
    print(''.join(ans))










