

if __name__ == '__main__':
    S = input()
    s = [[] for _ in range((3*10**5)) ]
    s_all = set()
    cnt = 0

    for i in range(len(S)):
        if S[i] == '(':
            cnt += 1

        elif S[i] == ')':
            for k in s[cnt]:
                s_all.remove(k)
            s[cnt] = []
            cnt -= 1

        else:
            if S[i] in s_all:
                print('No')
                break
            else:
                s[cnt].append(S[i])
                s_all.add(S[i])
    else:
        print('Yes')




