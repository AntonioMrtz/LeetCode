# https://leetcode.com/problems/backspace-string-compare/
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        result_s = ""
        result_t = ""

        max_len = len(s) if len(s) > len(t) else len(t)

        for i in range(0, max_len):

            if i < len(s):
                if s[i] == "#" and len(result_s) > 0:
                    result_s = result_s[:-1]

                elif not (s[i] == "#" and len(result_s) == 0):
                    result_s += s[i]

            if i < len(t):

                if t[i] == "#" and len(result_t) > 0:
                    result_t = result_t[:-1]

                elif not (t[i] == "#" and len(result_t) == 0):
                    result_t += t[i]

        return result_s == result_t


solution = Solution()

print(solution.backspaceCompare("ab#c", "ad#c"))
print(solution.backspaceCompare("ab##", "c#d#"))
print(solution.backspaceCompare("a#c", "b"))
print(solution.backspaceCompare("y#fo##f", "y#f#o##f"))
print(solution.backspaceCompare("ab#c", "ad#c"))
