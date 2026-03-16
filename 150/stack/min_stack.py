class MinStack:
    def __init__(self):
        self.stack = []  # [(value, min_till_now)]

    def push(self, val: int) -> None:
        min_till_now = (
            val if not self.stack or self.stack[-1][1] > val else self.stack[-1][1]
        )

        self.stack.append((val, min_till_now))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return 0

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    minstack = MinStack()
    minstack.push(1)
    minstack.push(2)
