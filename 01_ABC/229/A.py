

if __name__ == '__main__':
    # input
    S1 = input()
    S2 = input()

    if S1.count('#') + S2.count('#') == 2:
        if S1[0] == S2[1]:
            print('No')
        else:
            print('Yes')
    else:
        print('Yes')
