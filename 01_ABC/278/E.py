from collections import defaultdict


def count_by(dic, term):
    count = 0
    for v in dic.values():
        if v == term:
            count += 1
    return count


if __name__ == '__main__':
    H, W, N, h, w = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))

    d = defaultdict(int)
    s = set()
    for aa in A:
        for a in aa:
            d[a] += 1
            s.add(a)
    len_s = len(s)

    for k in range(0, H-h+1):
        for l in range(0, W-w+1):
            tmp_d = d.copy()
            for i in range(k, k+h):
                for j in range(l, l+w):
                    tmp_d[A[i][j]] -= 1
            if l == 0:
                print('%d' % (len_s-count_by(tmp_d, 0)), end='')
            else:
                print(' %d' % (len_s - count_by(tmp_d, 0)), end='')
        print()




