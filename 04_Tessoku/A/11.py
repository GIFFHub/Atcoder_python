
def binary_search(ok, ng):
    if ng - ok == 1:
        return ok
    cen = (ok+ng)//2
    if X < A[cen]: # cen は ok 範囲に入るか
        return binary_search(ok, cen) # cenはngとして次に行く → cenはX含まない
    elif A[cen] <= X:
        return binary_search(cen, ng)


if __name__ == '__main__':
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(binary_search(-1, N)+1)



