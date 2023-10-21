

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    t = A[0]
    for a in A:
        if a == t:
            continue
        else:
            break
    else:
        print('Yes')
        exit()

    print('No')