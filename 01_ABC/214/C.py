

if __name__ == '__main__':
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    ans = T.copy()

    min_T = min(T)
    min_index = T.index(min_T)

    '''
    ・初めて宝石をもらうタイミングは以下２パターンのみ
    　・高橋君からもらう
    　・となりのすぬけ君からもらう
    ・つまり、となりのすぬけ君が、初めて宝石もらうタイミングが確定していれば、確定する
    ・最初に確定するすぬけ君は、高橋君から最初に宝石をもらうすぬけ君
    ・そのとなりは、高橋君からもらうか、すぬけ君からもらうかで確定する
    ・そのとなりも・・・
    '''
    for i in range(N):
        ans[(min_index + i + 1) % N] = min(ans[(min_index + i + 1) % N], ans[(min_index + i) % N] + S[(min_index + i) % N])

    for a in ans:
        print(a)
