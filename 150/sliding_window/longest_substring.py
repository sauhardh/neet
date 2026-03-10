class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        _set = set()
        _max = 0

        while r < len(s):
            while s[r] in _set:
                _set.remove(s[l])
                l += 1

            _set.add(s[r])
            r += 1

            _max = max(len(_set), _max)

        return _max


if __name__ == "__main__":
    s = "pwwkew"
    # s = "zxyzxyz"
    # s = "xxxx"
    # s = "thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsovert"
    output = Solution().lengthOfLongestSubstring(s)
    print("output", output)
