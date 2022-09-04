import numpy as np
import math

def caluculate_rad(vec_1, vec_2):

    # コサインの計算
    length_vec_1 = np.linalg.norm(vec_1)
    length_vec_2 = np.linalg.norm(vec_2)
    inner_product = np.inner(vec_1, vec_2)
    cos = inner_product / (length_vec_1 * length_vec_2)

    # 角度（ラジアン）の計算
    rad = np.arccos(cos)
    degree = np.rad2deg(rad)
    return rad


if __name__ == '__main__':

    A = np.array(list(map(int, input().split())), dtype=object)
    B = np.array(list(map(int, input().split())), dtype=object)
    C = np.array(list(map(int, input().split())), dtype=object)
    D = np.array(list(map(int, input().split())), dtype=object)

    vec_ab = B - A
    vec_ad = D - A

    vec_ba = A - B
    vec_bc = C - B

    vec_cb = B - C
    vec_cd = D - C

    vec_da = A - D
    vec_dc = C - D

    BAD = caluculate_rad(vec_ab, vec_ad)
    ABC = caluculate_rad(vec_ba, vec_bc)
    BCD = caluculate_rad(vec_cb, vec_cd)
    ADC = caluculate_rad(vec_da, vec_dc)

    if BAD + ABC + BCD + ADC < 2*math.pi:
        print('No')
    else:
        print('Yes')
