from typing import List


class Solution:
    def sort(self, text: str) -> str:
        chars = sorted(list(text))
        return "".join(chars)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = [[str] for str in strs]

        for i, group in enumerate(new_strs):
            current = self.sort(group[0])

            for j in range(len(new_strs) - 1):
                if i == j:
                    continue

                if i >= len(new_strs) or j >= len(new_strs):
                    break

                test = self.sort(new_strs[j][0])

                if test == current:
                    el = i if len(new_strs[i]) < len(new_strs[j]) else j

                    select = i if el == j else j
                    new_strs[select] = new_strs[i] + new_strs[j]
                    new_strs.pop(el)

        return new_strs


if __name__ == "__main__":
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    # strs = ["stop", "pots", "reed", "", "tops", "deer", "opts", ""]
    # strs = ["hhhhu", "tttti", "tttit", "hhhuh", "hhuhh", "tittt"]
    # strs = ["", "b", ""]
    output = Solution().groupAnagrams(strs)
    print("output", output)
