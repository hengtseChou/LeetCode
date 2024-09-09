class MyQueue:

    # stack: last in first out
    # queue: first in first out
    # must use valid stack operation to implement queue

    def __init__(self):

        self.enqueue_stack = []
        self.dequeue_stack = []

    def push(self, x: int) -> None:
        
        self.enqueue_stack.append(x)

    def pop(self) -> int:

        if len(self.dequeue_stack) != 0:
            return self.dequeue_stack.pop(-1)
        while (self.enqueue_stack):
            tmp = self.enqueue_stack.pop(-1)
            self.dequeue_stack.append(tmp)
        return self.dequeue_stack.pop(-1)
        

        
    def peek(self) -> int:

        if len(self.dequeue_stack) != 0:
            return self.dequeue_stack[-1]
        while (self.enqueue_stack):
            tmp = self.enqueue_stack.pop(-1)
            self.dequeue_stack.append(tmp)
        return self.dequeue_stack[-1]

    def empty(self) -> bool:

        return (not self.enqueue_stack and not self.dequeue_stack)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
