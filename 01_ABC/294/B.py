

if __name__ == '__main__':
    H, W = map(int, input().split())
    ans = []
    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for _ in range(H):
        A = list(map(int, input().split()))
        tmp = []
        for a in A:
            if a == 0:
                tmp.append('.')
            else:
                tmp.append(alf[a-1])
        ans.append(tmp)


    for i in range(H):
        print(''.join(ans[i]))




