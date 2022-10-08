

if __name__ == '__main__':
    N = int(input())
    reels = []
    push = [0] * 10
    ans = 10**6
    for _ in range(N):
        reels.append(input())

    for num in range(10):
        for reel in reels:
            t = reel.find(str(num))
            push[t] += 1
        max_push = max(push)
        push.reverse()
        index = push.index(max_push)
        ans = min(ans, (max_push-1)*10+(9-index))
        push = [0]*10

    print(ans)

