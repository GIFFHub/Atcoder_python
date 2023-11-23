

if __name__ == '__main__':
    S = input()
    T = {'a', 'e', 'i', 'o', 'u'}
    ans = ''
    for s in S:
        if s not in T:
            ans += s

    print(ans)
