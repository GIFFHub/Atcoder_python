

if __name__ == '__main__':
    A, B, K = map(int, input().split())
    '''
    0と1で考える
    A個の0とB個の1
    '''
    ans = '0'*A+'1'*B

    print(ans)