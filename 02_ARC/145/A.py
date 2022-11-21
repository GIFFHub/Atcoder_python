def check(s:str) -> bool:
    if s[0] == 'B':
        return True
    elif s[-1] == 'B':
        return False
    else:
        inner_s = s[1:len(s)]
        return check(inner_s)


if __name__ == '__main__':
    N = int(input())
    S = input()

    if N == 1:
        print('Yes')
    elif N == 2:
        if S[0] == S[1]:
            print('Yes')
        else:
            print('No')
    elif check(S):
        print('Yes')
    else:
        print('No')




    '''
    考察
    ・N>=3で考える
    ・ABにしても回文にできない条件があるはず
    ・例えばN=3の場合
     OK: AAA, BBB, BBA, BAA, ABA, BAB
     NG: AAB, ABB
     　→Aで始まってBで終わる場合、絶対OUT
    ・そもそも、頭がBなら、二文字目以降全て入れ替えて回文になる
    ・問題は頭がAかつ、Aで終わる時
    '''