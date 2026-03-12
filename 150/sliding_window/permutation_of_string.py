class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0

        count1 = [0] * 26
        count2 = [0] * 26

        for c in s1:
            count1[ord(c) - ord("a")] += 1

        for r in range(len(s2)):
            count2[ord(s2[r]) - ord("a")] += 1

            while r - l + 1 > len(s1):
                count2[ord(s2[l]) - ord("a")] -= 1
                l += 1

            if count1 == count2:
                return True

        return False

    def checkInclusionGPT(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for c in s1:
            count1[ord(c) - ord("a")] += 1

        l = 0

        for r in range(len(s2)):
            count2[ord(s2[r]) - ord("a")] += 1

            if r - l + 1 > len(s1):
                count2[ord(s2[l]) - ord("a")] -= 1
                l += 1

            if count1 == count2:
                return True

        return False


if __name__ == "__main__":
    s1 = "abc"
    s2 = "lecabee"
    output = Solution().checkInclusion(s1, s2)
    print("output", output)
