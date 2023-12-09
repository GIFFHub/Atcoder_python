from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    S = input()

    d = defaultdict(int)

    all_pattern = N * (N-1) // 2 + N

    cnt = 1
    for i in range(1, N):
        if S[i-1] == S[i]:
            cnt += 1
        else:
            d[cnt] += 1
            cnt = 1
    d[cnt] += 1

    pattern = all_pattern
    for key, value in d.items():
        pattern -= value*(key*(key-1)//2+key)

    print(pattern)






