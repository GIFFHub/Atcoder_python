
'''

コーナーケースを考える
1✖️n : n
n✖️1 : n


'''



if __name__ == '__main__':

    H, W = map(int, input().split())

    if H == 1:
        print(W)
    elif W == 1:
        print(H)
    else:
        H2 = -(-H//2)
        W2 = -(-W//2)
        print(H2 * W2)
