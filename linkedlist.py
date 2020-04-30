
class Node:
    val = None
    next_node = None
    iterator_pos = None

    def __init__(self, new_val):
        self.val = new_val
        self.iterator_pos = self

    def __str__(self):
        return str(self.val)

    def __iter__(self):
        print("Yielding iterator_pos " + str(self.iterator_pos))
        yield self.iterator_pos
        print("After yield")
        self.iterator_pos = self.iterator_pos.get_next()

    def get_next(self):
        print("Moving ahead one node in next()")
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def append_to_tail(self, val):
        new_node = Node(val)
        if not self.next_node:
            self.next_node = new_node
        else:
            next_checked = self.next_node
            while next_checked:
                next_to_last = next_checked
                next_checked = next_to_last.get_next()
            assert(next_checked is None)
            next_to_last.set_next(new_node)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.append_to_tail(n2)
n1.append_to_tail(n3)
n1.append_to_tail(n4)

for n in n1:
    print(str(n))