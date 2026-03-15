class Solution:
    def isValid(self, s: str) -> bool:
        params = {"(": ")", "{": "}", "[": "]"}

        stack = []
        for c in s:
            if c in params.keys():
                stack.append(c)
                continue

            if not stack:
                return False
            elif not params[stack[-1]] == c:
                return False
            else:
                stack.pop()
                continue

        return False if stack else True


if __name__ == "__main__":
    s = "[({))]"
    output = Solution().isValid(s)
    print("output", output)
