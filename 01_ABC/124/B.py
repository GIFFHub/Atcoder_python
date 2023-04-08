

if __name__ == '__main__':
    N = int(input())
    H = list(map(int, input().split()))
    max_H = 0
    ans = 0
    for h in H:
        if h >= max_H:
            ans += 1
            max_H = h
    print(ans)



