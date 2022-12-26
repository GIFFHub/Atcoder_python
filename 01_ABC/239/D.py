import math


def check(k):
    cnt = 2
    while True:
        if cnt > math.sqrt(k):
            break
        if k % cnt > 0:
            cnt += 1
        else:
            return False
    return True


if __name__ == '__main__':
    A, B, C, D = map(int, input().split())
    '''
    和を素数にできたら青木くんの勝ち
    できなければ高橋くんの価値
    
    ・和を素数にできるとは？
    
    
    '''

    for i in range(A, B+1):
        for j in range(C, D+1):
            if check(i+j):
                break
        else:
            print('Takahashi')
            exit()
    print('Aoki')
