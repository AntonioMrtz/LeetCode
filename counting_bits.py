# https://leetcode.com/problems/counting-bits/

# 0,1,2,4 ,8 -> 1
# 3,5,6 ,9,12 ->2
# 7 ,10,11,14 -> 3
# 15 -> 4

import math


def countBits(n: int) -> list:

    res = []

    for i in range(0, n+1):
        res.append(0)
        res[i] = res[(i // 2)] + (i % 2)

    return res


print(countBits(2))
print(countBits(5))
