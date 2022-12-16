

if __name__ == '__main__':
    N = int(input())
    S = input()

    bad_turn = 0
    loser = 'Takahashi'
    for i, s in enumerate(S):
        if s == '1':
            bad_turn = i
            break

    if bad_turn % 2 == 1:
        loser = 'Aoki'

    print(loser)




