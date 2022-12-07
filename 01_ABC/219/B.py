

if __name__ == '__main__':
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    ans = []
    for t in T:
        if t == '1':
            ans.append(S1)
        elif t == '2':
            ans.append(S2)
        elif t == '3':
            ans.append(S3)

    print(''.join(ans))