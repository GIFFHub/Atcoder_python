
def binary_search(ok, ng):
    if ng - ok == 1:
        return ok
    cen = (ok+ng)//2

    tmp = A*cen + B*(len(str(cen)))
    if X >= tmp:
        return binary_search(cen, ng)
    else:
        return binary_search(ok, cen)


if __name__ == '__main__':
    A, B, X = map(int, input().split())

    print(min(10**9, binary_search(0, 10**18+1)))









