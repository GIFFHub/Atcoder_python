

if __name__ == '__main__':
    S = input()
    t = set()
    for s in S:
        t.add(s)
    len_t = len(t)
    if len_t == 1:
        print(1)
    elif len_t == 2:
        print(3)
    else:
        print(6)

