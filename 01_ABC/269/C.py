from itertools import product


if __name__ == '__main__':
    N = str(format(int(input()), 'b'))

    # とりあえず、何桁目が1なのかをlist化

    table = [] # 何桁目が1か
    len_N = len(N)
    for i in range(len_N):
        if N[i] == '1':
            table.append(len_N-i-1)

    #table = list(reversed(table))

    #print(table)
    len_table = len(table)
    for pro in product((0, 1), repeat=len_table):
        #print(pro)
        ans = 0
        for i in range(len_table):
            if pro[i]:
                ans += 2**table[i]
        print(ans)









