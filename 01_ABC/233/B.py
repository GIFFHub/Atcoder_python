

if __name__ == '__main__':
    L, R = map(int, input().split())
    S = input()

    S_list = list(S)
    ans = S_list[:L-1] + list(reversed(S_list[L-1:R])) + S_list[R:]

    for s in ans:
        print(s, end='')



