

if __name__ == '__main__':
    S = input()
    K = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, s in enumerate(S):
        if s in K:
            print(i+1)
            break