

if __name__ == '__main__':
    N = int(input())

    if N == 0:
        print('Yes')
    else:
        while True:
            if N % 10 == 0:
                N //= 10
            else:
                break

        N = str(N)
        for i in range(len(N)//2):
            if N[i] == N[-i-1]:
                continue
            else:
                print('No')
                break
        else:
            print('Yes')



