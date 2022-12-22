

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    if len(set(A)) == len(A):
        print('Yes')
    else:
        print('No')