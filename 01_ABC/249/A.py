A, B, C, D, E, F, X = map(int, input().split())

# 何秒止まっているかが大事

# A秒進んでC秒休むを繰り返した回数 cnt
cnt_t = X // (A+C)
cnt_a = X // (D+F)

# 上記回数後進んだ秒数
move_t = X % (A+C)
move_a = X % (D+F)

# 二人が進んだ距離
takahashi = B*A*cnt_t + B*min(A, move_t)
aoki = E*D*cnt_a + E*min(D, move_a)




if takahashi > aoki:
    print('Takahashi')
elif takahashi < aoki:
    print('Aoki')
else:
    print('Draw')
