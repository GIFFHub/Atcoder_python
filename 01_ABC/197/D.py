import math
import numpy as np
def get_rotation_matrix(rad):
    """
    指定したradの回転行列を返す
    """
    rot = np.array([[np.cos(rad), -np.sin(rad)],
                    [np.sin(rad), np.cos(rad)]])
    return rot


if __name__ == '__main__':
    N = int(input())
    x_up, y_up = map(int, input().split())
    x_down, y_down = map(int, input().split())

    #r = (y_up - y_down) / 2

    #l = math.sqrt(2*(r**2)*(1-math.cos(math.radians(360/N))))

    x_center = (x_up+x_down) / 2
    y_center = (y_up+y_down) / 2

    xp = x_up - x_center
    yp = y_up - y_center
    base_point = np.array([xp, yp])

    rad = math.radians(360/N)
    rot = get_rotation_matrix(rad)

    rotated_point = np.dot(rot, base_point)

    x1 = rotated_point[0]+x_center
    y1 = rotated_point[1]+y_center

    print(x1, y1)











