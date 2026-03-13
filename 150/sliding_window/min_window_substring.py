class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count_t = {}
        count_s = {}

        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        print(count_t)

        l = 0
        need = len(count_t)
        have = 0
        res = [-1, -1]
        resLen = float("infinity")

        for r in range(len(s)):
            count_s[s[r]] = count_s.get(s[r], 0) + 1

            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                have += 1

            while need == have:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                count_s[s[l]] -= 1

                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""


if __name__ == "__main__":
    s = "OUZODYXAZV"
    t = "XYZ"
    output = Solution().minWindow(s, t)
    print("output", output)
