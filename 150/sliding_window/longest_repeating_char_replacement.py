from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        freq = defaultdict(int)

        max_freq = 0
        max_length = 0

        while r < len(s):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1

            max_length = max(r - l + 1, max_length)
            r += 1

        return max_length

    def characterReplacement_GPTWAY(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        max_count = 0
        max_length = 0

        for r in range(len(s)):
            count[s[r]] += 1
            max_count = max(max_count, count[s[r]])

            while (r - l + 1) - max_count > k:
                count[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)

        return max_length


if __name__ == "__main__":
    # s = "AAABABB"
    # k = 1

    # s = "XYYX"
    # k = 2

    # s = "AABABBA"
    # k = 1
    #

    s = "AABA"
    k = 0
    output = Solution().characterReplacement(s, k)
    print("Output", output)
