from collections import defaultdict


if __name__ == '__main__':
    S = input()
    N = len(S)
    rest = set()
    A = [0]
    for i in range(N):
        if S[i] in rest:
            rest.discard(S[i])
            A.append(A[i]-2**(int(S[i])))
        else:
            rest.add(S[i])
            A.append(A[i]+2**(int(S[i])))

    d = defaultdict(int)
    for a in A:
        d[a] += 1
    ans = 0

    for value in d.values():
        if value > 1:
            ans += value * (value-1) // 2

    print(ans)


