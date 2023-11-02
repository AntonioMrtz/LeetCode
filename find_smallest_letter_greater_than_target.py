# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:

        ascii_code_target = ord(target)

        for letter in letters:
            if ord(letter) > ascii_code_target:
                return letter

        return letters[0]


solution = Solution()

print(solution.nextGreatestLetter(["c", "f", "j"], "a"))
print(solution.nextGreatestLetter(["c", "f", "j"], "c"))
print(solution.nextGreatestLetter(["x", "x", "y", "y"], "z"))
