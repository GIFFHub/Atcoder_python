import math

if __name__ == '__main__':
    N = int(input())
    T = math.pow(10, 9)+7
    K = [0]*N

    all_pattern = 1
    non_pattern = 1
    for i in range(1, N):
        all_pattern *= 9
        non_pattern *= 8
        all_pattern %= T
        non_pattern %= T
        K[i] = K[i-1]*10 + (all_pattern - non_pattern)*2
        K[i] %= T
    ans = K[N-1]%T
    print(int(ans))