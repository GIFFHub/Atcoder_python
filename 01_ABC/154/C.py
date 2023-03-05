

if __name__ == '__main__':
    N = int(input())
    A = set(map(int, input().split()))
    if N == len(A):
        print('YES')
    else:
        print('NO')