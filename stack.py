class Stack():
    def __init__(self) -> None:
        self.body = []

    def size(self) -> int:
        """Returns the number of elements on the stack"""
        return len(self.body)

    def is_empty(self) -> bool:
        """Check stack for emptiness. Returns True or False."""
        return self.size() == 0

    def push(self, element) -> None:
        """Adds a new element to the top of the stack."""
        self.body.append(element)

    def pop(self):
        """Removes the top element of the stack, changing the stack.
        Returns the removed stack element"""
        try:
            return self.body.pop()
        except IndexError as err:
            return -1, err

    def peek(self):
        """Returns the top element of the stack.
        The stack doesn't change."""
        try:
            return self.body[-1]
        except IndexError as err:
            return -1, err