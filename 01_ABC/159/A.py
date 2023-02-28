

if __name__ == '__main__':
    N, M = map(int, input().split())

    '''
    偶数＝偶数＋偶数 or 奇数+奇数
    
    '''
    ans = N*(N-1)//2 + M*(M-1)//2
    print(ans)