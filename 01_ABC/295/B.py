

if __name__ == '__main__':
    R, C = map(int, input().split())
    table = []
    for _ in range(R):
        B = input()
        tmp = []
        for b in B:
            tmp.append(b)
        table.append(tmp)

    for i in range(R):
        for j in range(C):
            if table[i][j] == '#':
                for l in range(R):
                    for k in range(C):
                        if table[l][k] != '.' and table[l][k] != '#':
                            if (abs(l-i) + abs(k-j)) <= int(table[l][k]):
                                table[i][j] = '.'
    for i in range(R):
        for j in range(C):
            if table[i][j] != '#':
                table[i][j] = '.'

    for t in table:
        print(''.join(t))
