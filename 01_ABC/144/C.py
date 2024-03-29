
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


if __name__ == '__main__':
    N = int(input())
    T = make_divisors(N)
    index = len(T)//2
    goal = (T[index], T[-index-1])
    print(goal[0]+goal[1]-2)