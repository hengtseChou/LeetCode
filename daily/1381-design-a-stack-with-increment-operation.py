class CustomStack:

    # ref: https://algo.monster/liteproblems/1381
    # this gives O(1) in increment
    # otherwise, simple list method would work

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.add = [0] * maxSize
        self.size = 0

    def push(self, x: int) -> None:
        if self.size < len(self.stack):
            self.stack[self.size] = x
            self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        self.size -= 1
        ans = self.stack[self.size] + self.add[self.size]
        # transfer the increment to the next element to be popped
        if self.size > 0:
            self.add[self.size - 1] += self.add[self.size]
        self.add[self.size] = 0
        return ans

    def increment(self, k: int, val: int) -> None:
        limit = min(k, self.size) - 1
        if limit >= 0:
            self.add[limit] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
