

if __name__ == '__main__':
    S = input()
    T = ['Sunny', 'Cloudy', 'Rainy']
    if S == T[0]:
        ans = T[1]
    elif S == T[1]:
        ans = T[2]
    else:
        ans = T[0]

    print(ans)
