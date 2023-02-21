

if __name__ == '__main__':
    K = int(input())
    A, B = map(int, input().split())
    for x in range(A, B+1):
        if x % K == 0:
            print('OK')
            break
    else:
        print('NG')