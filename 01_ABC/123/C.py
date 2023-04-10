

if __name__ == '__main__':
    N = int(input())

    T = []
    for i in range(5):
        T.append(int(input()))

    min_T = min(T)

    time = N // min_T
    if N % min_T != 0:
        time += 1
    time += 4

    print(time)



