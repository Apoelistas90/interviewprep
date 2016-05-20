class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):

        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: return None

        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items: return None
        return self.items[len(self.items)-1]


class MaxStack:

    def __init__(self):
        self.stack = Stack()
        self.maxstack = Stack()

    def push(self,item):
        self.stack.push(item)
        if self.maxstack.peek() < item or not self.items:
            self.maxstack.push(item)

    def pop(self):
        item = self.stack.pop()
        if self.maxstack.peek() == item:
            self.maxstack.pop()
        return item

    def getMax(self):
        return self.maxstack.peek()


anObject = Stack()
anObject.push(32)
anObject.push(1)
anObject.push(2)
print(anObject.getMax())
print(anObject.peek())