

if __name__ == '__main__':
    S = input()
    T = []
    for s in S:
        T.append(s)
    for i in range(len(T)//2):
        T[2*i], T[2*i+1] = T[2*i+1], T[2*i]

    print(''.join(T))