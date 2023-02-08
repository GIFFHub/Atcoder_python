

def gcd_t(list_g1):
    for a in reversed(range(1, min(list_g1)+1)):
        for b in list_g1:
            if b % a != 0:
                break
        else:
            return a