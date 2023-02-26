

if __name__ == '__main__':
    N = int(input())
    S = input()
    dx = 0
    dy = 0
    d = dict()
    d[0] = set()
    d[0].add(0)
    for s in S:
        if s == 'R':
            dx += 1
        elif s == 'L':
            dx -= 1
        elif s == 'U':
            dy += 1
        else:
            dy -= 1

        if dx in d:
            if dy in d[dx]:
                print('Yes')
                break
            else:
                d[dx].add(dy)
        else:
            if dx in d:
                d[dx].add(dy)
            else:
                d[dx] = set()
                d[dx].add(dy)
    else:
        print('No')

