

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    d = dict()
    for i in range(1, 2*(10**5)+1):
        d[i] = i

    cnt = 0
    for j in range(N//2+1):
        left = A[j]
        right = A[-(j+1)]
        lefts = []
        rights = []
        while True:
            if d[left] == left:
                for l in lefts:
                    d[l] = left
                break
            else:
                lefts.append(left)
                left = d[left]

        while True:
            if d[right] == right:
                for r in rights:
                    d[r] = right
                break
            else:
                right = d[right]
                rights.append(right)

        if left != right:
            d[left] = right
            cnt += 1

    print(cnt)


