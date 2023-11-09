import itertools
if __name__ == '__main__':
    N = int(input())
    R = input()
    C = input()

    def head(s):
        for c in s:
            if c != ".":
                return c

    for a, b, c in itertools.product(itertools.permutations(range(N)), repeat=3)
        print(a, b, c)


