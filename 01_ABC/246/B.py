import math

A, B = map(int, input().split())

d = math.sqrt(A**2 + B**2)

x = A/d
y = B/d

print(x, y)
