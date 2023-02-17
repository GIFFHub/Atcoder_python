

if __name__ == '__main__':
    A, B = map(float, input().split())
    B *= 100
    ans = A*B
    ans = str(ans)
    index = ans.find('.')
    ans = int(ans[:index-2])
    print(ans)
