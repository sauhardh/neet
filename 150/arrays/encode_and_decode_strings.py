from typing import List

"""
encode
 - reverse word
 - (length of word)(delimiter)(word)
 - Example: 
    - ["Hello", "World"]
    - Output: 5#World5#Hello
"""


class Solution:
    def __init__(self):
        self.delimiter = "#"

    def encode(self, strs: List[str]) -> str:
        output = ""

        for st in reversed(strs):
            length = len(st)
            output += str(length) + self.delimiter + st

        return output

    def decode(self, s: str) -> List[str]:
        output = []

        strs = list(s)
        end = 1
        while len(strs) > 0:
            char = "".join(strs[0:end])

            if isinstance(int(char), int) and strs[end] != self.delimiter:
                end += 1
                continue

            if isinstance(int(char), int) and strs[end] == self.delimiter:
                strs = strs[end + 1 :]
                word = "".join(strs[: int(char)])
                output.append(word)

                strs = strs[len(word) :]
                end = 1

        return output[::-1]


if __name__ == "__main__":
    strs = ["Hello", "World"]
    soln = Solution()
    output = soln.decode(soln.encode(strs))
    print(output)
