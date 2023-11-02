# https://leetcode.com/problems/power-of-four/

import math


class Solution(object):
    def isPowerOfFour(self, n) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        if n < 0 or n == 0:
            return False

        for i in range(0, 16):

            power = 4**i

            if power == n:
                return True

            if power > n:
                return False


solution = Solution()


for input_value in [16, 5, 1]:
    print(solution.isPowerOfFour(input_value))
