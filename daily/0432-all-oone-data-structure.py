# hash map: maintain a relationship of key -> corresponding counting node
# doubly linked list: store keys in ascending order of count


class Node:
    def __init__(self, key="", count=0):
        self.count = count
        self.keys = {key}
        self.prev = self.next = None

    # circular linked list
    def insert(self, node):
        node.prev = self
        node.next = self.next
        node.prev.next = node
        node.next.prev = node
        return node

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev


class AllOne:

    def __init__(self):
        self.root = Node()
        self.root.next = self.root
        self.root.prev = self.root
        self.nodes = {}

    def inc(self, key: str) -> None:
        root, nodes = self.root, self.nodes
        if key not in nodes:
            if root.next == root or root.next.count > 1:
                # next counting node (which is 1) does not exist
                nodes[key] = root.insert(Node(key, 1))
            else:
                root.next.keys.add(key)
                nodes[key] = root.next
        else:
            curr_node = nodes[key]
            if curr_node.next == root or curr_node.next.count > curr_node.count + 1:
                # next counting node does not exist
                nodes[key] = curr_node.insert(Node(key, curr_node.count + 1))
            else:
                curr_node.next.keys.add(key)
                nodes[key] = curr_node.next
            # if key is not new, then must handle the prev count
            curr_node.keys.discard(key)
            if not curr_node.keys:
                curr_node.remove()

    def dec(self, key: str) -> None:
        root, nodes = self.root, self.nodes
        curr_node = nodes[key]
        if curr_node.count == 1:
            nodes.pop(key)
        else:
            if curr_node.prev == root or curr_node.prev.count < curr_node.count - 1:
                nodes[key] = curr_node.prev.insert(Node(key, curr_node.count - 1))
            else:
                curr_node.prev.keys.add(key)
                nodes[key] = curr_node.prev
        curr_node.keys.discard(key)
        if not curr_node.keys:
            curr_node.remove()

    def getMaxKey(self) -> str:
        return next(iter(self.root.prev.keys))

    def getMinKey(self) -> str:
        return next(iter(self.root.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
