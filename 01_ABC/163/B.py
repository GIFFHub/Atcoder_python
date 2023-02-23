

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    all_task = sum(A)
    ans = -1
    if all_task <= N:
        ans = N - all_task

    print(ans)
