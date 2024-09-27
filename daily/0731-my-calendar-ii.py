# Hint:
# Store two sorted lists of intervals:
# one list will be all times that are at least single booked,
# and another list will be all times that are definitely double booked.
# If none of the double bookings conflict, then the booking will succeed,
# and you should update your single and double bookings accordingly.


class Node:
    def __init__(self, start: int, end: int):
        self.s = start
        self.e = end
        self.l = self.r = None

    def insert(self, start: int, end: int) -> None:
        # double booked interval must not overlap
        if start >= self.e:
            if not self.r:
                self.r = Node(start, end)
            else:
                self.r.insert(start, end)
        elif end <= self.s:
            if not self.l:
                self.l = Node(start, end)
            else:
                self.l.insert(start, end)

    def overlaps(self, start: int, end: int) -> bool:
        if start >= self.e:
            if not self.r:
                return False
            else:
                return self.r.overlaps(start, end)
        elif end <= self.s:
            if not self.l:
                return False
            else:
                return self.l.overlaps(start, end)
        else:
            return True


class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.db_booked = None  # use a BST to speed up non-overlap interval lookups

    def book(self, start: int, end: int) -> bool:
        if self.db_booked is not None and self.db_booked.overlaps(start, end):
            return False

        for s, e in self.booked:
            # max/min is slower than a single comparison
            # if max(start, s) < min(end, e):
            if start < e and end > s:
                if self.db_booked is None:
                    self.db_booked = Node(max(start, s), min(end, e))
                else:
                    self.db_booked.insert(max(start, s), min(end, e))
        self.booked.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
