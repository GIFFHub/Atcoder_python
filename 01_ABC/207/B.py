

if __name__ == '__main__':
    A, B, C, D = map(int, input().split())

    if C*D-B <= 0:
        print(-1)
    else:
        x = A // ((C*D)-B)
        if x == A/((C*D)-B):
            print(x)
        else:
            print(x+1)




