from itertools import product

if __name__ == '__main__':
    K = int(input())

    T = []
    for pro in product((0, 1), repeat=10):
        tmp = ''
        for i in range(10):
            if pro[i]:
                tmp += str(9-i)
        if tmp != '':
            T.append(int(tmp))

    T.sort()
    print(T[K])



