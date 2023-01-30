# https://blog.satoooh.com/entry/5195/#:~:text=%E7%B5%90%E8%AB%96%E3%81%8B%E3%82%89%E8%A8%80%E3%81%86%E3%81%A8%E3%80%81%20n,(n%E2%88%92r)!)

from scipy.special import comb
from math import factorial

if __name__ == '__main__':
    L = int(input())
    n = L-1
    r = 11
    ans1 = comb(n, r)
    ans2 = factorial(n) // factorial(r) // factorial(n - r)
    print(ans2)


