from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "/", "*"]
        values = []

        for x in tokens:
            if x in operators:
                if len(values) < 2:
                    continue

                val1 = int(values.pop())
                val2 = int(values.pop())

                match x:
                    case "+":
                        calc = val2 + val1
                    case "-":
                        calc = val2 - val1
                    case "/":
                        calc = val2 / val1
                    case "*":
                        calc = val2 * val1

                values.append(calc)
            else:
                values.append(x)

        return int(values[0])


if __name__ == "__main__":
    # tokens = ["1", "2", "+", "3", "*", "4", "-"]
    tokens = ["18"]
    output = Solution().evalRPN(tokens)
    print("output", output)
