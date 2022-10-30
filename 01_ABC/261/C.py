from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    S = []
    S_set = set()
    S_dict = defaultdict(int)
    for _ in range(N):
        s = input()
        if s in S_set:
            print('%s(%d)' % (s, S_dict[s]))
        else:
            print(s)
            S_set.add(s)
        S_dict[s] += 1





