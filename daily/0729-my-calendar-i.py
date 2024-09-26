class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, start, end):
        if self.start >= end:
            if not self.left:
                self.left = Node(start, end)
                return True
            else:
                return self.left.insert(start, end)
        elif self.end <= start:
            if not self.right:
                self.right = Node(start, end)
                return True
            else:
                return self.right.insert(start, end)
        return False


class MyCalendar:

    # using binary search tree is more efficient than using list
    # list traversal: O(n)
    # binary search tree: O(log n)

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(start, end)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
