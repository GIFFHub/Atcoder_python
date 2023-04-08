

if __name__ == '__main__':
    S = input()
    N = len(S)
    flg = 0
    ans = 0
    for s in S:
        if flg == int(s):
            ans += 1
        flg = 1 - flg

    print(min(ans, len(S)-ans))

