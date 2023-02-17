import math
import numpy as np


def rotation_o(u, t, deg=False):
    # 度数単位の角度をラジアンに変換
    if deg:
        t = np.deg2rad(t)

    # 回転行列
    R = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t),  np.cos(t)]])

    return np.dot(R, u)


if __name__ == '__main__':
    A, B, H, M = map(int, input().split())

    # 時針の移動角度
    # 12*60分で一周する
    # H時間M分はH*60+M分
    a = (360 * (H*60+M) / (12*60)) % 360
    b = (360 * (H*60+M) / 60) % 360

    A = (0, A)
    B = (0, B)
    A_pos = rotation_o(A, a, deg=True)
    B_pos = rotation_o(B, b, deg=True)

    ans = math.sqrt((A_pos[0]-B_pos[0])**2 + (A_pos[1]-B_pos[1])**2)

    print(ans)






