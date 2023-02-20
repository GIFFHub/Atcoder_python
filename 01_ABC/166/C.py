

if __name__ == '__main__':
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    d = dict()
    for _ in range(M):
        a, b = map(int, input().split())
        if a not in d:
            d[a] = [b]
        else:
            d[a].append(b)
        if b not in d:
            d[b] = [a]
        else:
            d[b].append(a)

    check = [False]*N
    ans = 0
    for i in range(1,N+1):
        if not check[i-1]:
            if i not in d:
                check[i-1] = True
                ans += 1
            else:
                check[i-1] = True
                for path in d[i]:
                    if H[path-1] >= H[i-1]:
                        break
                    else:
                        check[path-1] = True
                else:
                    ans += 1

    print(ans)






