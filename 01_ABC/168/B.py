

if __name__ == '__main__':
    K = int(input())
    S = input()
    if len(S) <= K:
        ans = S
    else:
        ans = S[:K] + '...'
    print(ans)

