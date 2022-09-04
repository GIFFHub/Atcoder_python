def main():
    # N, *S = open(0).read().split()
    N = int(input())
    S =  []
    for i in range(N):
        S.append(input())

    # N = int(N)
    st = set() # 重複なし集合
    ans = []
    for i, s in enumerate(S, 1):
        if s not in st:
            st.add(s) # setの場合はadd!
            ans.append(i)
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()