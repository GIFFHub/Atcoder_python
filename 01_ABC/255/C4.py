def binary_search(ng, ok):
    if ok-ng == 1:
        return ok

    target = (ng+ok)//2
    tmp = A+D*target
    if D > 0:
        if X <= tmp:
            return binary_search(ng, target)
        else:
            return binary_search(target, ok)
    else:
        if X >= tmp:
            return binary_search(ng, target)
        else:
            return binary_search(target, ok)


if __name__ == '__main__':
    X, A, D, N = map(int, input().split())

    if D > 0:
        Max = A+D*(N-1)
        Min = A
    else:
        Max = A
        Min = A+D*(N-1)

    if X > Max:
        ans = X-Max
    elif X < Min:
        ans = Min-X
    else:
        K = binary_search(-1, N+1)
        ans1 = A+D*K
        ans2 = A+D*(K-1)
        ans = min(abs(ans1-X), abs(ans2-X))
        ans = max(0, ans)

    print(ans)



