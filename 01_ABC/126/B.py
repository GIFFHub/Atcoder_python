

if __name__ == '__main__':
    S = input()
    if S[0] == '0':
        front = S[1:2]
    else:
        front = S[:2]
    if S[2] == '0':
        end = S[3]
    else:
        end = S[2:]

    front = int(front)
    end = int(end)

    if 1 <= front <= 12:
        if 1 <= end <= 12:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    else:
        if 1 <= end <= 12:
            print('YYMM')
        else:
            print('NA')

