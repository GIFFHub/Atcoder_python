

if __name__ == '__main__':
    N, X, Y = map(int, input().split())

    '''
    ・距離が1である組み合わせは確定でN
    ・距離が2以上になってくると、ショットカットできる位置(X,Y)によって変わってくる
    
    '''
    ans = [0]*(N-1)
    for i in range(N-1):
        ans[i] = N-i
    print(ans)

    for k in range(N-1):

