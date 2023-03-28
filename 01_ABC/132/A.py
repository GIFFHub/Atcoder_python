from collections import defaultdict

if __name__ == '__main__':
    S = input()
    d = defaultdict(int)
    for s in S:
        d[s] += 1

    for value in d.values():
        if value != 2:
            print('No')
            break
    else:
        print('Yes')