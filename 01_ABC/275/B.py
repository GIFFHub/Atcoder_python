
if __name__ == '__main__':
    A, B, C, D, E, F = map(int, input().split())
    T = 998244353
    A %= T
    B %= T
    C %= T
    D %= T
    E %= T
    F %= T

    a = (A*B*C) % T
    b = (D*E*F) % T

    print((a-b)%T)