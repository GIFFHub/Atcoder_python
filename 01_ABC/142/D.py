
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


if __name__ == '__main__':
    A, B = map(int, input().split())

    A_div = make_divisors(A)
    B_div = make_divisors(B)
    B_div_set = set(B_div)
    S = set()
    for a in A_div:
        if a in B_div_set:
            S.add(a)
    S = list(S)
    S.sort()
    ans = []
    S = S[1:]
    for s in S:
        for a in ans:
            if s % a == 0:
                break
        else:
            ans.append(s)

    print(len(ans)+1)


