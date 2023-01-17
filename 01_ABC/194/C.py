from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for a in A:
        d[a] += 1

    B = list(set(A))
    len_B = len(B)
    ans = 0

    for i in range(len_B-1):
        for j in range(i+1, len_B):
            ans += (B[j] - B[i])**2 * d[B[j]]*d[B[i]]

    print(ans)

