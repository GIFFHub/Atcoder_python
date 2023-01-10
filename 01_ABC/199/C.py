

if __name__ == '__main__':
    N = int(input())
    S = input()
    S_list= list(S)
    Q = int(input())
    start = 0

    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 2:
            start = N-start
        else:
            a_index = (start+a-1) % (2*N)
            b_index = (start+b-1) % (2*N)
            S_list[a_index], S_list[b_index] = S_list[b_index], S_list[a_index]

    if start == N:
        S_list = S_list[N:]+S_list[:N]

    print(''.join(S_list))









