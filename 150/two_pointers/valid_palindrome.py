class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def isPalindromeNormal(self, s: str) -> bool:
        strs = []
        for c in s:
            if c.isalnum():
                strs.append(c.lower())

        front = "".join(strs)
        strs.reverse()
        back = "".join(strs)

        if front == back:
            return True

        return False


if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    output = Solution().isPalindrome(s)
    print("output", output)
