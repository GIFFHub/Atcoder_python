

if __name__ == '__main__':

    '''
    A = [a1, a2, a3,,,,]とした時
    A[i] % K (B[i]とする) は以下で表せる
    
    ・i=1の時
    　　7 % K
    ・i>=2の時
    　　(B[i-1]*10 + 7) % K
    
    B[i]が繰り返されると、無限ループに入る
    0 <= B[i] <= K-1であり、K回繰り返せば、必ず複数回同じ値のものがでてくる（鳩の巣原理）
    よってO(K)でよい
    '''
    K = int(input())
    num = 0
    for i in range(K+1):
        num = (10 * num + 7) % K
        if num == 0:
            ans = i+1
            break
    else:
        ans = -1
    print(ans)

