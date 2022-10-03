

if __name__ == '__main__':

    X, A, D, N = map(int, input().split())
    ans = 0
    if D > 0:
        S_max = A+(N-1)*D
        S_min = A
    else:
        S_max = A
        S_min = A+(N-1)*D

    if X >= S_max:
        ans = abs(X-S_max)

    elif X <= S_min:
        ans = abs(S_min - X)

    else:
        ans = min(abs((X-A) % D), D- (abs(X-A) % D))

    print(ans)
