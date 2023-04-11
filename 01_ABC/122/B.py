

if __name__ == '__main__':
    S = input()
    T = {'A', 'C', 'G', 'T'}

    ans = 0
    tmp = 0
    for s in S:
        if s in T:
            tmp += 1
        else:
            tmp = 0
        ans = max(ans, tmp)
    print(ans)
