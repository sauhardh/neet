import enum
from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_vals = list(s)

        for t_val in t:
            if t_val in s_vals:
                pos = s_vals.index(t_val)
                s_vals.pop(pos)

        if not s_vals:
            return True
        return False


if __name__ == "__main__":
    s = "raji"
    t = "jari"
    output = Solution().isAnagram(s, t)
    print("output", output)
