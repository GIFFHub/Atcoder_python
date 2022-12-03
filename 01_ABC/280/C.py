

if __name__ == '__main__':
    S = input()
    T = input()


    ans = len(T)

    for i in range(len(S)):
        if S[i] != T[i]:
            ans = i+1
            break

    print(ans)

