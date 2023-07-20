import math

def eats_bananas(piles, h):

    l, r = 1, max(piles)
    res = max(piles)

    while l <= r:
        k = (l + r) // 2
        total_time = 0

        for p in piles:
            #round up
            total_time += math.ceil(p/k)
        
        if total_time <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1
    return res
