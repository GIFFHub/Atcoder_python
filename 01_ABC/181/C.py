

if __name__ == '__main__':
    N = int(input())
    P = []
    for _ in range(N):
        x, y = map(int, input().split())
        P.append((x, y))
    P.sort()
    ans = 'No'
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if (P[k][0]-P[j][0]) * (P[j][1]-P[i][1]) == (P[j][0]-P[i][0]) * (P[k][1]-P[j][1]):
                    ans = 'Yes'
                    break
            else:
                continue
            break
        else:
            continue
        break
    print(ans)


