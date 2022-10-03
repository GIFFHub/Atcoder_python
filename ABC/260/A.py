

if __name__ == '__main__':
    S = input()

    if S[0] == S[1]:
        if S[0] != S[2]:
            print(S[2])
        else:
            print(-1)
    elif S[0] == S[2]:
        print(S[1])
    else:
        print(S[0])