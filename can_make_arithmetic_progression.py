# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence

class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:

        if len(arr) == 1 or len(arr) == 0:
            return True

        elif len(arr) >= 2:
            arr.sort()
            gap = arr[1]-arr[0]

            for i in range(0, len(arr)):
                if i < len(arr)-1 and not arr[i+1]-arr[i] == gap:
                    return False

            return True


solution = Solution()


print(solution.canMakeArithmeticProgression([3, 5, 1]))
print(solution.canMakeArithmeticProgression([1, 2, 4]))
