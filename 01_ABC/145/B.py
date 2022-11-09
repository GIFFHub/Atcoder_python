

if __name__ == '__main__':
    N = int(input())
    S = input()

    if N % 2 == 1:
        print('No')
    else:
        half = N//2
        if S[:half] == S[half:]:
            print('Yes')
        else:
            print('No')

