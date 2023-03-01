

if __name__ == '__main__':
    A, B = map(int, input().split())
    ans = -1
    for i in range(100000):
        if i * 8 // 100 == A and i // 10 == B:
            ans = i
            break

    print(ans)
