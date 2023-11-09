import math

if __name__ == '__main__':
    B = int(input())

    A = 1
    while True:
        C = A**A
        C2 = pow(A, A)
        print('C:', C)
        print('C2', C2)
        if C == B:
            print(A)
            break
        elif C > B:
            print(-1)
            break
        else:
            A += 1

