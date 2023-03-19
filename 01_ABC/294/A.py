

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    ans = []
    for a in A:
        if a % 2 == 0:
            ans.append(a)

    print(*ans)