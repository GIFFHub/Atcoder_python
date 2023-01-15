import string

if __name__ == '__main__':
    S = input()
    S_list = list(S)
    d = dict()
    tmp = 1
    for i in string.ascii_uppercase:
        d[i] = tmp
        tmp += 1

    ans = 0
    len_S = len(S)
    for i, s in enumerate(S_list):
        ans += d[s]*((tmp-1)**(len_S-i-1))

    print(ans)


