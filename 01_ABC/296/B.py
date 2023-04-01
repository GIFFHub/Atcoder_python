

if __name__ == '__main__':
    S = []
    x = 'abcdefgh'
    y = '87654321'

    for _ in range(8):
        S.append(input())

    for i in range(8):
        if S[i] != '........':
            for j, s in enumerate(S[i]):
                if s == '*':
                    print(x[j]+y[i])
                    exit()
                    break
            break


