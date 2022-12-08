import string

if __name__ == '__main__':
    P = list(map(int, input().split()))
    alf = string.ascii_lowercase
    ans = []
    for p in P:
        ans.append(alf[p-1])

    print(''.join(ans))
