
if __name__ == '__main__':
    N = int(input())
    S = []
    S_set = set()
    judge1 = {'H', 'D', 'C', 'S'}
    judge2 = {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'}
    flg = 1
    for _ in range(N):
        s = input()
        s1 = s[0]
        s2 = s[1]

        if s1 not in judge1:
            flg = 0

        elif s2 not in judge2:
            flg = 0

        elif s in S_set:
            flg = 0
        S_set.add(s)

    if flg:
        print('Yes')
    else:
        print('No')
