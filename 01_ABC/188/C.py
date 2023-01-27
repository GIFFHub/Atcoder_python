

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = A.copy()

    while True:
        if len(B) == 2:
            target = min(B)
            break
        tmp = []
        for i in range(len(B)//2):
            tmp.append(max(B[2*i], B[2*i+1]))
        B = tmp.copy()

    ans = A.index(target) + 1
    print(ans)







