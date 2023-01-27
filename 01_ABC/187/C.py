

if __name__ == '__main__':
    N = int(input())
    r1 = set()
    r2 = set()
    for _ in range(N):
        s = input()

        if s[0] == '!':
            if s[1:] in r2:
                print(s[1:])
                break
            else:
                r1.add(s[1:])
        else:
            if s in r1:
                print(s)
                break
            else:
                r2.add(s)
    else:
        print('satisfiable')





