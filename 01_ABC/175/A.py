

if __name__ == '__main__':
    S = input()

    R = S.count('R')

    if R == 2:
        if S == 'RSR':
            R = 1

    print(R)