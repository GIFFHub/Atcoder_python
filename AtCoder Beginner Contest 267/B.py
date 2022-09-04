
if __name__ == '__main__':
    S = input()
    l = []
    if S[0] == '1':
        print('No')
    else:
        # 1列目
        l.append(int(S[6]))
        # 2列目
        l.append(int(S[3]))
        # 3列目
        if S[1] == '1' or S[7] == '1':
            l.append(1)
        else:
            l.append(0)
        # 4列目
        l.append(int(S[4]))
        # 5列目
        if S[2] == '1' or S[8] == '1':
            l.append(1)
        else:
            l.append(0)
        # 6列目
        l.append(int(S[5]))
        # 7列目
        l.append(int(S[9]))

        # lの中で、両サイドに1がある0があるか否か
        for i in range(len(l)):
            if l[i] == 0:
                if 1 in l[:i] and 1 in l[i:]:
                    print('Yes')
                    break
        else:
            print('No')
