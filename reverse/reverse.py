class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # rename passed in node as current
        current = node
        # create next variable
        next = None
        # while current is something
        while current is not None:
            # set the next varaible to the next node
            next = current.next_node
            # set the curren't next node to the prev node
            current.next_node = prev
            # set the prev node to the current node
            prev = current
            # move the head pointer to the prev
            self.head = prev
            # move on to the next node
            current = next