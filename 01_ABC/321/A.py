

if __name__ == '__main__':
    N = input()
    L = len(N)
    for i in range(L):
        if i == 0:
            pass
        else:
            if N[i-1] <= N[i]:
                print('No')
                break
    else:
        print('Yes')